import re

import glob

import sys

import os

import json

def commentContent(text):
    for comment in re.findall(r'\*\*(.*?)\*\/', text, re.S):
        return re.sub('\n+', '', re.sub(r'\n[ ]*\*+', ' ', comment).strip())

headerFiles = glob.glob(sys.argv[1] + '/**/*.h', recursive=True)

for headerFile in headerFiles:
    headerFileContent = open(headerFile).read()

    classDocComment = re.findall(r'(\/\*\*[\s\w.,()*="\'&\-+!\[\]:\/<>#`{}]*\*\/\s*)(?:UCLASS\([\s\w.,()*="\'&\-+!\[\]:\/<>#{}`]*?\)\n|(?:class UNREALGT_API))', headerFileContent)
    classDocCommentContent = commentContent(classDocComment[0]) if classDocComment else ""

    resultObject = {'filename': headerFile, 'description': classDocCommentContent, 'properties': []}

    # haters will argue that parsing cpp with a regex is stupid,
    # but for this usecase it's good enough
    propertyMatches = re.findall(r'(\/\*\*[\s\w.,()*="\'&\-+!\[\]:\/<>#`{}]*\*\/\s*)?UPROPERTY\(([\s\w.,()*="\'{}&\-+!\[\]:\/<>#`{}]*?(?:Edit|ShowOnlyInnerProperties)[\s\w.,()*="\'{}&\-+!\[\]:\/<>#`{}]*?)\)\n\s+(.+?)(\s\w+);', headerFileContent)
    for captures in propertyMatches:
        description = commentContent(captures[0])
        category = re.findall(r'Category = "?(\w+)"?', captures[1])
        category = category[0] if category else ""
        resultObject['properties'].append({
            'description': description if description else '',
            'category': category,
            'propType': captures[2],
            'name': captures[3]
        })
    
    jsonOutFile = open(os.path.join(sys.argv[2], os.path.splitext(os.path.basename(headerFile))[0]) + '.json', "w")
    json.dump(resultObject, fp=jsonOutFile, indent=4)


# python3 /Users/lmbp/projects/github/unrealgt.github.io/generate_properties.py /Users/lmbp/projects/github/UnrealLab/Plugins/ULab /Users/lmbp/projects/github/unrealgt.github.io/data
