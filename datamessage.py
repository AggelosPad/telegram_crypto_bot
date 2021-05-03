 
import json
import telegram
import sys

def notify_ending(message):
    token = 'XXXX'
    chat_id = 'XXXX'   
    bot = telegram.Bot(token=token)
    bot.sendMessage(chat_id=chat_id, text=message)


f = open('data_file.json')
data = json.load(f)

    
length = len(data)
for i in range(0,5):
    name = data.get('data')[i].get('name')
    
    user_input= sys.argv[1]
    if user_input == name:
        price = data.get('data')[i].get('quote').get('USD').get('price')
        percantage24 = data.get('data')[i].get('quote').get('USD').get('percent_change_24h')
        percantage1 = data.get('data')[i].get('quote').get('USD').get('percent_change_1h')
        message = str(str(name) + ' price: ' + str(price) + '\nLast hour: ' + str(percantage1) +'%'+'\nLast 24 hour: ' + str(percantage24) +'%')
        print(message)
        notify_ending(message)
        quit()
        


