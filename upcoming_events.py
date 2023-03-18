import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


def get_events():
    url = "https://www.inegol.bel.tr/guncel/etkinlikler/"
    response = requests.get(url)
    html_icerigi = response.content

    soup = BeautifulSoup(html_icerigi, "html.parser")
    etkinlikler = soup.find_all("div", {"class": "event-box-title"})

    event_list = []
    today = datetime.now().date()
    for etkinlik in etkinlikler:
        etkinlik_adi = etkinlik.find("h4").text.strip()
        etkinlik_tarihi = etkinlik.find("b").text.strip()
        etkinlik_tarihi_obj = datetime.strptime(etkinlik_tarihi, '%d.%m.%Y / %H:%M')
        etkinlik_konumu = etkinlik.find("span").text.strip()

        if etkinlik_tarihi_obj.date() >= today:
            event_list.append((etkinlik_adi, etkinlik_tarihi_obj, etkinlik_konumu))

    event_list = sorted(event_list, key=lambda x: x[1])[:3]
    formatted_events = []
    for event in event_list:
        formatted_event = f"🎉 {event[0]}\n📅 {event[1].strftime('%d.%m.%Y / %H:%M')}\n📍 {event[2]}\n"
        formatted_events.append(formatted_event)

    return "\n".join(formatted_events)
