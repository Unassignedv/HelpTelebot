import requests
import telebot
from telebot import types

token = "518652*****:AAGeNrwq91****"
token_weather = "*******"

bot = telebot.TeleBot(token)
city = "Moscow,RU"


@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("Хочу", "/help", '/schedule', "/inst", "/vk", "привет", "погода", "погода на неделю")
    bot.send_message(message.chat.id, "Здравствуйте! У меня для вас новая информация о МТУСИ. Хотите узнать?",
                     reply_markup=keyboard)
    bot.send_message(message.chat.id, 'Привет! Хочешь узнать погоду?', reply_markup=keyboard)


@bot.message_handler(func=lambda msg: msg.text.lower() == "/help")
def help(message):
    bot.send_message(message.chat.id,
                     "Я умею: \n\n\n ✅ Присылать расписание на неделю (команда /schedule) \n\n\n ✅Прислать ссылку на сайт МТУСИ (напишите хочу) \n\n\n ✅Прислать ссылку на группу в ВК МТУСИ (команда /vk) \n\n\n ✅Прислать ссылку на Инстаграм МТУСИ")


@bot.message_handler(func=lambda msg: msg.text.lower() == "/schedule")
def schedule(message):
    bot.send_message(message.chat.id,
                     "ПОНЕДЕЛЬНИК \n \n ✅ 1) (лек) Философия (9:30-11:05) (Плужникова Н.Н.)\n \n ✅ 2) (пр) Иностранный язык (11:20-12:55) (Лапаев Л.Л.) \n \n ✅ 3) (пр) Введение в ИТ (13:10-14:45) (с 21.02.2022 по 24.04.2022) \n \n ✅ 4) (лек) Введение в ИТ (15:25-17:00) \n \n ⛔ 5) Пары нет (17:15-18:50) \n \n ВТОРНИК \n \n ⛔ 1) Пары нет (9:30-11:05) \n \n ✅2) (лек) Физика (11:20-12:55) (Иноземцева Н.Г.) (до 03.04.2022 ) \n \n ✅ 3) Пары нет (13:10-14:45) \n \n ✅ 4) (пр) Философия (15:25-17:00) (Плужникова Н.Н.) \n \n ⛔ 5) Пары нет (17:15-18:50) \n \n СРЕДА \n \n ⛔ 1) Пары нет (9:30-11:05) \n \n ✅ 2) (пр) Высшая математика (11:20-12:55) (Свентковский В.А.) (до 02.05.2022) \n \n ✅ 3) (пр) Теоретические основы электротехники (13:10-14:45) (Елисеев С.Н.) (до 15.05.2022) \n \n ✅ 4) (пр) Введение в ИТ (15:25-17:00) (с 21.02.2022 до 22.05.2022) \n \n ✅ 5) (пр) Высшая математика (17:15-18:50) (Свентковский С.Н.) \n \n ЧЕТВЕРГ \n \n ⛔ 1) Пары нет (9:30-11:05) \n \n ✅ 2) (лаб) Физика Ауд. 338 (11:20-12:55) (с 04.04.2022) (Тимошина М.И. ; Вальковский С.Н.) \n \n ✅ 3) (лаб) Инженерная и компьютерная графика Ауд. 223 (13:10-14:45) (с 04.04.2020 до 29.05.2022) (Борисова О.А.) \n \n ⛔ 4) Пары нет (15:25-17:00) \n \n ✅ 5) (лаб) Теоретические основы электротехники Ауд. 124 (17:15-18:50) (с 14.03.2022) (Микиртичан А.Г.) \n \n ПЯТНИЦА \n \n ⛔ 1) Пары нет (9:30-11:05) \n \n ✅ 2) (лек) Инженерная и компьютерная графика (11:20-12:55) (Борисова О.А.) (до 03.04.2020) \n \n ✅3) (лек) Теоретические основы электротехники (13:10-14:45) (Елисеев С.Н.) (до 03.04.2022) \n \n ✅ 4) (лек) Высшая математика (15:25-17:00) (Свентковский В.А.) \n \n ✅ 5) (лек) Социология (17:15-18:50) (Артамонова Я.С.) (до 7 недели) \n \n СУББОТА \n \n ✅ 1) (пр) Социология (9:30-11:05) (Артамонова Я.С.) (с 8 до 15 недели) \n \n ✅ 2) (пр) Элективные дисциплины по физической культуре и спорту (11:20-12:55) (Шамилов Г.С.) \n \n ✅ 3) пр) Элективные дисциплины по физической культуре и спорту (11:20-12:55) (Шамилов Г.С.) (13:10-14:45) \n \n ⛔ 4) Пары нет (15:25-17:00) \n \n ✅ 5) (лаб) Введение в ИТ Авиамоторная Ауд. УЛК-702 (17:15-18:50) (Колесников О.В.) (с 07.02.2022) \n \n")


@bot.message_handler(func=lambda msg: msg.text.lower() == "/inst")
def inst(message):
    bot.send_message(message.chat.id, "Ссылка на Инстаграм МТУСИ: https://www.instagram.com/mtuci.official/")


@bot.message_handler(func=lambda msg: msg.text.lower() == "/vk")
def vk(message):
    bot.send_message(message.chat.id, "Ссылка на группу Вконтакте МТУСИ: \n https://vk.com/mtuci")


@bot.message_handler(content_types=["text"])
def text_pogoda(message):
    if message.text.lower() == "хочу":
        bot.send_message(message.chat.id, "Здесь ты найдешь актуальное расписание: https://mtuci.ru/time-table/")
    elif message.text.lower() == "привет":
        bot.send_message(message.chat.id, "К сожалению автору не хватило воображения на ответ")
    elif message.text.lower() == "погода":
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': token_weather})

        if res.status_code != 200:
            print("Ошибка подключении к weather api")
            exit(0)

        data = res.json()
        weather_message = f"""
        Город: {city}\n
        Погодные условия: {data['weather'][0]['description']}\n
        Температура: {str(data['main']['temp'])}\n
        Скорость ветра: {str(data['wind']['speed'])}\n
        Видимость: {data['weather'][0]['description']}\n
        Минимальная температура: {str(data['main']['temp_min'])}\n
        Максимальная температура: {str(data['main']['temp_max'])}\n
        """
        bot.send_message(message.chat.id, weather_message)
    elif message.text.lower() == "погода на неделю":
        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': token_weather})

        if res.status_code != 200:
            print("Ошибка подключении к weather api")
            exit(0)

        data = res.json()
        for i in data['list']:
            bot.send_message(message.chat.id,
                             "Дата <" + i['dt_txt'] +

                             "> \r\nТемпература <" +
                             '{0:+3.0f}'.format(i['main']['temp']) +

                             "> \r\nПогодные условия <" +
                             i['weather'][0]['description'] +

                             "> \r\nСкорость ветра <" +
                             str(i['wind']['speed']) +
                             ">")
    else:
        bot.send_message(message.chat.id, "Команда не распознана")


bot.polling(none_stop=True, interval=0)
