import speech_recognition as sr
from mediaAi import nlp
class VoiceToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recognize_voice(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            print("Recognizing...")
            text = self.recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the audio.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return ""

# Example usage:
if __name__ == "__main__":
    voice_to_text = VoiceToText()
    command = voice_to_text.recognize_voice()
    #print(nlp.predict(command))
    print("You said:", command)
