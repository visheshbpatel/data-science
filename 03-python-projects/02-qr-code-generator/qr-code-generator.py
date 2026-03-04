import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr_img = qrcode.make("https://github.com/visheshbpatel")

qr_img.save("qr-img.png", scale=10)


d = decode(Image.open("qr-img.png"))
print(d[0].data.decode("ascii"))