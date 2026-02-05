# AI Image Captioning using BLIP, PyTorch & Streamlit

This project implements an AI-based Image Captioning application using the **BLIP (Bootstrapping Language Image Pretraining)** model from HuggingFace Transformers. The application generates natural language descriptions for input images and provides audio output and downloadable results via a Streamlit interface.

---

## 🔧 Tech Stack

- Python
- PyTorch
- HuggingFace Transformers (BLIP)
- Streamlit
- gTTS (Text-to-Speech)

---

## 🧠 Model Used

- **Model:** Salesforce BLIP Image Captioning Base
- Pretrained transformer model for vision-language tasks
- Performs image-to-text generation

---

## ⚙️ Features

- Upload image and generate caption
- Text-to-speech audio output of caption
- Download results as TXT / MP3
- Simple and interactive Streamlit UI
- Modular Python code for inference and UI separation

---
---

## 🗂️ Project Structure
AI-IMAGE-CAPTIONING/ │── app.py              # Streamlit user interface │── utils.py            # Caption generation and audio logic │── requirements.txt │── README.md

---
---

## ▶️ How to Run

```bash
git clone https://github.com/ATUL-SHARMA1215/AI-IMAGE-CAPTIONING
cd AI-IMAGE-CAPTIONING
pip install -r requirements.txt
streamlit run app.py

---
---

##How It Works ??
• Image is uploaded through Streamlit UI
• Image is preprocessed using Pillow
• BLIP model generates caption using PyTorch inference
• Caption is converted to speech using gTTS
• User can download results in multiple formats

---
---

##Testing & Debugging Performed
•Tested with multiple image formats and sizes
•Debugged tensor conversion and preprocessing issues
•Validated caption generation on diverse real-world images
•Separated inference logic from UI for easier debugging

---
---

##Example
Input: Image of a dog running in a field
Output Caption: "A dog running through a grassy field."


---
---

##Learning Outcomes
•Working with vision-language transformer models
•Handling image preprocessing for deep learning inference
•Structuring Python code for modularity and testing
•Building interactive ML applications with Streamlit
•Debugging model inference and preprocessing logic