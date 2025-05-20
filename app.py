import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image, UnidentifiedImageError
from gtts import gTTS
import tempfile
import os
import zipfile

# Streamlit app configuration
st.set_page_config(page_title="🖼️ AI IMAGE CAPTIONING", layout="centered")

# Sidebar settings
with st.sidebar:
    st.title("⚙️ Settings")
    theme = st.radio("Choose Theme", ["Light", "Dark"], horizontal=True)
    download_audio = st.checkbox("⬇️ Enable MP3 Download", value=True)
    enable_download_txt = st.checkbox("📄 Enable TXT Download", value=True)
    auto_caption = st.checkbox("⚡ Auto-caption on Upload", value=True)  # Enabling Auto-caption by default
    adjust_speech_rate = st.slider("Speech Rate", 50, 200, 100, step=10)  # Speech rate slider

# Optional dark theme styling
if theme == "Dark":
    st.markdown("""
        <style>
            body, .stApp {
                background-color: #0e1117;
                color: white;
            }
            .stTextInput > div > div > input {
                background-color: #262730;
                color: white;
            }
            .stButton > button {
                background-color: #6200EE;
                color: white;
            }
        </style>
    """, unsafe_allow_html=True)

# Title and instructions
st.title("📸 AI IMAGE CAPTIONING")
st.markdown("Upload an image and let our AI describe. You can even hear it!")

# Load and cache the BLIP model
@st.cache_resource(show_spinner="🔄 Loading BLIP model...")
def load_model():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = load_model()

# Text-to-speech using gTTS (Google TTS)
def text_to_speech(text, save_mp3=True, rate=100):
    try:
        # Google TTS (using custom speech rate)
        tts = gTTS(text, lang="en", slow=False)
        tts.speed = rate / 100  # Adjust speech rate

        # Temporary save to MP3
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
            tts.save(f.name)
            return f.name
    except Exception as e:
        st.error(f"⚠️ TTS Error: {e}")
        return None

# Caption generation function
def generate_caption(image: Image.Image):
    try:
        inputs = processor(image, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=50)
        caption = processor.decode(outputs[0], skip_special_tokens=True)
        return caption
    except Exception as e:
        return f"❌ Error generating caption: {str(e)}"

# Caption handling function
def handle_caption(image):
    caption = generate_caption(image)
    if caption:
        st.success("📝 Caption Generated:")
        st.markdown(f"#### 💡 *{caption}*")

        # Text-to-Speech (automatically read aloud)
        audio_path = text_to_speech(
            caption,
            save_mp3=download_audio,
            rate=adjust_speech_rate
        )

        # MP3 download
        if audio_path and download_audio:
            st.audio(audio_path, format="audio/mp3", autoplay=True)
            with open(audio_path, "rb") as f:
                st.download_button("⬇️ Download MP3", f, file_name="caption_audio.mp3", mime="audio/mpeg")
            os.remove(audio_path)

        # TXT download
        if enable_download_txt:
            st.download_button("📄 Download Caption as .txt", caption, file_name="caption.txt")

# File uploader with image preview
uploaded_image = st.file_uploader("📤 Upload an image", type=["jpg", "jpeg", "png"])

# Check if image is uploaded and process
if uploaded_image:
    try:
        image = Image.open(uploaded_image).convert("RGB")

        # Resize image to maintain aspect ratio for better quality processing
        image.thumbnail((800, 800))

        st.image(image, caption="✅ Uploaded Image", use_container_width=True)

        # Auto-captioning: Automatically generate caption when the image is uploaded
        if auto_caption:
            with st.spinner("🧠 AI is analyzing your image..."):
                handle_caption(image)
        else:
            if st.button("✨ Generate Caption"):
                with st.spinner("🧠 AI is analyzing your image..."):
                    handle_caption(image)

    except UnidentifiedImageError:
        st.error("🛑 Uploaded file is not a valid image.")
    except Exception as e:
        st.error(f"❌ Error: {e}")
else:
    st.info("📎 Upload an image to get started.")

# Footer with download zip button
if uploaded_image and (download_audio or enable_download_txt):
    def create_zip(caption, audio_path=None):
        zip_filename = "image_caption_files.zip"
        with zipfile.ZipFile(zip_filename, "w") as zipf:
            # Save image
            image_filename = "uploaded_image.jpg"
            uploaded_image.seek(0)
            zipf.writestr(image_filename, uploaded_image.read())

            # Add caption text
            zipf.writestr("caption.txt", caption)

            # Add audio if required
            if audio_path:
                with open(audio_path, "rb") as f:
                    zipf.writestr("caption_audio.mp3", f.read())

        return zip_filename

    if st.button("⬇️ Download All Files as Zip"):
        with st.spinner("🔄 Creating zip..."):
            audio_path = text_to_speech(caption, save_mp3=True, rate=adjust_speech_rate) if download_audio else None
            zip_file = create_zip(caption, audio_path)
            with open(zip_file, "rb") as f:
                st.download_button("⬇️ Download ZIP", f, file_name="image_caption_files.zip", mime="application/zip")
            os.remove(zip_file)

# Footer
st.markdown("""
    <hr>
    <center>
        Built with ❤️ using Streamlit and 🤗 Hugging Face Transformers
    </center>
""", unsafe_allow_html=True)
