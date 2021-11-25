import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "1987567608:AAHER8qfBeqMONykRMqkBYmLJ1IuwBWX_3Y"

def handle(msg):    #Funzione richiamata nel momento in cui gli si invia un messaggio
    content_type, chat_type, chat_id = telepot.glance(msg)
    testo = msg['text'] #Assegnamo alla variabile testo il testo del messaggio inviato
    username = msg['from']['username']  #Assegnamo alla variabile username l'username dell'utente che invia il messaggio
    if testo == '/start':
        keyboard =InlineKeyboardMarkup(inline_keyboard=[
                   [InlineKeyboardButton(text='Press me', callback_data='press')],
               ])
        bot.sendMessage(chat_id, "Benvenuto nel bot!", reply_markup=keyboard)
    else:
        bot.sendMessage(chat_id, "Non capisco")

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

    bot.answerCallbackQuery(query_id, text='Got it')

bot = telepot.Bot(TOKEN)    #Creiamo l'oggetto bot, con il nostro token precedentemente dichiarato
MessageLoop(bot, {'chat': handle,
                  'callback_query': on_callback_query}).run_as_thread()    #Mettiamo il bot in ascolto dei messaggi o delle azioni nella tastiera in arrivo
print('Listening ...')

while 1: #Manteniamo il programma in esecuzione
    time.sleep(10)