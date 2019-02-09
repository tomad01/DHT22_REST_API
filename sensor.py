import Adafruit_DHT as dht
from Adafruit_BMP import BMP085
from datetime import datetime
import time,csv


def get_dht22_data():
    try:
        h,t = dht.read_retry(dht.DHT22, 4)
        status = "Ok"
    except Exception as er:
        status = str(er)
        h = 0
        t = 0
    return {'status':status,
            'temperature':{'value':"%.2f"%t,'unit':'C'},
            'humidity':   {'value':"%.2f"%h,'unit':'%'}}


def get_bmp180_data():
    try:
        bmp = BMP085.BMP085()
        status = "Ok"
        temp = bmp.read_temperature()
        pressure = bmp.read_pressure()
        altitude = bmp.read_altitude()
    except Exception as er:
        status = str(er)
        temp = 0
        pressure = 0
        altitude = 0
    return {'status':status,
            'temperature':{'value':"%.2f"%temp,'unit':'C'},
            'pressure':   {'value':"%.2f"%(pressure / 100.0),'unit':'hPa'},
            'altidude':   {'value':"%.2f"%altitude,'unit':'m'}}


    

    
    
    

