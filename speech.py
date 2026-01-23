import io
import speech_recognition as sr
from faster_whisper import WhisperModel

def transcribe_once():
    # 1. Initialize the AI Model
    print("--- System: Loading AI Model... ---")
    # 'tiny' is the fastest and lowest power usage for your MacBook Air
    model = WhisperModel("tiny", device="cpu", compute_type="int8")

    recognizer = sr.Recognizer()
    # How long to wait for silence before deciding the sentence is over
    recognizer.pause_threshold = 1.0 

    try:
        with sr.Microphone() as source:
            print("Status: Calibrating mic for background noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            
            # STATUS: Active
            print("Status: Active (Listening... speak now)")
            audio = recognizer.listen(source)

        # STATUS: Not Active
        print("Status: Not Active (Processing...)")
        
        # Convert audio data for the AI
        wav_data = io.BytesIO(audio.get_wav_data())
        
        # Run the transcription
        segments, _ = model.transcribe(wav_data, beam_size=1)
        text = "".join([s.text for s in segments]).strip()

        if text:
            print(f"\nResult: {text}")
        else:
            print("\nResult: No speech was detected.")
        return text

    except Exception as e:
        print(f"\nStatus: Error - {e}")
    
if __name__ == "__main__":
    transcribe_once()
    print("--- System: Finished and Closed ---")