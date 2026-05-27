import telebot, os
import google.generativeai as genai

# Railway muhitidan kalitlarni olish
bot = telebot.TeleBot(os.environ['TELEGRAM_TOKEN'])
genai.configure(api_key=os.environ['GEMINI_API_KEY'])
model = genai.GenerativeModel('gemini-1.5-flash')

@bot.message_handler(content_types=['text', 'photo', 'voice'])
def handle_message(message):
    if message.text:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    elif message.photo:
        bot.reply_to(message, "Rasm qabul qilindi, tahlil qilyapman...")
    elif message.voice:
        bot.reply_to(message, "Ovozli xabarni qabul qildim.")

bot.infinity_polling()

