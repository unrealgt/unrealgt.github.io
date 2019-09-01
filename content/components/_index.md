+++
title = "Components"
date = 2019-08-20T14:59:59+02:00
weight = 2
chapter = true
pre = "<b>2. </b>"
+++

### Chapter 2

# Generators, Streamers & Triggers

The data generation process is split into 3 different component types. These components can be combined to create complex data generation constructs.<br>
The basic generation workflow will look like this:
`Trigger -> Generator -> Streamer`<br>
Tirggers are used to kick of the generation, a trigger can be time based or based on an event (a motion sensor for example).<br>
Generators are resposible for data collection from the scene.<br>
Streamers can than be used to transport the collected data from the engine to an external storage or API (e.g. the File System).<br>

