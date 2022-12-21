import speech_recognition as sr
import os
import openai

r = sr.Recognizer()


openai.api_key = os.getenv("OPENAI_API_KEY")

with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize what you said")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=f"Translate this into  1. Telugu:\n\n{text}\n\n1. ",
  temperature=0.3,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

