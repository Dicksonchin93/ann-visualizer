# Keras Architecture Visualizer

A great visualization python library used to work with Keras. It uses python's graphviz library to create a presentable graph of the neural network you are building.

## Installation
### From Github
1. Download the `keras_architecture_visualizer` folder from the github repository.
2. Place the `keras_architecture_visualizer` folder in the same directory as your main python script.

### From pip
Use the following command:

```bash
pip install keras_architecture_visualizer
```

Make sure you have graphviz installed. Install it using:

```bash
sudo apt-get install graphviz && pip install graphviz
```

## Usage

```python

from keras_architecture_visualizer import KerasArchitectureVisualizer
#Build your model here
vis = KerasArchitectureVisualizer()
vis.visualize(model)
```

## Documentation

### KerasArchitectureVisualizer(filename="network.gv", title="MyNeural Network")
* `model` - The Keras Sequential/Functional model
* `view` - If True, it opens the graph preview after executed
* `filename` - Where to save the graph. (.gv file format)
* `title` - A title for the graph

## Example KerasArchitectureVisualizer
```python
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras_architecture_visualizer import KerasArchitectureVisualizer

network = Sequential()
        #Hidden Layer#1
network.add(Dense(units=6,
                  activation='relu',
                  kernel_initializer='uniform',
                  input_dim=11))

        #Hidden Layer#2
network.add(Dense(units=6,
                  activation='relu',
                  kernel_initializer='uniform'))

        #Exit Layer
network.add(Dense(units=1,
                  activation='sigmoid',
                  kernel_initializer='uniform'))

vis = KerasArchitectureVisualizer()
vis.visualize(model, title="")
```

This will output:
![photo](https://i.imgur.com/ngThGlk.png)

## Example CNN
```python
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras_architecture_visualizer import KerasArchitectureVisualizer
model = build_cnn_model()
vis = KerasArchitectureVisualizer()
vis.visualize(model, title="")

def build_cnn_model():
  model = keras.models.Sequential()

  model.add(
      Conv2D(
          32, (3, 3),
          padding="same",
          input_shape=(32, 32, 3),
          activation="relu"))
  model.add(Dropout(0.2))

  model.add(
      Conv2D(
          32, (3, 3),
          padding="same",
          input_shape=(32, 32, 3),
          activation="relu"))
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Dropout(0.2))

  model.add(
      Conv2D(
          64, (3, 3),
          padding="same",
          input_shape=(32, 32, 3),
          activation="relu"))
  model.add(Dropout(0.2))

  model.add(
      Conv2D(
          64, (3, 3),
          padding="same",
          input_shape=(32, 32, 3),
          activation="relu"))
  model.add(MaxPooling2D(pool_size=(2, 2)))
  model.add(Dropout(0.2))

  model.add(Flatten())
  model.add(Dense(512, activation="relu"))
  model.add(Dropout(0.2))

  model.add(Dense(10, activation="softmax"))

  return model
```

This will output:
![photo](https://i.imgur.com/v3QpACl.png)

