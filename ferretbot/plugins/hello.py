from slackbot.bot import respond_to
from slackbot.bot import listen_to

@respond_to('こんにちは')
def hello(message):
    message.reply('こんにちはー')

@listen_to('おはよう')
def help(message):
    message.send('おはようございます')
