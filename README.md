<h1 align="center">🎤 AI Live Lecture Notes Maker</h1>

<p align="center">
  <em>An intelligent assistant that records classroom audio, transcribes it using OpenAI's Whisper, and summarizes it into clean, concise notes with HuggingFace's Transformers — all running locally without any paid APIs!</em>
</p>

<hr>

<h2>🚀 Features</h2>

<ul>
  <li>🎙️ <strong>Record live audio</strong> during lectures</li>
  <li>📝 <strong>Transcribe</strong> spoken content using Whisper</li>
  <li>🧠 <strong>Summarize</strong> transcripts using BART</li>
  <li>🔒 <strong>Private</strong>: Everything runs <strong>locally</strong> with no internet required</li>
</ul>

<hr>

<h2>⚙️ Installation</h2>

<h3>📌 Requirements</h3>

<ul>
  <li>Python 3.9+</li>
  <li>Git</li>
</ul>

<h3>📥 Setup</h3>

<pre>
git clone https://github.com/&lt;your-username&gt;/AI-Live-Lecture-Notes.git
cd AI-Live-Lecture-Notes
python -m venv venv
venv\Scripts\activate   # (Windows)
pip install -r requirements.txt
</pre>

<h3>🔧 FFmpeg Setup (One-Time)</h3>

<ol>
  <li>Download from: <a href="https://www.gyan.dev/ffmpeg/builds/">https://www.gyan.dev/ffmpeg/builds/</a></li>
  <li>Extract & copy <code>bin/</code> path (e.g., <code>C:\ffmpeg\bin</code>)</li>
  <li>Add to <strong>Environment Variables &gt; Path</strong></li>
  <li>Verify installation:
    <pre>ffmpeg -version</pre>
  </li>
</ol>

<hr>

<h2>▶️ Running the App</h2>

<pre>streamlit run live_notes.py</pre>

Visit: <a href="http://localhost:8501">http://localhost:8501</a>

<hr>

<h2>📦 Dependencies</h2>

<pre>
streamlit
sounddevice
scipy
openai-whisper
transformers
torch
ffmpeg-python
</pre>

Install all:
<pre>pip install -r requirements.txt</pre>

<hr>

<h2>🛡️ Local & Private</h2>

No data leaves your device. All processing (recording, transcription, summarization) is done entirely offline.

<hr>

<h2>📌 Roadmap</h2>

<ul>
  <li>🔴 Real-time transcription support</li>
  <li>🌍 Multilingual transcription & translation</li>
  <li>📄 Export summarized notes to PDF</li>
  <li>☁️ Deploy to Streamlit Cloud or HuggingFace Spaces</li>
</ul>

<hr>

<h2 align="center">✨ Made with ❤️ by Saurabh Upadhyay</h2>
