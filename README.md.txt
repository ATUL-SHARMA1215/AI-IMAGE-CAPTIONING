# 🖼️ AI Image Captioning App

A web app built with Streamlit that generates captions for uploaded images using Hugging Face's BLIP model. It can also read the caption aloud using Google Text-to-Speech (gTTS) and offers downloadable MP3 and TXT files.

## 🚀 Features
- Generate image captions with BLIP
- Convert caption to speech (MP3)
- Download caption as `.txt` or `.zip`
- Dark/light theme toggle
- Adjustable speech rate

## 🔧 Installation

1. Clone the repo:
https://github.com/ATUL-SHARMA1215/AI-IMAGE-CAPTIONING/edit/main/README.md.txt#L17C23


2. pip install -r requirements.txt

3. python -m streamlit run app.py OR streamlit run app.py(if path is set)

# 🖼️ AI Image Captioning with Audio


This Streamlit app combines **computer vision** and **natural language processing** to generate intelligent captions for uploaded images using the BLIP transformer model. It also supports **text-to-speech audio output** and downloadable results!

## 🚀 Features

- Upload JPG, JPEG, or PNG images
- Auto-generate image captions using a pre-trained transformer model
- Hear captions via Google Text-to-Speech (gTTS)
- Download captions as `.txt` or `.mp3`
- Bundle everything into a downloadable `.zip`
- Toggle dark/light themes and customize speech rate
- One-click deployment on [Streamlit Cloud](https://streamlit.io/cloud)

## 🧠 Model Info

This app uses [Salesforce's BLIP (Bootstrapped Language-Image Pretraining)](https://huggingface.co/Salesforce/blip-image-captioning-base) via Hugging Face Transformers, which internally handles:
- Image feature extraction (like ResNet/Vision Transformer)
- Caption generation using a transformer decoder

## ⚙️ Requirements

Install the dependencies via:

```bash
pip install -r requirements.txt