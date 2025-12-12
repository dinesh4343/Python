#code for text to speeech usiing pyttsx3
import pyttsx3
import argparse
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Text to Speech using pyttsx3")
    parser.add_argument("text", nargs="*", help="Text to speak")
    args = parser.parse_args()

    if args.text:
        speak_text(" ".join(args.text))
    else:
        print("Please provide text to speak.")