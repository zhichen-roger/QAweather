import pyaudio
import wave
import  playmp3
from aip import AipSpeech
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
res_str='学校、幼儿园采取适当措施，保证学生和幼儿安全'
synth_context=client.synthesis(res_str,'zh',1,{
    'spd':4,
    'vol': 5,
    'pit':9,
    'per':4})
with open("synth.mp3","wb")as f:
    f.write(synth_context)
playmp3.play_mp3("synth.mp3")