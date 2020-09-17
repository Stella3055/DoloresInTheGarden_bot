import telegram
from flask import Flask, request
from telegram.ext import Dispatcher, MessageHandler, Filters, CommandHandler
import os

from module_globalVar import globalVar
globalVar._init()

from module_nlp.snowNLP import *
from module_cmdHandler.cmdHandler import *

TOKEN = os.environ["TOKEN"]
PORT = int(os.environ.get('PORT', '5000'))

globalVar.set_value("SENTIMENT_ANALYSIS", True)

bot = telegram.Bot(token=TOKEN)
app = Flask(__name__)

@app.route('/hook', methods=['POST'])
def webhook_handler():
    """Set route /hook with POST method will trigger this method."""
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        # Update dispatcher process that handler to process this message
        dispatcher.process_update(update)
    return 'ok'

def reply_handler(bot, update):
    """Reply message."""
    text = update.message.text
    user_id = update.message.from_user.id
    if globalVar.get_value("SENTIMENT_ANALYSIS", True):
        textSenti = sentimentAnalysis(text)
        if textSenti:
            update.message.reply_text(textSenti)
    else:
        update.message.reply_text(text)

# New a dispatcher for bot
dispatcher = Dispatcher(bot, None)

# Add handler for handling message, there are many kinds of message. For this handler, it particular handle text
# message.
dispatcher.add_handler(CommandHandler("sentiment_analysis_start", sentimentAnalysisStart))
dispatcher.add_handler(CommandHandler("sentiment_analysis_stop", sentimentAnalysisStop))
dispatcher.add_handler(CommandHandler("murmur", sendMurmur))
dispatcher.add_handler(CommandHandler("fetch_music", fetchMusic, pass_args=True))
dispatcher.add_handler(MessageHandler(Filters.text, reply_handler))

if __name__ == "__main__":
    # Running server
    app.run(port = PORT, host='0.0.0.0')