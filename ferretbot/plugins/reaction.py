from slackbot.bot import listen_to

@listen_to('カレー')
def curry(message):
    """カレーの絵文字でリアクションする"""
    message.react('curry')


@listen_to('ビール')
def beer(message):
    """ビルの絵文字でリアクションする"""
    message.react('beer')
