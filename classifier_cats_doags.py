#problem:
# Build a neural network that classifies images.
# Train this neural network.
# And, finally, evaluate the accuracy of the model.

# answer
import tensorflow as tf

mnist = tf.keras.datasets.mnist
X_train,y_train,X_test,y_test = mnist.load_data()
X_train,X_test = X_train / 255.0, X_test / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=(28,28)),
    tf.keras.layers.Dense(128,activation='relu',),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])