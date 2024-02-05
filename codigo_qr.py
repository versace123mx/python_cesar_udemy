import qrcode
from datetime import datetime

hoy = datetime.today()
timestamp = datetime.timestamp(hoy)

qr = qrcode.make('Hello world Venessita Culoncita')
qr.save('MyQR_'+str(timestamp)+'.png')