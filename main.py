from flask import Flask, render_template, request, jsonify
from gtts import gTTS
from pynput import keyboard
import wikipedia
import webbrowser
import os
from pynput.keyboard import Key,Controller
import random
app = Flask(__name__)
keyboard=Controller()

# code for get answwer

def getans(q):
    try:
        q= q.lower()
        if 'wikipedia' in q:
            try:
                q= q.replace('wikipedia','')
                answer= wikipedia.summary(q, sentences=2)
            except:
                answer= "failed to connect wikipedia"
        elif "open youtube" in q or "youtube kholo" in q:
            try:
                webbrowser.open('https://youtube.com')
                answer = "opening youtube"
            except:
                answer = "Sorry I unable to open youtube"
        elif "open google" in q or "google kholo" in q or "open chrome" in q or "chrome kholo" in q:
            try:
                webbrowser.open('https://google.com')
                answer = "opening google in chrome"
            except:
                answer = "Sorry I unable to open google"
        
        elif "type " in q:
            try:
                q= q.replace('type ','')
                keyboard.type(q)
                answer = "typing"
            except:
                answer = "Sorry unable to type"
        
        elif "shutdown computer" in q or "shutdown pc" in q or "shutdown laptop" in q or "off laptop" in q or "off pc" in q or "off computer" in q:
            try:
                os.system("shutdown /s /t 1")
                answer = "Ok bye"
            except:
                answer = "Sorry unable to shutdown"
        
        elif "restart computer" in q or "restart pc" in q or "restart laptop" in q:
            try:
                os.system("shutdown /r /t 1")
                answer = "Ok bye"
            except:
                answer = "Sorry unable to restart"
        
        elif "press " in q:
            try:
                q= q.replace('press ','')
                if (q=="enter"):
                    keyboard.press(Key.enter)
                    keyboard.release(Key.enter)
                elif (q=="tab"):
                    keyboard.press(Key.tab)
                    keyboard.release(Key.tab)
                else:
                    pass
                answer = "pressing"
            except:
                answer = "Sorry unable to type"
        
        elif "open whatsapp" in q or "whatsapp kholo" in q or "open whatsapp web" in q or "whatsapp web kholo" in q:
            try:
                webbrowser.open('https://web.whatsapp.com')
                answer = "opening whatsapp web in chrome"
            except:
                answer = "Sorry I unable to open whatsapp web"
        
        elif "search " in q:
            q= q.replace('search ','')
            try:
                if "on youtube" in q:
                    q= q.replace('on youtube','')
                    q= q.replace(' ','+')
                    q= q[:-1]
                    webbrowser.open(f"https://www.youtube.com/results?search_query={q}")
                    answer = "searching on youtube"
                elif "on google" in q:
                    q= q.replace('on google','')
                    q= q.replace(' ','+')
                    q= q[:-1]
                    webbrowser.open(f"https://www.google.com/search?q={q}")
                    answer = "searching on google"
                else:
                    pass
            except:
                answer = "Sorry I unable to search"
        elif "your name" in q or "who are you" in q:
            answer ="I am Om's Assistant created by Om"
        
        elif "tumhara naam" in q or "apna naam" in q or "kaun ho tum" in q or "kya naam" in q:
            answer ="main Om ki assistant hu , Om dwara banaai gai"
        
        else:
            answer= "No Command Such as"
    except:
        print("something went wrong")

    return answer




# speaker

def speakans(ans):
    
    language="en"
    output= gTTS(text=ans,lang=language, slow= False)
    num= random.random()

    output.save(f"static/output{num}.mp3")
    return f"static/output{num}.mp3"





@app.route("/")
def hello_world():
    return render_template('index.html' ,a=f'<div class="left"><p class="box2">Hello Om Bro! How can I help you</p></div>')

@app.route('/process', methods=['POST']) 
def getvalue():
    text =  request.get_json()['textbox']

    # print(text)
    ans=getans(text)
    speak= speakans(ans)
    return jsonify({"Ans": ans , "file":speak})




if __name__ == '__main__': 
    # app.run(debug=True) 
    app.run(host='0.0.0.0',port=5500)