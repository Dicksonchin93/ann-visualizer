from keras.models import Sequential
import unittest
import keras
from keras.layers import Input, Dense
from keras.models import Model
from keras_architecture_visualizer.visualize import KerasArchitectureVisualizer
from efficientnet.keras import EfficientNetB3

class MyTestCase(unittest.TestCase):
    def test_keras_architecture_vis(self):
        network = Sequential()
        # Hidden Layer#1
        network.add(Dense(units=6,
                          activation='relu',
                          kernel_initializer='uniform',
                          input_dim=11))

        # Hidden Layer#2
        network.add(Dense(units=6,
                          activation='relu',
                          kernel_initializer='uniform'))

        # Exit Layer
        network.add(Dense(units=1,
                          activation='sigmoid',
                          kernel_initializer='uniform'))
        vis = KerasArchitectureVisualizer()
        vis.visualize(network)

    def test_functional_api_for_image(self):
        inputs = Input(shape=((50,50,3)))
        # a layer instance is callable on a tensor, and returns a tensor
        l1 = Dense(units=800, kernel_initializer=keras.initializers.Ones(), activation='relu')(
            inputs)
        l2 = Dense(units=800, kernel_initializer=keras.initializers.Ones(), activation='relu')(l1)
        lo = Dense(10, activation='softmax')(l2)

        # This creates a model that includes
        # the Input layer and three Dense layers
        model = Model(inputs=inputs, outputs=lo)
        model.compile(optimizer='rmsprop',
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])
        vis = KerasArchitectureVisualizer()
        vis.visualize(model)

    def test_efficientnet(self):
        model = EfficientNetB3(weights=None)
        vis = KerasArchitectureVisualizer()
        vis.visualize(model)

if __name__ == '__main__':
    unittest.main()
