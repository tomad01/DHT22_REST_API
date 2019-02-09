from flask import *
from sensor import get_dht22_data,get_bmp180_data
import json

app = Flask(__name__)


@app.route('/senzor')
def senzor():
    dht22Data  = get_dht22_data()
    bmp180Data = get_bmp180_data()
    data = {'dht22':dht22Data,
    	    'bmp180':bmp180Data}
    return json.dumps(data)

@app.route()
def index():
    return "<h1>Nothing here<h1>"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8969,debug=True)
