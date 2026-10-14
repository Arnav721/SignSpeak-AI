# SignSpeak AI — Indian Sign Language Alphabet Recognition

## Overview
SignSpeak AI is a beginner-friendly deep-learning project that recognizes Indian Sign Language (ISL) alphabet signs from uploaded images.

The application uses a Convolutional Neural Network (CNN) built with TensorFlow and provides predictions through a Streamlit interface.

## Features
- Upload an image of a hand sign.
- Predict the corresponding alphabet.
- Display the model's estimated confidence.
- Show the top three possible predictions.

## Technologies Used
- Python
- TensorFlow / Keras
- Streamlit
- NumPy
- Pillow

## Project Structure
- `app.py` — Streamlit application
- `train_model.py` — CNN training script
- `requirements.txt` — Python dependencies
- `models/isl_model.keras` — trained model
- `models/class_names.json` — class labels
- `dataset/` — local dataset, excluded from Git

## Run Locally

1. Clone this repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Start the application:

   ```bash
   python -m streamlit run app.py
   ```

## Limitations
This project recognizes alphabet signs from images. It does not translate continuous signing or full sentences. Prediction accuracy can vary with image quality, lighting, hand position, and differences between training images and real-world images.

## Future Improvements
- Test performance on unseen images.
- Improve recognition of signs captured in different environments.
- Deploy the application online.

## Disclaimer
This is an educational project and is not a substitute for a complete sign-language translation system.