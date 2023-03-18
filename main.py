import telebot
import weather

TOKEN = '5868909460:AAGMwqOVw0utplOmfoKITK8YQotgcUE34_A'
bot = telebot.TeleBot(TOKEN)

# Telegram bot komutu /hava için işlev
@bot.message_handler(commands=['hava'])
def send_weather(message):
    # Kullanıcının kim olduğunu öğrenin
    user_name = message.from_user.username

    response = weather.get_weather()

    # Kullanıcının kim olduğunu yanıtınıza ekleyin
    bot.send_message(message.chat.id, f"Selam, @{user_name}\n{response}")

# Botu başlatın
bot.polling()
