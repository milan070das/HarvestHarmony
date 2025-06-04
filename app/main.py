import os
import base64
import json
from PIL import Image

import numpy as np
import tensorflow as tf
import streamlit as st
import google.generativeai as genai
import subprocess

os.environ["GEMINI_API_KEY"] = "AIzaSyA0jX1JDZD7Tkhgm4crgO08bAjG9KFBUYc"

# Configure the API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create a model and generate content
model1 = genai.GenerativeModel('gemini-2.0-flash')

def ai_chatbot():
    subprocess.Popen(["streamlit", "run", "chatbot.py"])

working_dir = os.path.dirname(os.path.abspath(__file__))
model_path = f"{working_dir}/trained_model/plant_disease_prediction_model.h5"
# Load the pre-trained model
model = tf.keras.models.load_model(model_path)
#model = tf.keras.models.load_model('model.h5', custom_objects={'CustomLayer': CustomLayer})

# loading the class names
class_indices = json.load(open(f"{working_dir}/class_indices.json"))

# Function to Load and Preprocess the Image using Pillow
def load_and_preprocess_image(image_path, target_size=(224, 224)):
    # Load the image
    img = Image.open(image_path)
    # Resize the image
    img = img.resize(target_size)
    # Convert the image to a numpy array
    img_array = np.array(img)
    # Add batch dimension
    img_array = np.expand_dims(img_array, axis=0)
    # Scale the image values to [0, 1]
    img_array = img_array.astype('float32') / 255.
    return img_array


# Function to Predict the Class of an Image
def predict_image_class(model, image_path, class_indices):
    preprocessed_img = load_and_preprocess_image(image_path)
    predictions = model.predict(preprocessed_img)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    predicted_class_name = class_indices[str(predicted_class_index)]
    return predicted_class_name


# Streamlit App
def get_img_as_base64(file):
    with open(file,"rb") as f:
        data=f.read()
    return base64.b64encode(data).decode()

img1=get_img_as_base64("bg.jpg")

page_bg_img=f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image:url("data:image/png;base64,{img1}");
background-size: 100% 100%; /* Sets the background image width and height */
background-repeat: no-repeat; /* Prevents the image from repeating */
background-position: center; /* Centers the image */
}}

[data-testid="stHeader"] {{
background:rgba(0,0,0,0);
}}
</style>
"""
st.markdown(page_bg_img,unsafe_allow_html=True)
st.title('HarvestHarmony 🌼')

uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    col1, col2 = st.columns(2)
    s=''

    with col1:
        resized_img = image.resize((150, 150))
        st.image(resized_img)

    with col2:
        if st.button('Classify'):
            # Preprocess the uploaded image and predict the class
            prediction = predict_image_class(model, uploaded_image, class_indices)
            s=str(prediction)
            st.success(f'Prediction: {str(prediction)}')
    if  'healthy' not in s:
                st.title('Possible cure and solutions:')
                #st.write(s)
                p='give me the points to cure '+s
                response=model1.generate_content(p)
                st.write(response.text)
if st.button("Emily👩: Your plant's AI assistant"):
    ai_chatbot()
    st.success("Emily is coming to your aid!")
    st.markdown(
        f"""
        <script>
        window.open("http://localhost:8502", "_blank");
        </script>
        """,
        unsafe_allow_html=True
    )
