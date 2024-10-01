from flask import Flask, render_template, redirect, url_for, flash, request, send_file
from flask_bootstrap import Bootstrap5
import os
from datetime import datetime as dt
from pypdf import PdfReader
import boto3
from io import BytesIO

YEAR = dt.now().year

# Initialize Flask and AWS Polly
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASH_KEY')
Bootstrap5(app)

polly = boto3.client('polly', region_name='us-east-1')

# Directory to store uploaded files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('start.html', year=YEAR)

@app.route('/upload', methods=['POST'])
def upload_pdf(): 

    file = request.files['pdf']
        
    if file and file.filename.endswith('.pdf'):
        # Save the uploaded PDF to the server
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Extract text from the PDF
        pdf_text = extract_text_from_pdf(file_path)

        # Split text into chunks of 3,000 characters or less
        chunks = split_text_into_chunks(pdf_text, 3000)

        # Convert each chunk of text to speech using AWS Polly and combine audio
        audio_stream = convert_chunks_to_speech(chunks)

        # Serve the generated audiobook
        return send_file(BytesIO(audio_stream), as_attachment=True, download_name='audiobook.mp3', mimetype='audio/mpeg')

    else:
        flash('Invalid input.')
        return redirect(url_for('index'))

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    reader = PdfReader(pdf_path)
    text = ''
    
    for page in reader.pages:
        text += page.extract_text() + '\n'
    
    return text

def split_text_into_chunks(text, max_length):
    """Split text into chunks of max_length characters."""
    return [text[i:i+max_length] for i in range(0, len(text), max_length)]

def convert_chunks_to_speech(chunks):
    """Convert text chunks to speech using AWS Polly and return combined audio."""
    audio_streams = []

    # Loop through each text chunk and get audio from Polly
    for chunk in chunks:
        response = polly.synthesize_speech(
            Text=chunk,
            OutputFormat='mp3',
            VoiceId='Joanna'  # You can change the voice here
        )
        audio_streams.append(response['AudioStream'].read())

    # Combine all audio streams into one
    combined_audio = b''.join(audio_streams)

    return combined_audio
    

if __name__ == '__main__':
    app.run(debug=True)