import requests
def namaz_vakitleri(a):
    namaz_url = "https://ezanvakti.herokuapp.com/vakitler?ilce="
    namaz_response = requests.get(namaz_url+str(a))
    namaz_verileri = namaz_response.json()

    return namaz_verileri
