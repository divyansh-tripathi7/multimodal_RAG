## Multimodal RAG Voice Assistant

This project is a **Flask-based API** that integrates multimodal AI models for image-to-text, speech-to-text, and text-to-speech functionalities. It utilizes **Llava 1.5 7B** for vision-language tasks, **Whisper** for speech recognition, and **gTTS** for text-to-speech conversion.

### Features
- 🖼️ **Image-to-Text**: Convert images to text descriptions using Llava 1.5 7B.
- 🎙️ **Speech-to-Text**: Transcribe audio files to text using OpenAI's Whisper model.
- 🔊 **Text-to-Speech**: Convert text into spoken audio using Google Text-to-Speech (gTTS).

## Installation
### Prerequisites
Ensure you have Python installed (>=3.8) and set up a virtual environment.

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Usage
### Start the Flask Server
```bash
python app.py
```

### API Endpoints
#### 1️⃣ Image-to-Text
**Endpoint:** `/image-to-text`
- **Method:** `POST`
- **Body:** Multipart form with an image file.
- **Response:**
  ```json
  { "text": "Generated description of the image" }
  ```

#### 2️⃣ Speech-to-Text
**Endpoint:** `/speech-to-text`
- **Method:** `POST`
- **Body:** Multipart form with an audio file.
- **Response:**
  ```json
  { "text": "Transcribed speech" }
  ```

#### 3️⃣ Text-to-Speech
**Endpoint:** `/text-to-speech`
- **Method:** `POST`
- **Body:** JSON with a "text" field.
- **Response:**
  ```json
  { "message": "Speech generated", "audio_file": "output.mp3" }
  ```

## Deployment
To deploy the app using **Docker**, run:
```bash
docker build -t multimodal-rag .
docker run -p 5000:5000 multimodal-rag
```

## Contributing
Feel free to open issues and pull requests if you'd like to contribute!

## License
MIT License © 2024

