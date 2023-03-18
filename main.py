import os
from dotenv import load_dotenv
import telebot
from modüller import pharmacy, upcoming_events, weather
from modüller.pharmacy import get_pharmacies

# .env dosyasındaki TOKEN'ı yükleyin
load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = telebot.TeleBot(TOKEN)


# Tüm mesajları işleme fonksiyonu
def save_chat_id(message):
    chat_id = message.chat.id
    with open("kullanıcı_bilgileri/chat_idler.txt", "a+") as file:
        file.seek(0)
        if str(chat_id) not in file.read().split():
            file.write(str(chat_id) + "\n")

# Telegram bot komutu /basla için işlev
@bot.message_handler(commands=['basla'])
def send_welcome(message):
    save_chat_id(message)
    bot.reply_to(message,
                 "/hava: Bu komut, hava durumunu öğrenmek için kullanılır. Bot kullanıcısının konumunu alarak, o konuma ait hava durumu bilgilerini gönderir ve hava durumuna göre öneriler verir. \n /etkinlik: Bu komut, yaklaşan etkinlikleri öğrenmek için kullanılır. Bot, İnegöl'de yaklaşan etkinlikleri ayıklar ve en yakın tarihte gerçekleşecek olan 3 etkinliği sunar. \n /eczane: Bu komut, nöbetçi eczaneleri öğrenmek için kullanılır. Bot, İnegöldeki Nöbetçi Eczaneleri anlık olarak çeker ve eczane hakkında bilgi verir.")


# Telegram bot komutu /hava için işlev
@bot.message_handler(commands=['hava'])
def send_weather(message):
    # Kullanıcının kim olduğunu öğrenin
    user_name = message.from_user.username

    response = weather.get_weather()

    # Kullanıcının kim olduğunu yanıtınıza ekleyin
    bot.send_message(message.chat.id, f"Selam, @{user_name}\n{response}")


# Telegram bot komutu /etkinlik için işlev
@bot.message_handler(commands=['etkinlik'])
def send_events(message):
    # Kullanıcının kim olduğunu öğrenin
    user_name = message.from_user.username

    events = upcoming_events.get_events()

    # Kullanıcının kim olduğunu yanıtınıza ekleyin
    bot.send_message(message.chat.id, f"Selam, @{user_name}\n{events}")

# Telegram bot komutu /eczane için işlev
@bot.message_handler(commands=['eczane'])
def send_pharmacies(message):

    # Kullanıcının kim olduğunu öğrenin
    user_name = message.from_user.username

    pharmacies = get_pharmacies()

    output_message = "Nöbetçi Eczaneler:\n\n"

    for pharmacy in pharmacies:
        output_message += f"{pharmacy['name']}\n{pharmacy['phone']}\n{pharmacy['address']}\n{pharmacy['date_range']} \n\n"

   # Kullanıcının kim olduğunu yanıtınıza ekleyin
    bot.send_message(chat_id=message.chat.id, text=output_message)


# Botu başlatın
bot.polling()
