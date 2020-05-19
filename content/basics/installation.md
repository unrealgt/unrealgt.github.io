---
title: "Installation"
date: 2019-07-26T14:14:04+02:00
draft: false
weight: 2
---

### Requirements

- Unreal Engine 4.24 or higher (you can try older versions but some features might not work as expected)

#### Windows

- Visual Studio 2017 or 2019 (2015 should work aswell but is not tested)

#### macOS

- XCode Command Line Tools

#### Linux

- Nothing if you already built the engine from source

## Installation

The only way to install the plugin is to build it from Source in an existing project.
This requires you to build your project from source manually.

1. Clone this repository into your projects plugin Directory.

2. Generate the project files (Cmake, Visual Studio Solution, Vscode workspace...) files by right clicking your projects `.uproject` file on Windows/macOS or by with `GenerateProjectFiles.sh` on linux.

3. Build & Run the generated solution/cmake project from your IDE or the CLI.<br>Select DebugGameEditor or DevelopmentGameEditor as Target.

4. After the Editor has launched goto `Edit > Plugins` and enable the UnrealGT plugin.
