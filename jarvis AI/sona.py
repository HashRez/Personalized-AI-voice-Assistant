# import speech_recognition as sr
# import pyttsx3
# import pywhatkit
# import datetime

# listener=sr.Recognizer()
# engine = pyttsx3.init()
# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[1].id)
# def talk(text):
#     engine.say(text)
#     engine.runAndWait()
# def take_command():
#     try:
#         with sr.Microphone() as source:
#             voice=listener.listen(source)
#             command=listener.recognize_google(voice)
#             command=command.lower()
#             if 'jarvis' in command:
#                 command=command.replace("jarvis","")
#                 print(command)
#     except:
#         pass

#     return command

# def run_alexa():
#     command=take_command()
#     if 'play' in command:
#         song=command.replace('play','')
#         talk('playing'+song)
#         pywhatkit.playonyt(song)
#     elif 'time' in command:
#         time =datetime.datetime.now().strftime('%I:%M %p')
#         print(time)
#         talk('current time is '+ time)
# run_alexa()

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print("Command:", command)
            if 'jarvis' in command:
                command = command.replace("jarvis", "")
    except sr.UnknownValueError:
        print("Could not understand the audio")
        return ""
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        return ""
    return command


def run_alexa():
    while True:
        command = take_command()
        if 'play' in command:
            song = command.replace('play', '')
            talk('Playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print("Current time:", time)
            talk('Current time is ' + time)
        elif 'search' in command:
            query = command.replace('search', '')
            try:
                result = wikipedia.summary(query, sentences=1)
                print("Wikipedia Summary:", result)
                talk("According to Wikipedia, " + result)
            except wikipedia.exceptions.DisambiguationError as e:
                print("Disambiguation Error:", e.options)
                talk("There are multiple options. Can you please be more specific?")
            except wikipedia.exceptions.PageError as e:
                print("Page Error:", e)
                talk("Sorry, I couldn't find any information on that.")
        elif 'joke' in command:
            joke = pyjokes.get_joke()
            print("Joke:", joke)
            talk(joke)
        elif 'stop' in command:
            talk('Goodbye!')
            break
        else:
            talk("Sorry, I didn't understand that command.")


run_alexa()


# from flask import Flask, request, jsonify
# import speech_recognition as sr
# import pyttsx3
# import pywhatkit
# import datetime
# import wikipedia
# import openai

# app = Flask(__name__)

# # Initialize the ChatGPT API client
# openai.api_key = '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'

# listener = sr.Recognizer()
# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

# def talk(text):
#     engine.say(text)
#     engine.runAndWait()

# def take_command():
#     try:
#         with sr.Microphone() as source:
#             print("Listening...")
#             voice = listener.listen(source)
#             command = listener.recognize_google(voice)
#             command = command.lower()
#             print("Command:", command)
#             if 'jarvis' in command:
#                 command = command.replace("jarvis", "")
#     except sr.UnknownValueError:
#         print("Could not understand the audio")
#         return ""
#     except sr.RequestError as e:
#         print("Could not request results; {0}".format(e))
#         return ""
#     return command

# @app.route('/process-command', methods=['POST'])
# def process_command():
#     data = request.json
#     command = data.get('command')

#     if 'play' in command:
#         song = command.replace('play', '')
#         talk('Playing ' + song)
#         pywhatkit.playonyt(song)
#     elif 'time' in command:
#         time = datetime.datetime.now().strftime('%I:%M %p')
#         print("Current time:", time)
#         talk('Current time is ' + time)
#     elif 'search' in command:
#         query = command.replace('search', '')
#         try:
#             result = wikipedia.summary(query, sentences=1)
#             print("Wikipedia Summary:", result)
#             talk("According to Wikipedia, " + result)
#         except wikipedia.exceptions.DisambiguationError as e:
#             print("Disambiguation Error:", e.options)
#             talk("There are multiple options. Can you please be more specific?")
#         except wikipedia.exceptions.PageError as e:
#             print("Page Error:", e)
#             talk("Sorry, I couldn't find any information on that.")
#     else:
#         # Send user query to ChatGPT API
#         response = openai.Completion.create(
#             engine="text-davinci-002",
#             prompt=command,
#             max_tokens=50
#         )
#         chatgpt_response = response.choices[0].text.strip()

#         # Speak the ChatGPT response
#         talk(chatgpt_response)

#     return jsonify({'response': chatgpt_response})

# if __name__ == '__main__':
#     app.run(debug=True)