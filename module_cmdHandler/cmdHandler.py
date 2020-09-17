from module_globalVar import globalVar
from module_musicDownload.musicDownload import *

def sentimentAnalysisStart(bot, update):
    globalVar.set_value("SENTIMENT_ANALYSIS", True)
    update.message.reply_text("情感分析 --> 启动")

def sentimentAnalysisStop(bot, update):
    globalVar.set_value("SENTIMENT_ANALYSIS", False)
    update.message.reply_text("情感分析 --> 关闭")

def sendMurmur(bot, update):
    update.message.reply_text("每天一粒，远离zz抑郁")

def fetchMusic(bot, update, args):
    # update.message.reply_text(getYtbMusicUrl(args), parse_mode='MarkdownV2')
    if args:
        update.message.reply_text(getYtbMusicUrl(args))
    else:
        update.message.reply_text("Give me some hints, Plz")
