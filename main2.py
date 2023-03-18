import telebot
import pyowm
import requests

# Bot API tokenınızı girin
TOKEN = '5868909460:AAGMwqOVw0utplOmfoKITK8YQotgcUE34_A'
bot = telebot.TeleBot(TOKEN)

# OpenWeatherMap API anahtarınızı girin
owm = pyowm.OWM('b4abed25005ae41d6dfcda82c3a35539')
mgr = owm.weather_manager()

# Eczane Bilgi Sistemi API adresi
EPS_API = 'https://api.collectapi.com/health/dutyPharmacy'

# CollectAPI için API anahtarınızı girin
COLLECT_API_KEY = 'apikey 3BACHLKO50gzkmkZpDHvL4:48BkD3i47hCl1eQabXF1hb'


# Telegram bot komutu /hava için işlev
@bot.message_handler(commands=['hava'])
def send_weather(message):
    observation = mgr.weather_at_place('Inegol, TR')
    w = observation.weather
    temperature = w.temperature('celsius')['temp']
    humidity = w.humidity
    wind_speed = w.wind()['speed']
    description = w.detailed_status
    response = f"İnegöl'ün hava durumu: \n Sıcaklık: {temperature}°C \n Nem: %{humidity} \n Rüzgar Hızı: {wind_speed} m/s"

    # EPS API'ye istek gönderin
    headers = {'Authorization': f"apikey {COLLECT_API_KEY}"}
    params = {'il': 'Bursa', 'ilce': 'Inegol'}
    response = requests.get(EPS_API, headers=headers, params=params)

    # EPS API'den verileri işleyin ve yanıt oluşturun
    data = response.json()
    if data['success'] and data['result']:
        pharmacies = '\n'.join([f"- {p['name']} ({p['address']})" for p in data['result']])
        response += f"\n\nNöbetçi eczaneler: \n{pharmacies}"
    else:
        response += "\n\nNöbetçi eczane bilgisi bulunamadı."

    bot.send_message(message.chat.id, response)


# Bot'u başlatın
bot.polling()


import telebot
import pyowm
import requests

# Bot API tokenınızı girin
TOKEN = '5868909460:AAGMwqOVw0utplOmfoKITK8YQotgcUE34_A'
bot = telebot.TeleBot(TOKEN)

# OpenWeatherMap API anahtarınızı girin
owm = pyowm.OWM('API_KEY')
mgr = owm.weather_manager()

# OpenTraffic.io API URL'si
TRAFFIC_API_URL = 'https://api.opentraffic.io/v1.1/traffic'

# Telegram bot komutu /hava için işlev
@bot.message_handler(commands=['hava'])
def send_weather(message):
    observation = mgr.weather_at_place('Inegol, TR')
    w = observation.weather
    temperature = w.temperature('celsius')['temp']
    humidity = w.humidity
    wind_speed = w.wind()['speed']
    description = w.detailed_status
    response = f"İnegöl'ün hava durumu: \n Sıcaklık: {temperature}°C \n Nem: %{humidity} \n Rüzgar Hızı: {wind_speed} m/s \n Betülü Çok Seviyorum"

    # Trafik yoğunluğu verilerini alın
    response = requests.get(TRAFFIC_API_URL)
    traffic_data = response.json()

    # Trafik yoğunluğunu kullanıcıya gösterin
    response = f"{response}\n\nŞehirdeki trafik yoğunluğu: {traffic_data['congestion']['level']}"
    bot.send_message(message.chat.id, response)

# Bot'u başlatın
bot.polling()

