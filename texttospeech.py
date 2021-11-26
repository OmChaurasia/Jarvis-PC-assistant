
from gtts import gTTS

t="Hello I am Om. The leader of world"
language="en"

output= gTTS(text=t,lang=language, slow= False)

output.save("output.mp3")