import requests
from bs4 import BeautifulSoup
import urllib.parse

def get_pharmacies():
    # İnternet sitesine bir istek gönderin
    url = "https://eczane.inegol.bel.tr/"
    response = requests.get(url)

    # İnternet sitesinin HTML içeriğini parse edin
    soup = BeautifulSoup(response.content, "html.parser")

    # Sayfadaki tüm eczane öğelerini bulun
    pharmacy_items = soup.find_all("div", {"class": "item"})

    # Her bir eczane öğesi üzerinde döngü yapın ve ilgili bilgileri çıkarın
    pharmacies = []
    for pharmacy in pharmacy_items:
        name = pharmacy.find("h2", {"class": "item-title"}).text
        date_range = pharmacy.find_all("li")[0].find("span").text
        phone = pharmacy.find_all("li")[1].find("a").text
        address = pharmacy.find_all("li")[2].find("address").text
       # address_map_url = "https://www.google.com/maps/search/?api=1&query=" + urllib.parse.quote_plus(address)
        pharmacies.append({
            "name": "🏥 " + name,
            "phone": "📞 " + phone,
            "address": "🏠 " + address,
            "date_range": "🗓️ " + date_range
        })

    return pharmacies
