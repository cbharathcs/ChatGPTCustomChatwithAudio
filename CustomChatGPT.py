from dbm import dumb
from http.client import responses
from urllib import response
from llama_index import GPTSimpleVectorIndex, Document, SimpleDirectoryReader, LLMPredictor, GPTSimpleKeywordTableIndex

from langchain import OpenAI
import os

import pyttsx3
import speech_recognition


recognizer = speech_recognition.Recognizer()

os.environ['OPENAI_API_KEY'] = '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'

#print('insideFile')

documents =  SimpleDirectoryReader("E:/ChatGpt/docs/src").load_data()

textlist = ['Supermarket.txt']

documents = [Document(t) for t in textlist]

#index = GPTSimpleVectorIndex.from_documents(documents)

#print(index)

#index.save_to_disk('E:/ChatGpt/docs/out/SuperMarketJson.json')

index = GPTSimpleVectorIndex.load_from_disk('E:/ChatGpt/docs/out/SuperMarketJson.json')

#respose = index.query("what should we kept in top shelves?")

#print("what should we kept in top shelves?  >>> ",respose)

#respose = index.query("what should we kept in Bottom shelves?")

#print("what should we kept in Bottom shelves?  >>>",respose)

#respose = index.query("where should I keep snacks?")

#print("where should I keep snacks?  >>> ",respose)


#respose = index.query("where to store the milk?")

#print("where to store the milk?  >>>> ",respose)


try :
    with speech_recognition.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration= 1.2)
        audio = recognizer.listen(mic)

        querystr = recognizer.recognize_google(audio, language='en-US')

        respose = index.query(querystr)

        print(querystr,">>>" ,respose)

        
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        engine.say(respose)
        engine.runAndWait()
        engine.stop()



        
except Exception as e: 
    print(e)



