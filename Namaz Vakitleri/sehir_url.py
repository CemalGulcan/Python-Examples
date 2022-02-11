import requests

def sehir_url_cagirma():
    sehir_url = "https://ezanvakti.herokuapp.com/sehirler?ulke=2"
    sehir_response = requests.get(sehir_url)
    sehir_verileri = sehir_response.json()

    return sehir_verileri