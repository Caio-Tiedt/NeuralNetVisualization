# NeuralNetVisualization
A python function to draw a Neural Network Model with the values of each connection between nodes and biases.

Works with neural networks created using the keras library. To get keras, run

from tensorflow import keras
from tensorflow.keras import layers

Then create and train your model using, for example this linear model

linmodel = keras.Sequential([
    layers.Dense(units=1, input_shape=[numinput])
])

linmodel.compile(
    optimizer="adam",
    loss="mae",
)

linhistory = linmodel.fit(
    X_train, y_train,
    validation_data=(X_valid, y_valid),
    epochs=1000,
    verbose=0,  # turn off training log
)

Now to visualize just run:

NeuralNetvisualization(linmodel)
