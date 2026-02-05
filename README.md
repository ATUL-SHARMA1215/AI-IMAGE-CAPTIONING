# AI Image Captioning using BLIP, PyTorch & Streamlit

This project implements an image captioning web application using the **BLIP (Bootstrapping Language-Image Pretraining)** model from HuggingFace Transformers. The app generates captions for uploaded images and provides audio output and downloadable results through a Streamlit interface.

---

## 🔧 Tech Stack

- Python
- PyTorch
- HuggingFace Transformers (BLIP)
- Streamlit
- gTTS
- Pillow

---

## 🧠 Model Used

- Model: `Salesforce/blip-image-captioning-base`
- Pretrained vision-language transformer for image-to-text generation

---

## ⚙️ Features

- Upload JPG/PNG images and generate captions
- Convert caption to speech (MP3)
- Download caption as TXT / MP3 / ZIP
- Clean Streamlit UI with theme and speech controls
- Modular Python code separating inference and UI logic

---

## 🗂️ Project Structure

AI-IMAGE-CAPTIONING/ ├── app.py              # Streamlit user interface ├── utils.py            # Caption generation and audio logic ├── requirements.txt └── README.md

---

## ▶️ How to Run Locally

```bash
git clone https://github.com/ATUL-SHARMA1215/AI-IMAGE-CAPTIONING
cd AI-IMAGE-CAPTIONING
pip install -r requirements.txt
streamlit run app.py

---

🔍 How It Works

1. Image is uploaded through the Streamlit interface
2. Image is preprocessed using Pillow
3. BLIP model performs caption generation using PyTorch inference
4. Caption is converted to speech using gTTS
5. Results are available for download in multiple formats

---


🧪 Testing & Debugging Performed

1. Tested with multiple image formats and sizes
2. Debugged tensor conversion and preprocessing issues
3. Validated caption outputs on diverse real-world images
4. Separated inference logic from UI for easier debugging and testing

---

📌 Example

Input: Image of a dog running in a field
Output Caption: "A dog running through a grassy field."

--- 

🎯 Learning Outcomes

1. Working with vision-language transformer models
2. Handling image preprocessing for deep learning inference
3. Structuring Python code for modularity and testing
4. Building interactive ML applications with Streamlit
5.Debugging model inference and preprocessing logic