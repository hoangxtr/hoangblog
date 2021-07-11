---
layout: post
title: Introduce about Mediapipe
subtitle: A little bit introduction about Mediapipe
thumbnail-img: /assets/img/mediapipe.png
share-img: /assets/img/path.jpg
tags: [Mediapipe, Computer Vision, Google Framework]
---

## What is Mediapipe
It is a open source framework released by google for machine learning solutions. A key “selling” point (it’s free) of Mediapipe is that the code is written in c++, but it can easily be deployed to any platform, from web assembly to Android to MacOS.      
When it first released, Mediapipe had only a few demos, but now their GitHub page boasts almost a dozen different demos from persistent object tracking, AR hair coloring, to pose tracking that may leave OpenPose in the dust.

## Why Mediapipe ?
Simply, because it's fast. When looking for hand tracking options, our team had two choices, OpenPose and MediaPipe. The first thing that stood out between the two was the absolute difference in speed. On an old Mac, MediaPipe had a sluggish **7 frames per second** while OpenPose would be lucky to have **7 seconds per frame**.  
MediaPipe is able to achieve its speed thanks to the use of GPU acceleration and multi-threading. The multi-threading and GPU acceleration allow newer phones to run away with frames, often being at FPS too high to see with the human eye.

## Working with Mediapipe



## Reference
https://medium.com/swlh/a-review-of-googles-new-mobile-friendly-ai-framework-mediapipe-25d62cd482a1#:~:text=Mediapipe%20is%20an%20open%2Dsource,under%20development%20for%20far%20longer.