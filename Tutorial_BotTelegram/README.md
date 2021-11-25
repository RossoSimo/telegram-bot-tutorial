# Tutorial Bot telegram in Python
## Primo esempio:
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

## Secondo esempio:
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