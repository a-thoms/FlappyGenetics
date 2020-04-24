import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras import Sequential
from random import randint
import numpy as np

class Brain:
    def __init__(self, input_size, hidden_size, output_size, **kwargs):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.model = self.setup_model()

        if kwargs:
            self.model.get_layer("x1").set_weights(kwargs["x1_weights"])
            self.model.get_layer("x2").set_weights(kwargs["x2_weights"])

    def setup_model(self):
        model = tf.keras.Sequential()
        model.add(Dense(self.hidden_size, input_shape=(self.input_size,), name="x1"))
        model.add(Dense(self.output_size, name="x2"))
        model.summary()
        return model

    def crossover(self, mate_brain):
        a_x1_weights = self.model.get_layer("x1").weights[0]
        a_x2_weights = self.model.get_layer("x2").weights[0]
        b_x1_weights = mate_brain.get_layer("x1").weights[0]
        b_x2_weights = mate_brain.get_layer("x2").weights[0]

        x1_shape = a_x1_weights.shape
        x2_shape = a_x2_weights.shape
        alea_n = randint(0, x1_shape[0])
        alea_m = randint(0, x1_shape[1])

        child1_x1_weights = np.ones(x1_shape)
        child1_x2_weights = np.ones(x2_shape)
        child2_x1_weights = np.ones(x1_shape)
        child2_x2_weights = np.ones(x2_shape)

        child1_x1_weights[0:alea_n, 0: alea_m] = a_x1_weights[0: alea_n, 0: alea_m]
        child1_x1_weights[alea_n: x1_shape[0], alea_m: x1_shape[1]] = b_x1_weights[alea_n: x1_shape[0], alea_m: x1_shape[1]]
        child1_x2_weights[0:alea_n, 0: alea_m] = a_x2_weights[0: alea_n, 0: alea_m]
        child1_x2_weights[alea_n: x1_shape[0], alea_m: x1_shape[1]] = b_x2_weights[alea_n: x1_shape[0], alea_m: x1_shape[1]]

        child2_x1_weights[0:alea_n, 0: alea_m] = b_x1_weights[0: alea_n, 0: alea_m]
        child2_x1_weights[alea_n: x1_shape[0], alea_m: x1_shape[1]] = a_x1_weights[alea_n: x1_shape[0], alea_m: x1_shape[1]]
        child2_x2_weights[0:alea_n, 0: alea_m] = b_x2_weights[0: alea_n, 0: alea_m]
        child2_x2_weights[alea_n: x1_shape[0], alea_m: x1_shape[1]] = a_x2_weights[alea_n: x1_shape[0], alea_m: x1_shape[1]]

        # child1_x1_tf_weights = tf.Variable(child1_x1_weights)
        # child1_x2_tf_weights = tf.Variable(child1_x2_weights)
        # child2_x1_tf_weights = tf.Variable(child2_x1_weights)
        # child2_x2_tf_weights = tf.Variable(child2_x2_weights)

        #layer.setweights
        child1_brain = Brain(self.input_size, self.hidden_size, self.output_size, x1_weights=child1_x1_weights, x2_weights=child1_x2_weights)
        child2_brain = Brain(self.input_size, self.hidden_size, self.output_size, x1_weights=child2_x1_weights, x2_weights=child2_x2_weights)

        return child1_brain, child2_brain


b1 = Brain(2, 32, 1)
b2 = Brain(2, 32, 1)
b1.crossover(b2.model)
