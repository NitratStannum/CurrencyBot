import telebot
import time
from config import TOKEN, curency_dict
from extensions import APIException, Convertor

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):

    start_text = 'Вас приветствует "Валютный конвертор"'
    help_text = '<b>Чтобы конвертировать валюты</b>, напишите мне сообщение в следующем формате:\n \
<i>*имя валюты, цену которой вы хотите узнать*</i> <i>*имя валюты, в которой надо узнать цену первой валюты*</i>\
<i>*количество первой валюты*</i>'

    bot.send_message(message.chat.id, start_text, parse_mode='html')
    time.sleep(1.0)
    bot.send_message(message.chat.id, help_text, parse_mode='html')


@bot.message_handler(commands=['help'])
def help_message(message):

    help_text = '<b>Чтобы конвертировать валюты</b>, напишите мне сообщение в следующем формате:\n \
<i>*имя валюты, цену которой вы хотите узнать*</i> <i>*имя валюты, в которой надо узнать цену первой валюты*</i>\
<i>*количество первой валюты*</i>'

    bot.send_message(message.chat.id, help_text, parse_mode='html')


@bot.message_handler(commands=['values'])
def valuta(message):

    valut_lst = ''

    for value in curency_dict.keys():
        valut_lst += f'{value}\n'

    valuta_text = f'<b>Список доступных валют</b>:\n{valut_lst}'

    bot.send_message(message.chat.id, valuta_text, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_currency(message):

    try:
        # преобразование введенного пользователем текста в список из строк
        values = message.text.lower().split(' ')

        if len(values) != 3:
            raise APIException(
                'Ошибка: проверьте количество введенных параметров')
        quote: str = values[0]  # конвертируемая валюта
        base: str = values[1]  # валюта, в которую переводим
        amount: str = values[-1]

        summ = Convertor.conv(quote, base, amount)

    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя !\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        finally_text = f'<u>Валюта:</u> {quote}\n\
<u>Переводим в</u>: {base}\n\
<u>Количество:</u> {amount}\n\
<u>Сумма:</u> {summ}'

    bot.send_message(message.chat.id, finally_text, parse_mode='html')


bot.infinity_polling()
