from snownlp import SnowNLP

def sentimentAnalysis(text):
    s = SnowNLP(text)
    sentimentScore = s.sentiments
    reply = ""
    if sentimentScore > 0.35:
        pass
    else:
        reply = "监测到负能量发言(Probability = %f)\n肃反委员会小助手提醒您，网络并非法外之地" %sentimentScore
    print("[LOG] sentimentScore = %f" %sentimentScore)
    return reply