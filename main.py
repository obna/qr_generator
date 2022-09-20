import wifi_qrcode_generator
import qrcode
import cv2
import os
import shutil


def move_it(toBeMoved):
    bake = shutil.move(toBeMoved, finalDestination)
    print('A new QR code has generated on path ' + bake[1:])


def qrd_website():
    url = input('Input URL: ')
    filename = "qrd_site.png"
    img = qrcode.make(url)
    img.save(filename)
    moveThis = foundHere + '/' + filename
    move_it(moveThis)


def qrd_wifi():
    name = input('Enter WPA wifi name')
    value = input('Enter password')
    wifi_qrcode_generator.wifi_qrcode(
        name, False, 'WPA', value)


def qrd_scan():
    pass


foundHere = os.path.dirname(os.path.abspath(__file__))
finalDestination = '/'+foundHere+"/qr-codes"

qrtype = int(input("Enter 1 for Website, 2 for Wifi, 3 to Scan, 4 to stop: "))

if qrtype == 1:
    qrd_website()
if qrtype == 2:
    pass
if qrtype == 3:
    pass
