def sentimentAnalysisStart(update, context):
    SENTIMENT_ANALYSIS = True
    update.message.reply_text('''
    情感分析 --> 启动
    ''')

def sentimentAnalysisStop(update, context):
    SENTIMENT_ANALYSIS = False
    update.message.reply_text('''
    情感分析 --> 关闭
    ''')