import PySimpleGUI as psg
import pyttsx3

speaker = pyttsx3.init()

layout = [
    [psg.Text('What should I say:')],
    [psg.InputText(key='-INPUT-')],
    [psg.Text('Select a voice:')],
    [psg.Radio('Male', "RADIO1", default = True, key ='-MALE-'),
     psg.Radio('Female', "RADIO1", key ='-FEMALE-'),
     ],
    [psg.Text('VOLUME: '),
     psg.Slider(key='-VOLUME-',range=(0,10), size=(18, 15), orientation='horizontal')],
    [psg.Button('Speak'), psg.Button('Exit')]
]

window = psg.Window('AI AUDIO', layout)

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Speak':
        # Initialize the pyttsx3 engine
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        volume = engine.getProperty('volume')
        set_volume = values['-VOLUME-']
        # Get the text from the input box
        text = values['-INPUT-']

        voices = engine.getProperty('voices')

        # Set the voice type
        if values['-MALE-']:
            engine.setProperty('voice', voices[0].id)
        elif values['-FEMALE-']:
            engine.setProperty('voice', voices[1].id)
           
        engine.setProperty('volume', set_volume )
        engine.say(text)

        engine.runAndWait()


window.close()
