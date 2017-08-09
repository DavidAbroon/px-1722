
from picamera import PiCamera
from time import sleep

import os

def displayMainMenu():
    print("1. Take new Images")
    print("2. Save all images to the remote serve")
    print("3. Qquit")

    answer = int(input("Select Menu Option"))

    processMenuResponse(answer)

def processMenuResponse(answer):
    if answer == 1:
        createNewProject()

def createNewProject():
    project = str(raw_input("Enter Project name"))
    #Set up paths for image transfer
    localPath = '/home/pi/thomas/img/' + project + '.jpg'
    #remotePath = '/Users/addallal/Desktop/PushImage/pushedImage.jgp'

    camera = PiCamera()

    #Rotate Lense image preview/capture if needed
    #camera.rotation = 180

    camera.start_preview(alpha=200)

    #Allow lense to adjust to light
    sleep(2)

    #Capture an image
    camera.capture(localPath)

    camera.stop_preview()

    #copy image once captured to management PC
    #os.system("scp /home/pi/Documents/scannedImage.jpg addallal@andrews-mbp-2:/Users/addallal/Desktop/PushImage")


displayMainMenu()


