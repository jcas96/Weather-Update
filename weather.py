import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

n=ToastNotifier()

def getInfo(link):
    r=requests.get(link)
    return r.text


htmldata = getInfo("https://weather.com/weather/today/l/f925f1db2e723fe3cad20869825df22ad09788fb3650d4b2b45546294ccdba38")

soup = BeautifulSoup(htmldata, 'html.parser')


current = soup.find_all("span", class_="CurrentConditions--tempValue--MHmYY")
currentStr = (str(current))

temps = soup.find_all("div", class_="CurrentConditions--tempHiLoValue--3T1DG")
hiLo = (str(temps))

loc = soup.find_all("h1",class_="CurrentConditions--location--1YWj_")
location = (str(loc))

result = "Current Temp in "+(location[48:-6]) + " is: "+currentStr[82:84]+"\nHigh : "+hiLo[103:105]+"\nLow: "+hiLo[204:-28]
n.show_toast("Weather", result, duration=10)
