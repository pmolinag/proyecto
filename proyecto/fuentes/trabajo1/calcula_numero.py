import os, time, sys, hashlib, logging
from random import randint
pipe_name = 'so_4'

palabra_enviar = "nada"
palabra_encriptada = "nada"
mensaje = "nada"
grupo = "grupo_4:"
esta2 = False

def selectWordUpper(dic, doUppercase):
    word=dic
    w = list(dic)
    for i in range(randint(0, len(w))):
        pos = randint(0, len(w) - 1)
        w[pos] = w[pos].upper()

    if doUppercase:
        word = "".join(w)

    return word

def comprobar(encrypt, dic):
    i = 0
    word = ""
    esta = False
    word2 = ""
    while i < 500 and esta == False:
        word = selectWordUpper(dic, True)
        word = encryptWord(word)
        if word == encrypt:
            esta = True
            print("ENCONTRADO")
            word2 = word
        i = i + 1

    return word2

def encryptWord(word):
        md5 = hashlib.md5()
        my_bytes = str.encode(word)
        type(my_bytes)
        md5.update(my_bytes)
        res = md5.hexdigest()
        # encrypt = hashlib.md5(word).hexdigest()
        return res

def child( ):
    global line
    logging.info('CHILD::Se va a abrir comunicacion con el pipe so_4 para escribir una palabra de ejemplo, en este caso rosie, pero se podria cambiar por la que fuera')
    pipeout = os.open(pipe_name, os.O_WRONLY)
    palabra_clave = "rosIE"
    os.write(pipeout, palabra_clave.encode())
    os.close(pipeout)
    logging.info('CHILD::Palabra escrita correctamente, y se ha cerrado la conexion con el pipe so_4')

def parent( ):
    global line
    logging.info('PARENT::Se va a proceder a abrir conexion con el pipe so_4 y a leer la palabra encriptada que contiene')
    pipein = open(pipe_name, 'r')
    line = pipein.read()
    pipein.close()
    logging.info('PARENT::Palabra leida correctamente, se ha cerrado la conexion con el pipe so_4')
    encrypt = encryptWord(line)
    Archivo_Palabras = open("dicionario.txt", "r")
    Palabras1 = Archivo_Palabras.read()
    Archivo_Palabras.close()
    Palabras = Palabras1.splitlines()
    i = 0
    global esta2
    global palabra_enviar
    global palabra_encriptada
    global mensaje
    logging.info('PARENT::Se comienza la busqueda por el diccionario.')
    print("Buscando...")
    while i < len(Palabras) and esta2 == False:
        encrypt2 = comprobar(encrypt, Palabras[i])
        if encrypt == encrypt2:
            esta2 = True
            palabra_enviar = Palabras[i]
            palabra_encriptada = encrypt2
            mensaje = grupo + palabra_enviar + ":" + palabra_encriptada
            logging.info('PARENT::Ya se ha encontrado la palabra¡')
        i = i + 1

def getMensaje():
    return mensaje

""" Create named pipe """
if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)

""" Create logs """
fichero_log = os.path.join(os.getcwd(), 'busqueda_palabra.log')

print('Archivo Log en ', fichero_log)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s : %(message)s',
                    filename = fichero_log,
                    filemode = 'w',)

""" Create child """
pid = os.fork()
if pid != 0:
    parent()
else:
    child()
