import speech_recognition as sr #use SpeechRecogniton in cmd if this doesnt work
r=sr.Recognizer()
a=sr.AudioFile('male.wav')#name of audio file preferably wav
with a as source:
    audio=r.record(source)
text=r.recognize_google(audio)#uses google audio conv.
file1=open(r"C:\Python37\Projects\Speech To Text\1.txt","w")#path to store newly created text file
file1.writelines(text)
file1.close()
