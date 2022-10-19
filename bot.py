import telebot
from main import check
from secret import API

bot = telebot.TeleBot(API)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id,f"Здравствуйте, {message.from_user.first_name}! Вас приветствует чат-бот по поиску "
                                     f"вакансий на сайте rabota.by. Для того, чтобы найти вакансии, введите ключевое "
                                     f"слово для поиска и я покажу вам 5 последних вакансий по данному запросу.")

@bot.message_handler()
def get_text(message):
    user_request = message.text
    bot.send_message(message.chat.id, f'Подождите немного, я собираю информацию...')
    answer = check(user_request)
    bot.send_message(message.chat.id, text=answer)
    bot.send_message(message.chat.id, f'Для нового запроса введите снова ключевое слово.')

bot.polling(none_stop=True)