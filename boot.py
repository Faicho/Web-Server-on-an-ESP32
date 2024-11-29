import socket
from machine import Pin
import network
import esp
esp.osdebug(None)

#garbage collection
import gc
gc.collect()

ssid = '[INSERT]'
password = '[INSERT]'

#station mode is where the esp32 connects to your existing wifi network
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

led = Pin(2, Pin.OUT)
