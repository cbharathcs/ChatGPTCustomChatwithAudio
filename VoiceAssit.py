
import pyttsx3
import speech_recognition

recognizer = speech_recognition.Recognizer()

try :
    with speech_recognition.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration= 1.2)
        audio = recognizer.listen(mic)

        querystr = recognizer.recognize_google(audio, language='en-US')
        print(querystr)

        respose = "find milk "

        print(querystr,">>>" ,respose)

        engine = pyttsx3.init()
        engine.say(respose)
        engine.runAndWait()
        engine.stop()



        
except Exception as e: 
    print(e)