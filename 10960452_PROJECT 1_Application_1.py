 #ID: 10960452

import PySimpleGUI as psg
import pyttsx3


layout = [
    [psg.Text('Enter text to speak:')],
    [psg.InputText(key='input_text')],
    [psg.Text('Select voice type:')],
    [psg.Radio('Male', 'voice_type', key='male_voice', default=True),
     psg.Radio('Female', 'voice_type', key='female_voice')],
    [psg.Button('Speak')],
    [psg.Text('Volume:'),
     psg.Slider(range=(0, 100), orientation='h', default_value=50, key='volume')],
    [psg.Text('Speed:'),+
     psg.Slider(range=(0, 300), orientation='h', default_value=100, key='speed')],
    [psg.Quit()]
]

window = psg.Window('Text-to-Speech App', layout)

engine = pyttsx3.init()

while True:
    event, values = window.Read()

    if event in (None, 'Quit'):
        break

    elif event == 'Speak':
        input_text = values['input_text']
        male_voice = values['male_voice']
        voice = engine.getProperty('voices')

        if male_voice:
            engine.setProperty('voice', voice[0])
        else:
            engine.setProperty('voice', voice[1])

        volume = values['volume']
        speed = values['speed']
        engine.setProperty('volume', volume / 100)
        engine.setProperty('rate', speed)

        engine.say(input_text)
        engine.runAndWait()

window.Close()
engine.stop()
