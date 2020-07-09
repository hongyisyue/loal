import board
import neopixel
import time
from LWRPClient import LWRPClient


pixels = neopixel.NeoPixel(board.D18, 256)
for x in range(0,256):
    pos = x % 3
    if pos == 0:
        pixels[x] = (30, 0, 0)

    elif pos == 1:
        pixels[x]= (0, 30, 0)
    else:
        pixels[x]= (0, 0, 30)
        
    pixels[x] = (0, 0, 0)
    
LWRP = LWRPClient("172.16.0.101", 93)
LWRP.login()

print (LWRP.deviceData())
print (LWRP.networkData())
print (LWRP.sourceData())
print (LWRP.destinationData())
print (LWRP.GPIData())
print (LWRP.GPOData())
