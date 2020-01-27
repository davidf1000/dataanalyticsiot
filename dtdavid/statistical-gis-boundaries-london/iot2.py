#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 20:47:23 2020

@author: davidfauzi
"""


#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 11:40:49 2019

@author: davidfauzi
"""
from Adafruit_IO import Client, Feed, RequestError
import time
import requests
import base64
import os
import cv2
# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = '0f7873c4c7bf48bb95e79d4112889e8e'

# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'davidfauzi'

# Create an instance of the REST client
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

#DEFINE ALL THE FEEDS

cam = aio.feeds('cam')
basex=aio.feeds('basex')
""" requests part"""

    
    
def sendpic():
    #SEND IMAGE
    """
    Plan: Asumsi sudah ada gambar send.jpg, dari situ disini diubah base64 lalu dikirim ke cam
    """
    with open("send.jpg", "rb") as imageFile:
        image = base64.b64encode(imageFile.read())
        # encode the b64 bytearray as a string for adafruit-io
        image_string = image.decode("utf-8")
    try:
      aio.send('cam', (image_string))
      print('Picture sent to Adafruit IO')
      print(len(image_string))
    except:
      print('Sending to Adafruit IO Failed...')
      print(len(image_string))
    time.sleep(0.4)

#MAIN LOOP
while(True):

    aio.send('basex','23')

    time.sleep(10)
#def iftttpush(temp,wind,hum,pplup,ppldown,crowd):
