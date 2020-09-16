from snownlp import SnowNLP

def sentimentAnalysis(update, context):
    text = update.message.text
    s = SnowNLP(text)
    sentimentScore = s.sentiments
    reply = ""
    if sentimentScore > 0.5:
        reply = "经分析，您的发言包含积极情绪的概率为 %f\n今天也是充满正能量的一天" %sentimentScore
    else:
        reply = "经分析，您的发言包含积极情绪的概率为 %f\nчрезвычайная комиссия提醒您，网络并非法外之地" %sentimentScore
    update.message.reply_text(reply)