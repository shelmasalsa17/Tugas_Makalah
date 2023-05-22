import playsound 
from gtts import gTTS 
import speech_recognition 
import os
 

def rekam():
    rekam = speech_recognition.Recognizer()
    microphone = speech_recognition.Microphone()
    result = ""
    rekam.pause_treshold = 1
    with microphone as source: 
        rekaman = rekam.listen(source)
    try: 
        result = rekam.recognize_google(rekaman, language = 'id')
        return result
    except rekam.UnknownValueError: 
        result = "Tidak valid"
        return result
    except Exception as e:
        result = e 
        return result
  
    
def convert_suara(text): 
    output_suara = gTTS(text=text, lang = 'id', slow = False)
    output_suara.save("answer.mp3")
    playsound.playsound("answer.mp3", True)
    os.remove("answer.mp3")
    


#print("Hallo ini test case untuk proses convert suara")
#input = "Hallo Selamat Pagi"
#convert_suara(input)