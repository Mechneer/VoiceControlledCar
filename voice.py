import speech_recognition as sr
import pyttsx3 as tts
import controller as cnt

def take():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recording...")
            voice = r.recognize_google(audio, language="tr")
        except Exception as e:
            print("Try again")
            return "None"
        return voice


if __name__ == "__main__":
    while True:
        query = take().lower()
        if 'başla' in query:
            print("okey")
            cnt.ins(1)
        elif 'geri' in query:
            print("okey")
            cnt.ins(2)
        elif 'dur' in query:
            cnt.ins(0)
            print("okey")
        elif 'yak' in query:
            cnt.ins(3)
            print("okey")
        elif 'çık' in query:
            break
