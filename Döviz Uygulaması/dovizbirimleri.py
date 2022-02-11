import requests

def doviz_verileri():

    url = "http://data.fixer.io/api/latest?access_key=ff94219dd36d64ad5ac46c377fadf181"

    response = requests.get(url)

    veriler = response.json()

    list = []

    for i in veriler["rates"].keys():
        list.append(i)

    return list

def doviz_verileri1(a):

    url = "http://data.fixer.io/api/latest?access_key=ff94219dd36d64ad5ac46c377fadf181"

    response = requests.get(url)

    veriler = response.json()

    return (veriler["rates"][a])
