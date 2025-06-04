# 🌾 HarvestHarmony

HarvestHarmony is an AI-powered plant disease detection and assistant app built using **TensorFlow**, **Streamlit**, and **Google Gemini API**. It allows users to upload images of plant leaves, predicts diseases using a deep learning model, and offers intelligent suggestions for cures. It also includes a virtual assistant named **Emily** to answer plant-related queries.

---

## ✨ Features

- 🧠 **Deep Learning-based Plant Disease Detection**
- 🌱 **Upload Images to Classify Health of Plant Leaves**
- 💡 **AI-generated Cure and Treatment Suggestions using Gemini API**
- 🤖 **"Emily" – Chatbot for Plant Assistance**
- 🎨 **Custom Background UI with Streamlit Styling**
- 🔄 **Two-column Layout for Better UX**
- 🧾 **Easy-to-use File Upload Interface**

---

## 🚀 Tech Stack

**Frontend:**  
- Streamlit  
- HTML/CSS Styling in Python

**Backend & AI:**  
- TensorFlow (Keras)  
- Google Generative AI (Gemini)  
- PIL (Pillow)  
- NumPy  
- JSON  
- Python `subprocess` (for chatbot launch)

---

## 📁 Folder Structure

<pre> 📦 HarvestHarmony/ ├── 📄 main_app.py # Main Streamlit app for disease detection ├── 📄 chatbot.py # Gemini-powered Streamlit chatbot (Emily) ├── 📄 class_indices.json # Class index to label mapping for model predictions ├── 🖼️ bg.jpg # Background image for Streamlit app ├── 📁 trained_model/ │ └── 📄 plant_disease_prediction_model.h5 # Pre-trained Keras model ├── 📄 requirements.txt # Python dependencies </pre>
