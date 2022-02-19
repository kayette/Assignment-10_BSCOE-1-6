import pyqrcode
from PIL import Image

def generateQR():
    with open('Contact Tracing Form.txt') as f:
        form_data = f.read()
    genQR = pyqrcode.create(form_data, error='H')
    with open('QRCode.png', 'wb') as v:
        genQR.png(v, scale=10)
    finQR = Image.open('QRCode.png')
    width, height = finQR.size
    logo_size = 300
    finQR = finQR.convert("RGBA")
    genLogo = Image.open('Logo.png')
    xmin = ymin = int((width / 2) - (logo_size / 2))
    xmax = ymax = int((width / 2) + (logo_size / 2))
    genLogo = genLogo.resize((xmax - xmin, ymax - ymin))
    finQR.paste(genLogo, (xmin, ymin, xmax, ymax))
    finQR.show()

generateQR()