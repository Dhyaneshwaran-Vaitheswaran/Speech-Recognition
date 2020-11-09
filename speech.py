# Import speech recognition, time module and wb
import speech_recognition as sr
from time import ctime
import webbrowser as wb


# Creating a recognizer
r = sr.Recognizer()

# Listening audio (convert speech to text)
def record_audio(ask = False):
    if ask:
        print(ask)

    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''

        # Conditions
        try:
            voice_data = r.recognize_google(audio)

        except sr.UnknownValueError:
            print('Sorry I did not get that.')

        except sr.RequestError:
            print('Please connect to the internet.')
        
        return voice_data

# Conditions

def respond(voice_data):

    if 'what is your name' in voice_data:
        print('My name is Alexa')
    if 'what is the time' in voice_data:
        print('Time: ',ctime())
    if 'search' in voice_data:
        search = record_audio('What do you want to search for ?')
        url = 'https://google.com/search?q=' + search
        wb.get().open_new_tab(url)
        print('Here is what I found for ' + search)
    

# Voice Data
print('How can I help you ?')
voice_data = record_audio()
print(voice_data)
respond(voice_data)