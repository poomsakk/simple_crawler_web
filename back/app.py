from flask import Flask, send_file
from flask_cors import CORS  # Req for Dev , not req for pythonanywhere.com
from crawler import getData, createFile

app = Flask(__name__)
CORS(app)  # Req for Dev , not req for pythonanywhere.com

tak_url = "https://th.wikipedia.org/wiki/%E0%B8%A3%E0%B8%B2%E0%B8%A2%E0%B8%8A%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B9%83%E0%B8%99%E0%B8%88%E0%B8%B1%E0%B8%87%E0%B8%AB%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B8%95%E0%B8%B2%E0%B8%81"
nakhon_nayok_url = "https://th.wikipedia.org/wiki/%E0%B8%A3%E0%B8%B2%E0%B8%A2%E0%B8%8A%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B9%83%E0%B8%99%E0%B8%88%E0%B8%B1%E0%B8%87%E0%B8%AB%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B8%99%E0%B8%84%E0%B8%A3%E0%B8%99%E0%B8%B2%E0%B8%A2%E0%B8%81"
nakhon_prathom_url = "https://th.wikipedia.org/wiki/%E0%B8%A3%E0%B8%B2%E0%B8%A2%E0%B8%8A%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B9%83%E0%B8%99%E0%B8%88%E0%B8%B1%E0%B8%87%E0%B8%AB%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B8%99%E0%B8%84%E0%B8%A3%E0%B8%9B%E0%B8%90%E0%B8%A1"
nakhon_phanom_url = "https://th.wikipedia.org/wiki/%E0%B8%A3%E0%B8%B2%E0%B8%A2%E0%B8%8A%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B9%83%E0%B8%99%E0%B8%88%E0%B8%B1%E0%B8%87%E0%B8%AB%E0%B8%A7%E0%B8%B1%E0%B8%94%E0%B8%99%E0%B8%84%E0%B8%A3%E0%B8%9E%E0%B8%99%E0%B8%A1"

# ====== PATH BELOW CAN SEE THROUGH DIRECTLY BROWSER ======


@app.route("/")
def hello_world():
    return "<h2>Hello, World!</h2><br/>for Tak go path => xxx/1 or xxx/11<br/>for Nakhon Nayok go path => xxx/2 or xxx/22<br/>for Nakhon Pratom go path => xxx/3 or xxx/33<br/>for Nakhon Pranom go path => xxx/4 or xxx/44"


@app.route("/1")
def getData_tak():
    global tak_url
    response = getData(tak_url)
    return '<br/>'.join(response)


@app.route("/2")
def getData_nakhon_nayok():
    global nakhon_nayok_url
    response = getData(nakhon_nayok_url)
    return '<br/>'.join(response)


@app.route("/3")
def getData_nakhon_pratom():
    global nakhon_prathom_url
    response = getData(nakhon_prathom_url)
    return '<br/>'.join(response)


@app.route("/4")
def getData_nakhon_pranom():
    global nakhon_phanom_url
    response = getData(nakhon_phanom_url)
    return '<br/>'.join(response)

# ====== USE PATH BELOW TO CALL FROM YOUR APP ======


@app.route("/Tak-data")
def getData_tak_api():
    global tak_url
    return getData(tak_url)


@app.route("/Nakhon_Nayok-data")
def getData_nakhon_nayok_api():
    global nakhon_nayok_url
    return getData(nakhon_nayok_url)


@app.route("/Nakhon_Prathom-data")
def getData_nakhon_pratom_api():
    global nakhon_prathom_url
    return getData(nakhon_prathom_url)


@app.route("/Nakhon_Phanom-data")
def getData_nakhon_pranom_api():
    global nakhon_phanom_url
    return getData(nakhon_phanom_url)

# =============== DOWNLOAD =============


@app.route('/Tak-csv')
def getFile_Tak():
    createFile('Tak', tak_url)
    try:
        return send_file('Tak.csv')
    except Exception as e:
        return str(e)


@app.route('/Nakhon_Nayok-csv')
def getFile_Nakhon_Nayok():
    createFile('Nakhon_Nayok', tak_url)
    try:
        return send_file('Nakhon_Nayok.csv')
    except Exception as e:
        return str(e)


@app.route('/Nakhon_Prathom-csv')
def getFile_Nakhon_Prathom():
    createFile('Nakhon_Prathom', tak_url)
    try:
        return send_file('Nakhon_Prathom.csv')
    except Exception as e:
        return str(e)


@app.route('/Nakhon_Phanom-csv')
def getFile_Nakhon_Phanom():
    createFile('Nakhon_Phanom', tak_url)
    try:
        return send_file('Nakhon_Phanom.csv')
    except Exception as e:
        return str(e)
