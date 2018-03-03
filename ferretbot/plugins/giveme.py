from slackbot.bot import respond_to

@respond_to('(.*)ちょうだい')
def giveme(message, something):
    message.reply('{}あるよー'.format(something))
