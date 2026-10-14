# 🤟 SignSpeak-AI — Indian Sign Language Alphabet Recognition

An AI/ML project that recognizes Indian Sign Language (ISL) alphabet signs from images using a Convolutional Neural Network (CNN).

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://signspeak-ai-nj9bi9qfgznqccbpzjxh92.streamlit.app/)

## 🚀 Live Demo

Try the application: [SignSpeak-AI on Streamlit](https://signspeak-ai-nj9bi9qfgznqccbpzjxh92.streamlit.app/)

Upload an image of a hand sign to see the predicted alphabet, the model's estimated confidence score, and its top three predictions.

## 📌 About the Project

SignSpeak-AI is a beginner-level AI/ML project exploring how deep learning and computer vision can be used to recognize hand signs.

The application uses a trained CNN model to classify an uploaded hand-sign image into one of the alphabet classes it has learned. A simple Streamlit interface makes it possible to interact with the model directly through a web browser.

## Project details

- Domain: Artificial Intelligence / Machine Learning
- Task: Image classification
- Sign language: Indian Sign Language (ISL)
- Model: Convolutional Neural Network (CNN)
- Input: JPG, JPEG, or PNG image
- Output: Predicted alphabet, confidence score, and top-three predictions
- Deployment: Streamlit Community Cloud

> Scope: This project recognizes individual alphabet signs from images. It does not translate continuous signing, complete words, or sentences.

## ✨ Features

- 🖼️ **Image Upload:** Upload a hand-sign image for prediction.
- 🔤 **Alphabet Recognition:** Predict the alphabet class most likely to match the image.
- 📊 **Confidence Score:** View the model's estimated probability for its top prediction.
- 🥇 **Top-Three Predictions:** Compare the three highest-scoring classes.
- 🌐 **Interactive Web App:** Use the application through a simple Streamlit interface.
- 🧠 **Saved Deep-Learning Model:** Load the trained model for predictions without retraining it each time.

## ⚙️ How It Works

The project follows a basic image-classification pipeline:

1. The user uploads an image through the Streamlit interface.
2. The image is converted to RGB and resized to **64 × 64 pixels**.
3. The preprocessed image is passed to the trained CNN.
4. The model produces scores for the supported alphabet classes.
5. The application displays the predicted class, confidence score, and top-three results.

```text
Hand-Sign Image
       ↓
 Streamlit Upload
       ↓
 Image Preprocessing
   (64 × 64, RGB)
       ↓
 Trained CNN Model
       ↓
 Class Predictions
       ↓
 Alphabet + Confidence
    + Top 3 Results
```

## 🧠 Model Overview

The project uses a Convolutional Neural Network (CNN), a deep-learning architecture commonly used for image recognition.

The model includes:

- Convolutional layers: Learn visual features from hand images.
- Max-pooling layers: Reduce the spatial dimensions of feature maps.
- Flatten layer: Converts extracted features into a one-dimensional representation.
- Dense layer: Learns combinations of the extracted features.
- Dropout: Helps reduce overfitting during training.
- Softmax output layer: Produces scores across the supported classes.

Training configuration

| Setting | Value |
|---|---|
| Framework | TensorFlow / Keras |
| Input size | 64 × 64 pixels |
| Color mode | RGB |
| Batch size | 32 |
| Optimizer | Adam |
| Loss function | Sparse categorical cross-entropy |
| Training epochs | 10 |

These settings describe the current training configuration; actual performance should be established through a separate evaluation on test images.

## 🛠️ Technologies Used

- Python — Main programming language
- TensorFlow and Keras — Building and training the CNN
- Streamlit — Web application interface
- NumPy — Numerical operations
- Pillow — Image processing
- Git and GitHub — Version control and project hosting

## 📂 Project Structure

```text
SignSpeak-AI/
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
├── .gitignore
├── .devcontainer/
│   └── devcontainer.json
└── models/
    ├── isl_model.keras
    └── class_names.json
```

**Important files**

- `app.py` — Loads the trained model, accepts image uploads, and displays predictions.
- `train_model.py` — Defines and trains the CNN using the training and validation images.
- `requirements.txt` — Lists the Python dependencies.
- `models/isl_model.keras` — Saved trained model.
- `models/class_names.json` — Class-label mapping used for predictions.
- `README.md` — Project documentation.

The dataset and virtual environment are kept locally and may not be included in the GitHub repository.

## 💻 Run the Project Locally

### Prerequisites

- Python installed on your computer
- Git installed
- The project dependencies listed in `requirements.txt`
- The trained model files in the `models/` directory

### 1. Clone the repository

```bash
git clone https://github.com/Arnav721/SignSpeak-AI.git
cd SignSpeak-AI
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the environment

**Windows PowerShell**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal, usually `http://localhost:8501`.

## 🧪 Testing the Application

To explore the model's predictions:

1. Open the application.
2. Upload an image of an alphabet sign.
3. Review the predicted class and confidence score.
4. Compare the top-three predictions.
5. Repeat with images from different classes and backgrounds.

Testing with images not used during training helps provide a more meaningful indication of how well the model generalizes.

No test-accuracy figure is reported here because a formal evaluation result has not been established in this README.

## ⚠️ Limitations

- The application recognizes individual images rather than continuous sign-language movements.
- It does not translate complete sentences or conversations.
- Prediction quality depends on the training data and the similarity of new images to that data.
- Lighting, backgrounds, camera angles, and hand positions may affect results.
- A high confidence score does not guarantee a correct prediction.
- The application is an educational prototype, not a complete sign-language translation system.

## 🔮 Future Improvements

Possible future improvements include:

- Evaluate the model using test accuracy and a confusion matrix.
- Improve generalization using data augmentation.
- Test the model on a wider variety of real-world images.
- Explore webcam-based alphabet recognition.
- Investigate video-based recognition of dynamic signs.
- Improve the interface and prediction explanations.

These are potential extensions, not claims about features already implemented.

## 📚 What I Learned

Through this project, I explored:

- The fundamentals of image classification and computer vision.
- Organizing labeled image datasets.
- Building and training a CNN with TensorFlow/Keras.
- Saving and loading a trained model.
- Connecting a machine-learning model to a Streamlit application.
- Deploying an AI/ML project online using GitHub and Streamlit Community Cloud.

## 👨‍💻 Author

Arnav Bhardwaj  
B.Tech — Artificial Intelligence and Machine Learning

- GitHub: [Arnav721](https://github.com/Arnav721)
- Live Project: [SignSpeak-AI](https://signspeak-ai-nj9bi9qfgznqccbpzjxh92.streamlit.app/)

## 📄 Dataset and Licensing

The dataset used for training and experimentation should be credited according to its original source and license. Check the dataset's redistribution terms before sharing its images.

No separate software license has been specified for this project yet. Add a suitable license file if you intend to define how others may reuse your code.
