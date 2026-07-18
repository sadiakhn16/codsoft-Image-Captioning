# AI Image Captioning System

## Project Description

The AI Image Captioning System is a deep learning application that automatically generates descriptive captions for uploaded images. It combines Computer Vision and Natural Language Processing (NLP) using a pre-trained Vision Transformer (ViT) as the image encoder and GPT-2 as the language decoder.

Users can upload an image through a Streamlit web interface, and the system analyzes the image to generate a meaningful natural language description.

---

## Features

- Upload JPG, JPEG, or PNG images
- Automatically generate captions for uploaded images
- Interactive Streamlit web interface
- Uses a pre-trained deep learning model
- Simple and user-friendly interface

---

## Technologies Used

- Python
- Streamlit
- PyTorch
- Hugging Face Transformers
- Pillow (PIL)

---

## AI Model Used

- VisionEncoderDecoderModel
- Vision Transformer (ViT)
- GPT-2 Language Model

---

## Project Structure

```
image_captioning/
│
├── app.py
├── model.py
├── requirements.txt
├── README.md
└── uploads/
```

---

## How to Run

### Step 1: Install the required libraries

```bash
pip install -r requirements.txt
```

### Step 2: Run the application

```bash
streamlit run app.py
```

### Step 3: Open the browser

The application will automatically open at:

```
http://localhost:8501
```

---

## Working

1. Upload an image using the file uploader.
2. The Vision Transformer extracts image features.
3. GPT-2 generates a descriptive caption.
4. The generated caption is displayed on the screen.

---

## Applications

- Image understanding
- Assistive technology for visually impaired users
- Automatic image description
- Social media caption generation
- Smart photo management

---

## Future Improvements

- Display multiple caption suggestions
- Add support for camera input
- Improve the user interface
- Deploy the application online
- Support multiple languages

---

## Developed By

**Your Name**

College Internship Project
