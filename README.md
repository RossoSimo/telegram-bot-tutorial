# telegram-bot-tutorial

## Dispensa corso telegrame e bot telegram in python:
Il corso è diviso in:
- [Tutorial generale Python](./Tutorial_Python/README.md), un tutorial per imparare le basi di Python.
- [Tutorial bot telegram](./Tutorial_BotTelegram/README.md), un tutorial per creare un bot telegram con Python e la libreria telepot.


## Introduzione:
- [Introduzione Python](#Introduzione-Python)
- [Telegram bot](#Telegram-bot)
    - [Creare il proprio bot](#Creare-il-proprio-bot)
    - [Installazione requisiti](#Installazione-requisiti)
        - [Installazione Python](#Installazione-Python)
        - [Installazione telepot](#Installazione-telepot)
- [Documentazione](#Documentazione)

# Introduzione Python

Potete trovare una veloce guida all'utilizzo di python [qui](Tutorial_Python/README.md).

# Telegram bot

## Creare il proprio bot

## Installazione requisiti

Per poter dar vita al nostro bot abbiamo bisogno di scrivere del codice che caratterizzerà la sua funzionalità, e per farlo
avremo bisogno di **configurare** la macchina dove il codice verrà eseguito.

### Installazione Python

Prima di tutto bisogna installare **python**, ovvero il linguaggio di programmazione con cui andremo ad affrontare il tutto.
Per farlo basta seguire i passaggi indicati qui sotto:

Per controllare se è già presente una versione di python3 all'interno del nostro computer, aprire una finestra del terminale e inserire:
```
python --version
```
In caso sia già installato, verificare che la versione sia **Python 3.5 o superiore**. In caso contrario segui i passaggi qui sotto.

Su **Windows** basterà recarsi sul [sito ufficiale](https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe) ed installare una versione **valida** di python.

**N.B.** Durante l'installazione assicurarsi di aggiungere al `PATH`.

Su una distribuzione **Linux** basata su Debian come **Ubuntu** bisognerà eseguire i seguenti comandi all'interno del terminale:
```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3
```

### Installazione telepot

Telepot sarà la **libreria** che utilizzeremo per la creazione del nostro bot.
Per installarla dobbiamo usufruire del `pip`, ovvero il packet manager usato da python.

Prima di tutto verifichiamo se `pip` è presente nel nostro computer:

Quindi nel termianle digitiamo:
```
pip --version
```
Se non riceviamo risposta possiamo provare con `pip3` al posto di `pip`.
In caso non funzionasse neanche ora seguire i passaggi qui sotto:

Su **Windows** se si è già [installato python](#Installare-Python) bisogna [aggiungerlo alle variabile d'ambiente](https://www.tecnobabele.com/come-aggiungere-python-alla-variabile-path-di-windows/2020-10-14/), ovvero `PATH`.

Su **Ubuntu** bisognerà digitare su terminale:
```
sudo apt-get update
sudo apt install python3-pip
```

Quindi verificare nuovamente l'installazione.

Installiamo dunque **telepot** con:
```
pip3 install telepot
pip3 install telepot --upgrade
```
Se non riceviamo risposta possiamo provare con `pip` al posto di `pip3`.

# Documentazione

[Telegram Bot API](https://core.telegram.org/api)

[Telepot](https://telepot.readthedocs.io/en/latest/reference.html)

>>>>>>> dfdc59a5b2c5b73aa467cd753b78ead018848eef
