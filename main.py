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
    filename = input('Save this .png QR code as: ')
    img = qrcode.make(url)
    filename = filename+'.png'
    img.save(filename)
    moveThis = foundHere + '/' + filename
    move_it(moveThis)


foundHere = os.path.dirname(os.path.abspath(__file__))
finalDestination = '/'+foundHere+"/qr-codes"

qrtype = int(input("Enter 1 for Website, 2 for Wifi, 3 to Scan, 4 to stop: "))

if qrtype == 1:
    qrd_website()
if qrtype == 2:
    pass
if qrtype == 3:
    pass
