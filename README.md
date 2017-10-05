## Proyecto

[Site](https://pmolinag.github.io/proyecto/)

El proyecto es un bot en telegram, implementado principalmente en python, el cual será un buscador de los vuelos más baratos disponibles entre las paginas web de viaje más conocidas, desde la ciudad que el usuario introduzca hasta otra ciudad destino.

Para ello, voy a utilizar:

- Lenguaje principal: python
- Sistema de gestión de nube: Azure
- API de telegram(telebot para python)
- La gestión de la base de datos la haré con MySQL

## REQUISITOS
Instalamos una libreria que nos ayudara a recoger datos de las webs de vuelos:
- sudo apt-get install python-bs4 o pip install beautifulsoup4

Tambien instalaremos la libreria request para poder descargarnos paginas web enteras, para luego poder recoger sus datos.

- pip install requests

Y, por supuesto, tener instalado Python
- sudo apt-get install python

Tambien instalamos la API que nos va a facilitar el desarrollo del bot para Telegram:

- git clone https://github.com/eternnoir/pyTelegramBotAPI.git
- cd pyTelegramBotAPI
- sudo python setup.py install

O con pip:

- sudo pip install pyTelegramBotAPI

y seguimos estas instrucciones necesarias para que nos den nuestro token particular, para poder trabajar con el a lo largo del desarrollo del bot.

Para poder utilizar esta API, primero vamos a tener que regristar nuestro bot y disponer del token que nos proporciona el bot llamado The BotFather. Es muy simple, únicamente hay que abrir conversación desde Telegram con @BotFather y seguir los pasos: una vez tenemos abierto chat con @botfather, enviamos el siguiente mensaje para crear nuestro bot: /newbot y The BotFather nos preguntará por el nombre de nuestro bot (nombre que será visible) y el nombre de usuario (un nombre corto entre 5-32 caracteres y que debe acabar con la palabra bot).
Con todo esto The BotFather nos contestará con un string que será nuestro TOKEN y utilizaremos en nuestra programación Python para identificarnos.
