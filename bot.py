import telebot
from config import TOKEN
#Импорт библиотек

bot = telebot.TeleBot(TOKEN)
#Объект бот из класса

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который ")

@bot.message_handler(commands=['best_film'])
def get_genre(message):
    genre_question = bot.send_message(message.chat.id, 'Напиши :')
    bot.register_next_step_handler(genre_question, get_year)  

def get_year(message): 
    year = message.text
    style_question = bot.send_message(message.chat.id, '')
    bot.register_next_step_handler(style_question, year) 






if __name__=="__main__":
    bot.polling(non_stop= True)