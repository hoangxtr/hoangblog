---
layout: post
title: Squeeze and Excitation Networks 
subtitle: A little bit about SENet 
thumbnail-img: https://www.researchgate.net/profile/Somshubra-Majumdar/publication/322517887/figure/fig2/AS:583263630401536@1516072294413/The-computation-of-the-temporal-Squeeze-and-Excite-block.png
# share-img: /assets/img/path.jpg
tags: [Paper sumary, Computer Vision]
---

# Squeeze-and-Excitation Networks 

*"Let’s add parameters to each channel of a convolutional block so that the network can adaptively adjust the weighting of each feature map."*

## Why
CNNs use their convolutional filters to extract information from images. Lower layers find trivial pieces of context like edges or high frequencies, while upper layers can detect faces, text or other complex geometrical shapes. They extract whatever is necessary to solve a task efficiently.

![](https://miro.medium.com/max/2000/1*bmObF5Tibc58iE9iOu327w.png)

Before the apperance of this paper, CNN often use many kernel to extract information from a input, and **the network weights each of its channels equally when creating the output feature maps**. It someway cannot make impression for the important channels.SENets are all about changing this by adding a content aware mechanism (cơ chế nhận biết thông tin) to weight each channel adaptively. In it’s most basic form this could mean adding a single parameter to each channel and giving it a linear scalar how relevant each one is **(Nói tóm gọn lại là đánh trọng số cho mỗi channel**).

## How
All it need to do simply add a SE-Block after the feature map so that it can make an impression for the important channels of feature map.
``` python
def se_block(in_block, ch, ratio=16):
    x = GlobalAveragePooling2D()(in_block)
    x = Dense(ch//ratio, activation='relu')(x)
    x = Dense(ch, activation='sigmoid')(x)
    return multiply()([in_block, x])
```

![](https://miro.medium.com/max/748/1*WNk-atKDUsZPvMddvYL01g.png)
These five steps add almost no additional computation cost (about 0.26% GFLOPs of ResNet-50 as author's experiment). The authors show that by adding SE-blocks to ResNet-50 it can expect almost the same accuracy as ResNet-101 delivers. This is impressive for a model requiring only half of the computational costs.

When put SE-blocks to resnet, we have SE-resnet, it can be shown like that bellow:
![](https://www.researchgate.net/publication/332436202/figure/fig1/AS:748129708171266@1555379430914/The-SE-ResNet-module-architecture-A-Basic-SE-ResNet-module-B-Bottleneck-SE-ResNet.png)

## Result 

The paper further investigates other architectures like Inception, Inception-ResNet and ResNeXt. The latter leads them to a modified version that shows a top-5 error of 3.79% on ImageNet. 
![](https://miro.medium.com/max/875/1*35_UHH8pDshPfqtBB-MbDA.png)

What amazes me the most about SENets is just how simple and yet effective they are. Being able to add this approach to any model at almost no cost, should make you jump back to the drawing board and retraining everything you ever built. 
