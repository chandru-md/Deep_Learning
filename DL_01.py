import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

# 1. Create sample dataset
X = np.random.rand(1000, 10)   # 1000 samples, 10 features
y = (np.sum(X, axis=1) > 5).astype(int)  # binary labels

# 2. Build model
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(10,)),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

# 3. Compile model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# 4. Train model
model.fit(X, y, epochs=10, batch_size=32)

# 5. Evaluate
loss, acc = model.evaluate(X, y)
print(f"Accuracy: {acc:.4f}")

# Improve model
layers.Dropout(0.3)  # prevent overfitting

#Add call backs
from tensorflow.keras.callbacks import EarlyStopping

early_stop = EarlyStopping(patience=3)
model.fit(X, y, epochs=50, callbacks=[early_stop])

#CNN Example - Image Model
model = keras.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])