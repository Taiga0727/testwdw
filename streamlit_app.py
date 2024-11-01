import streamlit as st
from PIL import Image
import io

# Sidebar - Configurations
st.sidebar.image("https://your_logo_url.com/logo.png", width=120)  # Add logo here
st.sidebar.title("Config")
st.sidebar.write("You can lower temperature to make it more deterministic.")

# Model Selection Dropdowns
classify_model = st.sidebar.selectbox("Classify Model", ["SurgiCare-V1-large-turbo", "Other Model"])
llm_model = st.sidebar.selectbox("LLM Model", ["typhoon-v1.5x-70b-instruct", "Other Model"])

# Additional Configuration Sliders
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=512, value=256)
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.6)
top_p = st.sidebar.slider("Top P", 0.0, 1.0, 0.95)
st.sidebar.button("Save Config")

# Main Interface
st.title("Welcome to SurgiCare!")
st.subheader("AI Application for supporting post-surgery patient recovery.")

# Columns for Image Input
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Take a Picture")
    camera_input = st.camera_input("Camera input")

with col2:
    st.markdown("### Upload or Select a Sample Photo")
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])
    sample_image = st.selectbox("Or use a sample image", ["-- Select --", "Sample 1", "Sample 2"])
    use_sample = st.checkbox("Switch to use sample images")

# Process Image Button
if st.button("Process Image"):
    image = None

    if camera_input:
        image = Image.open(io.BytesIO(camera_input.getvalue()))
    elif uploaded_file:
        image = Image.open(uploaded_file)
    elif use_sample and sample_image != "-- Select --":
        # Load a sample image based on selection
        image = Image.open("path_to_sample_image.jpg")  # Replace with actual path to sample

    if image:
        st.image(image, caption="Processed Image", use_column_width=True)
        # Add model processing here if needed
        # result = model.process(image) 
        # st.write(result)  # Display result
    else:
        st.warning("Please provide an image to process.")

# Diagnose History
st.subheader("Full Diagnose History")
st.text_input("Enter your question here")
