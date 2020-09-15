import time
import telepot
from pprint import pprint
from telepot.loop import MessageLoop

TOKEN = os.environ["TOKEN"]

bot = telepot.Bot(TOKEN)
pprint(bot.getMe())
def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if msg['text'] == '/food':
        bot.sendMessage(chat_id, 'hamburger')
    elif msg['text'] == '/drink':
        bot.sendMessage(chat_id, 'coke zero')
MessageLoop(bot, handle).run_as_thread()
while 1:
    time.sleep(10)