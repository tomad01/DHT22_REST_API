import Adafruit_DHT as dht
from datetime import datetime
import time,csv


def get_data():
    """this func is returning (temp,hum) as numbers with two decimals casted in strings"""
    try:
        h,t = dht.read_retry(dht.DHT22, 4)
        return ("%.2f"%t,"%.2f"%h)
    except Exception as er:
        print str(er)
        return ("0","0")
    

    
    
    

