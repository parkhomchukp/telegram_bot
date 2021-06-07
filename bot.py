import telebot
import time
import schedule

TOKEN = '1507550266:AAF-xfqoY1DS2b36ATmy1GhmVhqwYUNfAv0'  # enter token of your bot under parentheses
bot = telebot.TeleBot(TOKEN)
current_message = ''  # enter message under parentheses
ChatID = '-495877451'  # enter chat ID under parentheses
sending_message_time = ''  # enter time under parentheses


def msg(message):
    bot.send_message(ChatID, message)


schedule.every().day.at(sending_message_time).do(msg, current_message)
while True:
    schedule.run_pending()
    time.sleep(1)
