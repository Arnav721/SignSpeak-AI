
from pathlib import Path
import json

import numpy as np
import streamlit as st
import tensorflow as tf
from PIL import Image

# Project paths
BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "models" / "isl_model.keras"
CLASSES_PATH = BASE_DIR / "models" / "class_names.json"

st.set_page_config(
    page_title="SignSpeak AI",
    page_icon="🤟",
    layout="centered"
)

st.title("🤟 SignSpeak AI")
st.write("Indian Sign Language Alphabet Recognition")
st.write("Upload an image of a hand sign to predict its alphabet.")

@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)

model = load_model()

with open(CLASSES_PATH, "r") as file:
    class_names = json.load(file)

uploaded_file = st.file_uploader(
    "Upload a sign-language image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    st.image(image, caption="Uploaded hand sign", width=300)

    # Prepare image for the model
    resized_image = image.resize((64, 64))
    image_array = np.array(resized_image, dtype=np.float32)
    image_array = np.expand_dims(image_array, axis=0)

    # Predict the letter
    predictions = model.predict(image_array, verbose=0)[0]
    predicted_index = int(np.argmax(predictions))
    predicted_letter = class_names[predicted_index]
    confidence = float(predictions[predicted_index]) * 100

    st.subheader(f"Predicted Letter: {predicted_letter}")
    st.metric("Model Confidence", f"{confidence:.2f}%")

    st.caption(
        "Confidence is the model's estimated probability, "
        "not a guarantee that the prediction is correct."
    )

    # Show the top three predictions
    top_indices = np.argsort(predictions)[-3:][::-1]

    st.subheader("Other Possible Predictions")

    for index in top_indices:
        st.write(
            f"{class_names[int(index)]}: "
            f"{predictions[index] * 100:.2f}%"
        )
