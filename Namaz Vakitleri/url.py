import requests

def ilce_url_cagirma(a):
    ilce_url = "https://ezanvakti.herokuapp.com/ilceler?sehir="
    ilce_response = requests.get(ilce_url + str(a))
    ilce_verileri = ilce_response.json()

    return ilce_verileri
