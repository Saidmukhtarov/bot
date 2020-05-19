import telebot

bot = telebot.TeleBot('1078355228:AAEqHPap1GSR_Y1ygrKIqgWnoaFtuQqIwnU')


keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Salom', 'Hayr', 'Katalog', 'Uylar')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Assalomu alaykum Siz hozir @Saidmukhtarov_Official tomonidan yozilgan Botni ishga tushirdingiz', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'salom':
        bot.send_message(message.chat.id, 'Assalomu alaykum men 04.05.2020 yilda yozilgan kod bo`yicha ishlovchi chat botman')
    elif message.text.lower() == 'hayr':
        bot.send_message(message.chat.id, 'Yana kelasiz degan umiddaman')
    elif message.text.lower() == 'katalog':
        bot.send_photo(message.chat.id, 'https://i.pinimg.com/originals/7b/c2/3f/7bc23f0632e1915ea5e6085e3e715f6d.jpg')
        bot.send_message(message.chat.id, 'Narxi: 1 000 000 so`m')
        bot.send_photo(message.chat.id, 'https://www.windowscanada.com/media/fbimages/Top_10_Window_Designs_in_2018.jpg')
        bot.send_message(message.chat.id, 'Narxi: 1 500 000 so`m')

    elif message.text.lower() == 'uylar':
        bot.send_photo(message.chat.id, 'https://lh3.googleusercontent.com/proxy/ni1u0jVhGJrr7lcWT0JoLpNnWze5tuM4Rt3g8jhLADobSjjmP8tSTTBs2J5MDfxOQ7lFxQK7WNn1ayaVk51NMFI1_bXJUlalK2aQWLzNBzkVeIj76gvad-2VtZYW1o6NlHLtTQzV15uFX-JWsmCwu9rEfB1Qb-pM8STerejEsV0BlPLRv4SgyRBS5awvHp2p8PLmVqBf3HdqtFhs0F1gGI4')
        bot.send_message(message.chat.id, 'Narxi: 70 000$')
        bot.send_photo(message.chat.id, 'https://www.makemyhouse.com/actual/1521719392_682.jpg?design')
        bot.send_message(message.chat.id, 'Narxi: 150 000$')
    else:
        bot.send_message(message.chat.id, 'Qo`shimcha ma`lumot uchun @Saidmukhtarov_Official ga murojaat qilishingiz mumkin')

bot.polling()