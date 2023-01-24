import telebot, wikipedia, re
# импор библиотеки и подключения токен бота
bot = telebot.TeleBot('ваш токен')
wikipedia.set_lang("ru")
# Метод для получения текстовых сообщений

def get_wiki(request):
    try:
        ny = wikipedia.page(request)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext_second = ''
        for x in wikimas:
            if not ('==' in x):
                if (len((x.strip())) > 3):
                    wikitext_second = wikitext_second + x + '.'
                else:
                    break

        wikitext_second = re.sub('\([^()]*\)', '', wikitext_second)
        wikitext_second = re.sub('\([^()]*\)', '', wikitext_second)
        wikitext_second = re.sub('\{[^\{\}]*\}', '', wikitext_second)

        return wikitext_second
    except Exception as e:
        return "В энциклопедии нет информации об этом"


@bot.message_handler(commands=["start"])
def start(message, res=False):
    bot.send_message(message.chat.id, 'Отправь мне любое слово, и я найду его значение!')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, get_wiki(message.text))

bot.polling(none_stop=True, interval=0)
