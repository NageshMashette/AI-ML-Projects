import os
from gtts import gTTS
text = "Previously we saw how to serve a tensorflow model on local. One might say, 'Great! Let's just run it on a cloud instance, open the correct ports and tadaa! I am serving my model worldwide! This approach may be ok for testing purposes or for a side project of yours, but I strongly advise against it. Your server can be easily overwhelmed and security issues will quickly arise."

lang = 'en'

myobj = gTTS(text=text,  lang=lang, slow=False)
myobj.save("audio.mp3")
os.system("audio.mp3")
