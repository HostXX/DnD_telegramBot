from random import randint 
# D4, D6, D8, D10, D12, D20


def rollDice(bot, update):
    diceNumber = int(update.message.text[5:])
    result = randint(1, diceNumber)
    print (result)
    print (update.message.chat.first_name)
    
    username = update.message.chat.first_name
    bot.sendMessage(chat_id=update.message.chat_id, text = " You rolled " + str(result))


