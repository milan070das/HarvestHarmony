import streamlit as st
import google.generativeai as genai
import os
import base64

# Set the GEMINI API key
os.environ["GEMINI_API_KEY"] = "AIzaSyBH0SjlQNUOJ4vqAqf4KvqvRlBCSzPtOAU"

# Configure the API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Create a model instance
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to get image as base64
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
st.markdown(page_bg_img, unsafe_allow_html=True)

# Page title
st.title("Hello, it's Emily👩, your plant's AI assistant. How can I help you today?")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "chat_input" not in st.session_state:
    st.session_state.chat_input = ""

# Define Emily's persona as a constant
EMILY_PERSONA = (
    "You are Emily, an AI assistant specialized in helping with plant diseases. "
    "You provide friendly, knowledgeable, and practical advice for curing and preventing plant issues. "
    "Speak as if you are Emily, the user's trusted plant care assistant."
)

# Ensure persona context is preserved
def generate_response(user_input):
    # Combine persona and user input for context
    full_prompt = f"{EMILY_PERSONA}\nUser: {user_input}\nEmily:"
    response = model.generate_content(full_prompt)
    return response.text.strip()

# Handle chat submission
def submit_chat():
    # Save user input
    st.session_state.messages.append({"role": "user", "text": st.session_state.chat_input})

    # Generate response with Emily's persona
    response_text = generate_response(st.session_state.chat_input)

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "text": response_text})

    # Clear input box
    st.session_state.chat_input = ""

# Chat input box
st.text_input('Type here to chat...', key="chat_input", on_change=submit_chat)

# Display chat messages
for message in st.session_state.messages:
    if message["role"] == "user":
        st.write(f"**You:** {message['text']}")
    else:
        st.write(f"**Emily:** {message['text']}")