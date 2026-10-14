
from pathlib import Path
import json

import tensorflow as tf
from tensorflow.keras import layers, models

# Project and dataset paths
BASE_DIR = Path(__file__).resolve().parent
DATASET_DIR = BASE_DIR / "dataset"
MODEL_DIR = BASE_DIR / "models"
MODEL_DIR.mkdir(exist_ok=True)

TRAIN_DIR = DATASET_DIR / "Training"
VAL_DIR = DATASET_DIR / "Validation"

# Image settings
IMG_SIZE = (64, 64)
BATCH_SIZE = 32
SEED = 42

# Load training images
train_data = tf.keras.utils.image_dataset_from_directory(
    TRAIN_DIR,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    label_mode="int",
    color_mode="rgb",
    seed=SEED,
    shuffle=True
)

# Load validation images using the same class order
class_names = train_data.class_names

val_data = tf.keras.utils.image_dataset_from_directory(
    VAL_DIR,
    class_names=class_names,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    label_mode="int",
    color_mode="rgb",
    shuffle=False
)

print("Alphabet classes:", class_names)
print("Number of classes:", len(class_names))

# Improve data-loading performance
AUTOTUNE = tf.data.AUTOTUNE
train_data = train_data.prefetch(AUTOTUNE)
val_data = val_data.prefetch(AUTOTUNE)

# Build a Convolutional Neural Network (CNN)
model = models.Sequential([
    layers.Input(shape=(64, 64, 3)),
    layers.Rescaling(1.0 / 255),

    layers.Conv2D(32, 3, activation="relu"),
    layers.MaxPooling2D(),

    layers.Conv2D(64, 3, activation="relu"),
    layers.MaxPooling2D(),

    layers.Conv2D(128, 3, activation="relu"),
    layers.MaxPooling2D(),

    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dropout(0.3),
    layers.Dense(len(class_names), activation="softmax")
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

model.summary()

# Train the model
history = model.fit(
    train_data,
    validation_data=val_data,
    epochs=10
)

# Save the trained model and class names
model.save(MODEL_DIR / "isl_model.keras")

with open(MODEL_DIR / "class_names.json", "w") as file:
    json.dump(class_names, file)

print("\nTraining completed!")
print("Model saved to:", MODEL_DIR / "isl_model.keras")
print("Class names saved to:", MODEL_DIR / "class_names.json")
