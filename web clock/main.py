from pydub import AudioSegment
import speech_recognition as sr

def mp3_to_wav(mp3_file_path, wav_file_path):
    audio = AudioSegment.from_mp3(mp3_file_path)
    audio.export(wav_file_path, format="wav")

def transcribe_audio(wav_file_path, language="hi-IN"):
    recognizer = sr.Recognizer()
    audio_file = sr.AudioFile(wav_file_path)
    
    with audio_file as source:
        audio_data = recognizer.record(source)
    
    try:
        text = recognizer.recognize_google(audio_data, language=language)
        return text
    except sr.UnknownValueError:
        return "Could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

# Specify the paths
mp3_file_path = "path/to/your/audio.mp3"
wav_file_path = "path/to/your/audio.wav"

# Convert MP3 to WAV
mp3_to_wav(mp3_file_path, wav_file_path)

# Transcribe the WAV audio to text in Hindi
transcribed_text = transcribe_audio(wav_file_path, language="hi-IN")

print("Transcribed Text:", transcribed_text)
