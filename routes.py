from flask import *
from sensor import get_data
import json

app = Flask(__name__)


@app.route('/senzor')
def senzor():
    temp,hum = get_data()
    data = {'temperature':temp,
    	      'humidity':hum}
    return json.dumps(data)

@app.route()
def index():
    return "<h1>Nothing here<h1>"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8969,debug=True)
