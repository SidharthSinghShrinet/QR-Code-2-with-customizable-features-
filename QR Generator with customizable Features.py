import qrcode 
from PIL import Image

qr=qrcode.QRCode(version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=5
)
A=input("Enter the URL :")
B=input("Please enter the inside color name :")
C=input("Please enter the outside color name :")

qr.add_data(A)
qr.make(fit=True)
img=qr.make_image(fill_color=B,back_color=C)
img.save("Generate1.png")