import telebot
from config import TOKEN
#Импорт библиотек

bot = telebot.TeleBot(TOKEN)
#Объект бот из класса
@bot.message_handler(commands=['help'])
def handle_start(message):
    bot.send_message(message.chat.id, '''Привет! Я бот, вот команды которые ты можешь использовать при роботе со мной
                    /start - знакомство с ботом и что он умеет
                    /best_film - выбор фильма по твоим критериям
                    ''')

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который может подбирать фильмы по критериям, напиши /help для большего количества функций")

@bot.message_handler(commands=['best_film'])
def get_genre(message):
    genre_question = bot.send_message(message.chat.id, '''Напиши жанр который ты хочешь из этих:
                                                        1.Animation
                                                        2.Adventure
                                                        3.Comedy
                                                        4.Action
                                                        5.Thriller
                                                        6.Drama
                                                        7.Romance
                                                        8.Biography
                                                        9.History
                                                        10.Crime
                                                        11.Mystery
                                                        12.Family
                                                        13.War
                                                        14.Fantasy
                                                        15.Music
                                                        16.Horror
                                                        17.Sport
                                                        18.Sci-Fi
                                                        19.Documentary
                                                        20.Western
                                                        21.Musical
                                                        22.Film-Noir
                                                        23.Short
                                                        24.News''')
    bot.register_next_step_handler(genre_question, get_vote)  

def get_vote(message): 
    vote = message.text
    style_question = bot.send_message(message.chat.id, 'С какой оценки начать поиск от 1 до 10?')
    bot.register_next_step_handler(style_question, id) 

    






if __name__=="__main__":
    bot.polling(non_stop= True)
