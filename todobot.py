import telebot
import random

token = "5701540465:AAEkZHbsrpqqZkeoEiy5fQuBDxZoUruQ--M"

bot = telebot.TeleBot(token)

HELP = """
/help - вывести список доступных команд.
/add - добавить задачу в формате <дата> <задача>.
/show <дата> - показать все добавленные задачи на конкретную дату.
/random - добавить случайную задачу на сегодня.
/exit - выйти из программы."""

RANDOM_TASKS = ["Почистить зубы", "Выпить кофе", "Вымыть посуду", "Погулять в парке", "Купить продукты", "Приготовить ужин", "Покормить кота"]

tasks = {}

def add_todo(date, task):
  if date in tasks:
      #Дата есть в словаре
      #Добавляем в список задачу
      tasks[date].append(task)
  else:
      #Даты нет в словаре
      #Создаем запись с ключем date
      tasks[date] = []
      tasks[date].append(task)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands=["add", "todo"])
def add(message):
    command = message.text.split(maxsplit=2)
    date = command[1].lower()
    task = command[2]
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["random"])
def random_add(message):
    date = "сегодня"
    task = random.choice(RANDOM_TASKS)
    add_todo(date, task)
    text = "Задача " + task + " добавлена на дату " + date
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["show", "print"])
def show(message): #message.text = /print <date>
    command = message.text.split(maxsplit=1)
    date = command[1].lower()
    text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + task + "\n"
    else:
        text = "Задач на эту дату нет"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["exit"])
def exit(message):
    bot.send_message(message.chat.id, "До встречи!")

#Постоянно обращается к серверам телеграм
bot.polling(none_stop=True)
