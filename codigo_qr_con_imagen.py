import qrcode
from PIL import Image
from datetime import datetime
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer,HorizontalBarsDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask,ImageColorMask

hoy = datetime.today()
timestamp = datetime.timestamp(hoy)

logo = Image.open('Screenshot_163.png')

# Ajustamos el tamaño de la imagen
hsize = int((float(logo.size[1])*float(100/float(logo.size[0]))))
logo = logo.resize((100, hsize))

qr_big = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr_big.add_data("https://www.python.org/")
qr_big.make()
img_qr_big = qr_big.make_image(image_factory=StyledPilImage, module_drawer=HorizontalBarsDrawer()).convert('RGB')

pos=((img_qr_big.size[0]-logo.size[0]) // 2, (img_qr_big.size[1] - logo.size[1]) // 2)

img_qr_big.paste(logo,pos)
img_qr_big.save('QRPrueba_'+str(timestamp)+'.png')