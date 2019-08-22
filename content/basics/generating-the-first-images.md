---
title: "Generating the First Images"
date: 2019-07-26T14:20:36+02:00
draft: false
weight: 2
---

Open a scene of your choice in the Editor.

{{< figure src="../images/create_blueprint.png" class="captionright" height="300" caption="Right click in the content Browser and create a new Blueprint and choose Actor as base class." >}}

Open your Blueprint in the editor.

{{< figure src="../images/add_components.png" class="captionleft" height="300" caption="Add the following components to your created Blueprint: ULImageGenerator, ULFileStreamer, ULTimedCaptureTrigger and an **optional** ULCameraMovement" >}}

## Component Configuration

**ULImageGenerator**

The Image generator is responsible for generating pixel data from the scene.  
You can configure the resolution and output image format.
We use BMP as format in this example since it doesn't require CPU heavy compression.  
Keep in mind that multiple image generators or high resolutions will degrade your performance at runtime, because each image generator requires it's own render pass.

{{< figure src="../images/image_generator_properties.png" class="captionleft" height="300">}}

**ULFileStreamer**

A Streamer component streams generated Data. In this case the generated image will be streamed into a file.

To link the streamer with a generator select the image generator from the dropdown. If it doesn't show up hit compile at the top and retry.

{{< figure src="../images/file_streamer_properties.png" class="captionleft" height="300">}}

You can also set the naming convention for the created files.
You have access to `{ID}` and `{Time}` as variables.
The files are stored inside your Projects `Saved` Directory in the `ULab` folder.

**ULTimedCaptureTrigger**

This component is responsible for triggering Data generation.
Generator Components that should be triggered by this component, must be added to the TriggerComponents Array.

{{< figure src="../images/timed_capture_properties.png" class="captionleft" height="300">}}

In this case the generation is triggered at a fixed time interval which can be modified by changing the Frame Rate parameter `1/framerate = time between images in seconds`.
Be careful with high frame rates or the TriggerEveryFrame options as those will heavily degrade performance.

**ULCameraMovement (optional)**

If you don't want to capture at a fixed location you can add
a CameraMovementComponent to your blueprint. This component will add some basic movement capabilities to your Blueprint/Actor, which can be configured in the properties tab.

We choose the default Follow Main View as movement mode.
(TODO movement mode will be an enum in the future update image)

{{< figure src="../images/camera_movement_properties.png" class="captionleft" height="300">}}

* `Follow Main View` will follow your main viewport camera/player
* `Follow Actor` will follow a actor, this actor can only be selected after the Blueprint has been placed in a level
* `Follow Rail` will follow a camera Rail Actor, you can configure the speed at which our Blueprint Actor will follow the rail.  
Tutorial for camera rails: https://docs.unrealengine.com/en-us/Engine/Sequencer/HowTo/CameraRigRail you can skip 2-3. and 9.-16, we will use our blueprint as cine camera instead and the movement a long the rail is handled by this component not the sequencer.

Examples: https://github.com/lolleko/UnrealLab/tree/master/Plugins/ULab/Content/Examples

## First Test

Once you configured your components save and compile your blueprint.

Drag and drop your blueprint from the content browser into the scene.
You should see a camera indicating the direction your ImageGenerator is going to record.

Start the simulation and images should get generated in your `Saved/ULab` directory.

