---
layout: post
title: Understanding backpropagation
subtitle: Some knowleadges about backpropagation
thumbnail-img: /assets/img/backpropogation_title.jpeg
share-img: /assets/img/path.jpg
tags: [Deep learning, Computer Vision, Backpropagation, Neural network]
---

## Understand backpropagation
- Neural network is the most important basis of Deep learning. It's release has brought AI closer to us. It like human's brain.
![](../assets/img/neural_network.png)

## Forwarding 
- This is process calculate value for each node in the neural network. It's have us to inferred output of neural network. 

## Backpropagation
- It's a process of updating weights of neural network using optimize algorithms like Gradient Descent (SGD, RMS, ...)
- Here we will example backpropagation of a neural network like bellow, with:
    - Loss: MSE
    - activation at each node: sigmoid  

    ![](../assets/img/backprob.png)


    - In order to update weight, Gradient Descent requires us to calc derivative of Loss by each weight, so can have:
    ![](../assets/img/backprob1.jpg)
    
    So in order to calc derivative of loss by weight, we only need to calculate ![equation](https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_red&space;\inline&space;\delta&space;_{j}) 

    - Because derivative computation of loss of the output layer different from the hidden layer, so we have separately result:
        - With output layer:  
        ![](../assets/img/backprob2.jpg)

        - With hidden layer:
        ![](../assets/img/backprob3.jpg)
        Asume that **k** is the layer next to **j**
### Implement backpropagation step by step
- Initiate weights for neural network, randomly or by some methods
- For each training example:
    - Forward the input to calculate the value for nodes (hidden or output layer).
    - For each output k (model have many output):  
    ![equation](https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_pink&space;\inline&space;\delta&space;_{k}&space;=&space;o&space;*&space;(1-o)&space;*&space;(t-o))

    - For each node in hidden layer (h is activation):  
    ![equation](https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_pink&space;\inline&space;\delta&space;_{j}&space;=&space;\sum_{k}^{}&space;\delta&space;_{k}&space;*&space;w_{kj}&space;*&space;h'(a&space;_{j}))

    - Update each network weight:  
    ![equation](https://latex.codecogs.com/png.image?\dpi{110}&space;\bg_pink&space;\inline&space;w&space;_{ji}&space;<-&space;w&space;_{ji}&space;&plus;&space;\eta&space;&space;*&space;\delta&space;_{j}&space;*&space;z&space;_{j})