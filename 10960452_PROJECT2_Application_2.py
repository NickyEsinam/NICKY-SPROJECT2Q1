 #ID: 10960452

import qrcode
from PIL import Image
import PySimpleGUI as psg


layout = [[psg.Text('Enter text to generate QR code:'), psg.InputText()],
          [psg.Button('Create QR Code')],
          [psg.Image(key='qrcode')]]

window = psg.Window('QR Code Generator', layout)

while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED:
        break
    elif event == 'Create QR Code':
        input_text = values[0]
        if input_text:
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(input_text)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            img.save("qrcode.png")

            qr_code_image = Image.open("qrcode.png")
            window['qrcode'].update(data=qr_code_image.tobytes())

window.close()
