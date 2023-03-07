import PySimpleGUI as sg
import time
import scoring
from essential_generators import DocumentGenerator

#default Settings
guiFont = ("Verdana", 16)
inputFont = ("Verdana", 20)
sg.theme('DarkGrey11')
textBoxSize = (30, 8)

inputCol = [
    [sg.Text("Type in this box", font=guiFont)],
    [sg.Multiline(key="inputText", size=textBoxSize, no_scrollbar=True, font=inputFont)],
    [sg.Button("Submit")]
]

testCol = [
    [sg.Text("Text to type", font=guiFont)],
    [sg.Multiline(key="randomText", size=textBoxSize, no_scrollbar=True, font=inputFont, disabled=True)],
]

buttonRow = [[[sg.Button('Start'), sg.Button('View Data')], sg.Text("Score: ", key="score", font=guiFont)]]

layout = [[sg.Column(inputCol, vertical_alignment='top'), sg.Column(testCol, vertical_alignment='top'), buttonRow]]

window = sg.Window("Type Training by Vlad Apostol", layout, size=(1000, 420))

while True:
    event, value = window.read()
    if event == "Start":
        randomText = DocumentGenerator().sentence()
        window['randomText'].update(randomText)
        start = time.time()
    if event == "Submit":
        end = time.time()
        result = scoring.calculateScore(value['inputText'], value['randomText'], start, end)
        window['inputText'].update('')
        window['randomText'].update('')
        window['score'].update(result)
    if event == "View Data":
        print(scoring.returnGraph())
    if event == sg.WINDOW_CLOSED:
        break

window.close()


