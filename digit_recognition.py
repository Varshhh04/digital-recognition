print("Script started...")

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Load the MNIST dataset
print("Loading dataset...")
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Normalize the images (scale pixel values to [0,1])
x_train, x_test = x_train / 255.0, x_test / 255.0

# Reshape data to fit CNN input format (28x28x1)
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)

print("Dataset loaded and preprocessed.")

# Build the CNN Model
print("Building model...")
model = Sequential([
    Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    MaxPooling2D((2,2)),
    Conv2D(64, (3,3), activation='relu'),
    MaxPooling2D((2,2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model
print("Training model...")
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test), verbose=1)

# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"\nTest Accuracy: {test_acc:.4f}")

# Test with a random image from the test set
print("Testing with a random image...")
index = np.random.randint(0, len(x_test))

# Show the image
plt.imshow(x_test[index].reshape(28,28), cmap='gray')
plt.title(f"Actual: {y_test[index]}")
plt.show()

# Predict
prediction = model.predict(x_test[index].reshape(1, 28, 28, 1))
predicted_digit = np.argmax(prediction)

print(f"Predicted Digit: {predicted_digit}")
