import pyowm
import telebot
from googletrans import Translator

TOKEN = '5868909460:AAGMwqOVw0utplOmfoKITK8YQotgcUE34_A'
bot = telebot.TeleBot(TOKEN)

owm = pyowm.OWM('b4abed25005ae41d6dfcda82c3a35539')
mgr = owm.weather_manager()

# Turkish translations objesi oluşturun
translator = Translator()

# Telegram bot komutu /hava için işlev
@bot.message_handler(commands=['hava'])
def send_weather(message):
    # Kullanıcının kim olduğunu öğrenin
    user_name = message.from_user.username

    observation = mgr.weather_at_place('Inegol, TR')
    w = observation.weather
    temperature = w.temperature('celsius')['temp']
    humidity = w.humidity
    wind_speed = w.wind()['speed']

    # Hava durumu açıklamasını Türkçeye çevirin
    weather_description = w.detailed_status
    description_tr = translator.translate(weather_description, src='en', dest='tr').text

    # Hava durumu açıklamasına göre öneriler
    if "rain" in weather_description:
        outfit = 'Şemsiye almayı unutma!'
    elif "cloud" in weather_description:
        outfit = 'Bugün biraz bulutlu, yanına bir ceket alman iyi olabilir.'
    elif "sun" in weather_description:
        outfit = 'Hava bugün çok güzel, rahat bir şekilde giyinebilirsin.'
    else:
        outfit = 'Bugün hava biraz değişken, hazırlıklı olmakta fayda var.'

    # Hava durumu yanıtı ve önerileri içeren yanıt
    response = f"İnegöl'ün hava durumu: \n Sıcaklık: {temperature}°C \n Durum: {description_tr} \n Nem: %{humidity} \n Rüzgar Hızı: {wind_speed} m/s \n\n{outfit}"

    # Kullanıcının kim olduğunu yanıtınıza ekleyin
    bot.send_message(message.chat.id, f"Selam, @{user_name}\n{response}")

# Bot'u başlatın
bot.polling()
