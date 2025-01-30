import pyttsx3

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

for index, voice in enumerate(voices):
    print(f"Voice {index}: {voice.name} ({voice.id}) - Gender: {'Female' if 'female' in voice.name.lower() else 'Male'}")

engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

if __name__ == "__main__":
    speak("This is a test to check the female voice.")
