# Tutorial Bot telegram in Python

## [Primo esempio](Example\echo_bot.py):
Questo bot ripeterá il messaggio che gli si invia, se il messaggio é di tipo testo.
```python
import time
import telepot
from telepot.loop import MessageLoop

TOKEN = "INSERISCI IL TOKEN"

def handle(msg):    #Funzione richiamata nel momento in cui gli si invia un messaggio
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type) #Tipo del massaggio  inviato
    print(chat_type)    #Tipo di chat che ha inviato il messaggio (privata,gruppi,...)
    print(chat_id)      #Id della chat che ha inviato il messaggio
    testo = msg['text'] #Assegnamo alla variabile testo il testo del messaggio inviato
    if content_type == 'text':
        bot.sendMessage(chat_id, testo)   #inviamo il messaggio con il testo che ci é stato inviato, alla chat che ce lo ha inviato

bot = telepot.Bot(TOKEN)    #Creiamo l'oggetto bot, con il nostro token precedentemente dichiarato
MessageLoop(bot, handle).run_as_thread()    #Mettiamo il bot in ascolto dei messaggi in arrivo
print('Listening ...')

while 1: #Manteniamo il programma in esecuzione
    time.sleep(10)
```

## [Secondo esempio](Example\chat_bot.py):
```python
import time
import telepot
from telepot.loop import MessageLoop

TOKEN = "INSERISCI IL TOKEN"

def handle(msg):    #Funzione richiamata nel momento in cui gli si invia un messaggio
    content_type, chat_type, chat_id = telepot.glance(msg)
    testo = msg['text'] #Assegnamo alla variabile testo il testo del messaggio inviato
    username = msg['from']['username']  #Assegnamo alla variabile username l'username dell'utente che invia il messaggio
    if testo == '/start':
        bot.sendMessage(chat_id, "Benvenuto nel bot!")
    elif testo == 'Ciao' or testo == 'ciao':
        bot.sendMessage(chat_id, f"Ciao {username}")    #inviamo il messaggio Ciao con l'username dell'utente
    elif testo == 'Come stai?':
        bot.sendMessage(chat_id, "Bene, tu?")
    elif testo == 'Bene':
        bot.sendMessage(chat_id, "Bene!")
    else:
        bot.sendMessage(chat_id, "Non capisco")

bot = telepot.Bot(TOKEN)    #Creiamo l'oggetto bot, con il nostro token precedentemente dichiarato
MessageLoop(bot, handle).run_as_thread()    #Mettiamo il bot in ascolto dei messaggi in arrivo
print('Listening ...')

while 1: #Manteniamo il programma in esecuzione
    time.sleep(10)
```

## [Terzo esempio](Example/simpleKeyboard_bot.py):
Crea una tastiera a schermo dove poter scegliere varie opzioni.
```python
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
 
from pprint import pprint
import time
import datetime
import json
from urllib.request import urlopen
 

TOKEN="INSERISCI TOKEN QUI" # da cambiare
 
def on_chat_message(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)
 
	keyboard = InlineKeyboardMarkup(inline_keyboard=[
                     [InlineKeyboardButton(text='IP', callback_data='ip'),
                     InlineKeyboardButton(text='Info', callback_data='info')],
                     [InlineKeyboardButton(text='Time', callback_data='time')],
                 ])
	bot.sendMessage(chat_id, 'Usa la tastiera qui sotto', reply_markup=keyboard)
 
 
def on_callback_query(msg):
	query_id, chat_id, query_data = telepot.glance(msg, flavor='callback_query')
	print('Callback Query:', query_id, chat_id, query_data)
	if query_data=='ip': # Fa una richiesta web per ricavare l'ip
		my_ip = urlopen('http://ip.42.pl/raw').read()
		bot.sendMessage(chat_id, my_ip)
	elif query_data=='info': # invia info del utente
		info=json.dumps(bot.getUpdates(),sort_keys=True, indent=4)
		bot.sendMessage(chat_id, info)
	elif query_data=='time': # Invia il tempo
		ts = time.time()
		bot.answerCallbackQuery(query_id, text=datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')) #messaggio a comparsa
 
 
bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
				  'callback_query': on_callback_query}).run_as_thread() 
print('Listening ...')
 
 
while 1:
	time.sleep(10)
```