from captcha.image import ImageCaptcha
from datetime import datetime

hoy = datetime.today()
timestamp = datetime.timestamp(hoy)

image = ImageCaptcha(width=420,height=150)

texto = "Vanessa Culoncita"

data = image.generate(texto)

image.write(texto,"captcha_"+str(timestamp)+".png")