---
layout: post
title: Working with model in Tensorflow
subtitle: All things you need to use model in Tensorflow
cover-img: /assets/img/tensorflow.jpg
thumbnail-img: /assets/img/tensorflow.jpg
share-img: /assets/img/path.jpg
tags: [Tensorflow, Computer Vision]
---

## Component of a model
- Architecture of model
- Weights value of model
- Training configuration (loss, optimizer)
- The state of optimizer, which allow you to resume to training exactly where you left off

## Kind of save a model

### Save entire of the model
- We use function :
```python
model.save('model.h5)
```

- So when load model, we use:
```python
new_model = load_model('model.h5')
```
- With this method, we can get the origin model without do anythings

### Save the model architecture only
- We save architecture only, without weight values, configuration or optimizer state

- We can save as json
```python
json_string = model.to_json()
```
or 
```python
yal_string = model.to_yal()
```
- We can reload **only model architecture** with
```python
new_model = model_from_json(json_string)
```

### Save the model weight values
- It saves **only weight values** without architecture, configurations ,..., so you can only load it if you have model architecture
- Save weights
```python
model.save_weights('weights.h5')
```
- Load weights   

```python
model = Sequential()
model.add(Conv2D(64, (3,3), input_shape=(64,64), activation='relu')
model.add(Conv2D(128, (3,3), input_shape=(64,64), activation='relu')
model.add(Conv2D(256, (3,3), input_shape=(64,64), activation='relu')

model.load_weights('weights.h5')
```
