import PySimpleGUI as sg
from tkinter import Tk  # in Python 2, use "Tkinter" instead
output = ""
west1 = [3, 1, 1, 0, 1, 3, 2, 2, 3, 3, 0, 4, 0, 4, 1, 1, 3, 0, 2, 3, 2, 1, 1, 4, 3, 1, 3, 0, 3, 3, 0, 0, 4, 0, 2, 4, 0,
         0, 4, 5,
         0, 3, 2, 0, 4, 1, 2, 2, 0, 0, 0, 1, 4, 2, 2, 2, 4, 2, 1, 2, 2, 2, 2, 0, 1, 1, 0, 0, 0, 3, 2, 0, 1, 3, 4, 1, 1,
         0, 1, 5,
         0, 2, 0, 2, 0, 1, 0, 4, 4, 0, 0, 0, 1, 0, 4, 0, 4, 4, 0, 4, 0, 1, 4, 4, 1, 4, 2, 0, 3, 3, 0, 2, 2, 0, 3, 4, 1,
         3, 1, 5,
         1, 1, 1, 2, 1, 3, 1, 3, 0, 0, 0, 1, 1, 0, 2, 0, 2, 0, 1, 4, 2, 2, 3, 1, 3, 3, 1, 4, 4, 1, 3, 4, 1, 4, 4, 1, 4,
         0, 1, 5,
         2, 1, 2, 2, 2, 3, 3, 0, 3, 2, 4, 4, 0, 0, 0, 2, 4, 3, 2, 3, 1, 1, 1, 0, 2, 2, 1, 2, 3, 1, 0, 3, 1, 0, 2, 2, 0,
         4, 3, 5,
         4, 0, 3, 4, 3, 1, 4, 0, 1, 2, 2, 2, 1, 1, 1, 3, 4, 0, 2, 1, 0, 3, 0, 1, 4, 1, 3, 3, 4, 1, 2, 2, 1, 3, 3, 0, 1,
         3,
         2, 5,
         0, 2, 4, 1, 4, 2, 2, 1, 4, 2, 2, 2, 0, 3, 0, 2, 4, 2, 0, 0, 1, 2, 3, 2, 1, 2, 4, 0, 2, 3, 2, 3, 2, 0, 1, 4, 0,
         3, 5,
         3, 1, 0, 1, 3, 2, 2, 1, 1, 2, 1, 3, 0, 2, 0, 3, 2, 2, 2, 2, 0, 0, 4, 2, 2, 3, 1, 0, 3, 1, 3, 2, 2, 4, 1, 1, 3,
         5]
layout = []
temp = []
count = 0
trigram = [[0], [0]]
tricount = 0
image_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15\xc4\x89\x00\x00\x00\rIDATx\x9cc````\x00\x00\x00\x05\x00\x01\xa5\xf6E@\x00\x00\x00\x00IEND\xaeB`\x82'
for x in west1:
    if x == 0:
        temp.append(sg.Button("☺", key="eye", image_data=image_data, font=("", 16, "bold"), image_size=(30, 30)))
    if x == 1:
        temp.append(sg.Button("↑", key="up", image_data=image_data, font=("", 16, "bold"), image_size=(30, 30)))
    if x == 2:
        temp.append(sg.Button("→", key="right", image_data=image_data, font=("", 16, "bold"), image_size=(30, 30)))
    if x == 3:
        temp.append(sg.Button("↓", key="down", image_data=image_data, font=("", 16, "bold"), image_size=(30, 30)))
    if x == 4:
        temp.append(sg.Button("←", key="left", image_data=image_data, font=("", 16, "bold"), image_size=(30, 30)))
    if x == 5:
        layout.append(temp)
        temp = []
        count = count + 1
        if count % 2 == 1:
            temp.append(sg.Button("☻", image_data=image_data, font=("", 16, "bold"), image_size=(7, 30)))

layout.append([sg.Text("Output: ", font=("", 16, "bold"), key='Output')])
layout.append([sg.Button("print", font=("", 16, "bold"), image_size=(7, 30))])
# sg.Window(title="The Eyes John, What Do They MEAN!?!", layout=[[]], margins=(500, 50)).read()
# Create the window
window = sg.Window("The Eyes John, What Do They MEAN!?!", layout)


def waltz(triarr):
    alparray = [['a'], ['b', 'c', 'd'], ['e', 'f', 'g', 'h', 'i'], ['j', 'k', 'l', 'm', 'n', 'o', 'p'],
                ['q', 'r', 's', 't', 'u'], ['v', 'w', 'x'], ['y']]
    triarr[1][0] = triarr[1][0] + 3
    if triarr[1][0] == 1 or triarr[1][0] == 5:
        triarr[0][0] = triarr[0][0] + 1
    if triarr[1][0] == 2 or triarr[1][0] == 4:
        triarr[0][0] = triarr[0][0] + 2
    if triarr[1][0] == 3:
        triarr[0][0] = triarr[0][0] + 3
    return alparray[triarr[1][0]][triarr[0][0]]


# Create an event loop
while True:
    event, values = window.read()
    if event == "☻":
        break
    if "eye" in event:
        tricount = tricount + 1
    if "up" in event:
        trigram[1][0] = trigram[1][0] - 1
        tricount = tricount + 1
    if "left" in event:
        trigram[0][0] = trigram[0][0] + 1
        tricount = tricount + 1
    if "right" in event:
        trigram[0][0] = trigram[0][0] + 1
        tricount = tricount + 1
    if "down" in event:
        trigram[1][0] = trigram[1][0] - 1
        tricount = tricount + 1
    if "print" in event:
        r = Tk()
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append(output)
        r.update()  # now it stays on the clipboard after the window is closed
    if tricount == 3:
        tricount = 0
        output = output + waltz(trigram)
        trigram = [[0], [0]]
    window['Output'].update('Output: ' + output)
window.close()
