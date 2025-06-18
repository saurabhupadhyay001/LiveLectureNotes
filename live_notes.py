import streamlit as st
import sounddevice as sd
from scipy.io.wavfile import write
import tempfile
import whisper
from transformers import pipeline
import os

# Load Whisper model (base or tiny to keep fast on CPU)
@st.cache_resource
def load_whisper_model():
    return whisper.load_model("base")

# Load summarizer
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

model = load_whisper_model()
summarizer = load_summarizer()

# App title
st.title("🎤 AI Live Lecture Notes Maker")
st.markdown("Record lecture audio, transcribe it, and get clean AI-generated notes.")

# Recording duration slider
duration = st.slider("🎧 Recording Duration (seconds)", 5, 180, 30)

# Record button
if st.button("Start Recording"):
    st.info("🔴 Recording... Please speak clearly.")
    fs = 44100  # Sample rate
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()

    # Save to temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
        write(temp_audio.name, fs, recording)
        audio_path = temp_audio.name

    st.success("✅ Recording complete.")

    # Transcribe
    st.subheader("📝 Transcription:")
    result = model.transcribe(audio_path)
    st.text_area("Raw Transcript", result["text"], height=150)

    # Summarize
    st.subheader("🧠 Summarized Notes:")
    summary = summarizer(result["text"], max_length=150, min_length=30, do_sample=False)
    st.text_area("AI Summary", summary[0]['summary_text'], height=150)

    # Delete temp file safely
    try:
        os.remove(audio_path)
    except PermissionError:
        st.warning("⚠️ Couldn't delete temporary audio file. Please close any apps using it.")
