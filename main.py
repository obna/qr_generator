import wifi_qrcode_generator
import qrcode
import cv2

qrtype = int(input("1) Website\t2) Wifi\t3) Scan\nEnter 1, 2, or 3: "))


def qrd_website():
    url = input('Input URL')
    filename = "qrd_site.png"
    img = qrcode.make(url)
    img.save(filename)


if qrtype == 1:
    qrd_website()
