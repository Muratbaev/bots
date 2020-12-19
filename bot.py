#импортировать нашу библиотеку и подключить токен бота
import telebot;
bot = telebot.TeleBot('%ваш токен%');
#объявим метод для получения текстовых сообщений
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
#В этом участке кода мы объявили слушателя для текстовых сообщений и метод их обработки. Поле content_types может принимать разные значения
@bot.message_handler(content_types=['text', 'document', 'audio'])
#бот отвечает пользователю своими швблонами
if message.text == "Привет":
    bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
elif message.text == "/help":
    bot.send_message(message.from_user.id, "Напиши привет")
else:
    bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
    bot.polling(none_stop=True, interval=0)
    python bot.py