from flask import Flask, request, jsonify
import torch
from transformers import BitsAndBytesConfig, pipeline
import whisper
from gtts import gTTS
import os

app = Flask(__name__)

# Load Llava 1.5 7B for image-to-text processing
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16
)
model_id = "llava-hf/llava-1.5-7b-hf"
image_pipe = pipeline("image-to-text", model=model_id, model_kwargs={"quantization_config": quantization_config})

# Load Whisper for speech-to-text processing
whisper_model = whisper.load_model("base")

@app.route("/image-to-text", methods=["POST"])
def image_to_text():
    if "image" not in request.files:
        return jsonify({"error": "No image file provided"}), 400
    
    image = request.files["image"]
    text_output = image_pipe(image)["generated_text"]
    return jsonify({"text": text_output})

@app.route("/speech-to-text", methods=["POST"])
def speech_to_text():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file provided"}), 400
    
    audio_file = request.files["audio"]
    audio_path = "temp_audio.wav"
    audio_file.save(audio_path)
    
    text_output = whisper_model.transcribe(audio_path)["text"]
    os.remove(audio_path)
    
    return jsonify({"text": text_output})

@app.route("/text-to-speech", methods=["POST"])
def text_to_speech():
    data = request.get_json()
    if "text" not in data:
        return jsonify({"error": "No text provided"}), 400
    
    tts = gTTS(data["text"])
    tts.save("output.mp3")
    
    return jsonify({"message": "Speech generated", "audio_file": "output.mp3"})

if __name__ == "__main__":
    app.run(debug=True)
