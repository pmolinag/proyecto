import threading, os, hashlib, signal, sys, multiprocessing
from random import randint

pal = "nada"
pipe_name = "so_4"
pipe_name_env = "so_server"
encontrado = False
mensaje = "nada"




def mostrar_palabras(signal, frame):
    global lista, lista1, lista2
    i = 0
    j = 0
    k = 0
    while i < len(lista):
        print("GENERAL: " + lista[i])
        i = i + 1
    while j < len(lista1):
        print("Thread numero 1: " + lista1[j])
        j = j + 1
    while k < len(lista2):
        print("Thread numero 2: " + lista2[k])
        k = k + 1

def method_exits(signum, frame):
    print("Programa cerrado.")
    exit()


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

def buscar():
    global mensaje, encontrado
    encrypt2 = "nada"
    palabra_enviar = "nada"
    palabra_encriptada = "nada"
    grupo = "grupo_4:"
    lista = []
    lista1 = []
    lista2 = []
    encrypt = encryptWord(line)
    Archivo_Palabras = open("dicionario.txt", "r")
    Palabras1 = Archivo_Palabras.read()
    Archivo_Palabras.close()
    Palabras = Palabras1.splitlines()
    i = 0
    print("Thread con nombre " + threading.currentThread().getName() + " se encuentra buscando...")
    while i < len(Palabras) and encontrado == False:
        lista.append(Palabras[i])
        if threading.currentThread().getName() == "thread_busqueda" and (i%2) == 1:
            lista1.append(Palabras[i])
            encrypt2 = comprobar(encrypt, Palabras[i])
        elif threading.currentThread().getName() == "thread_busqueda2" and (i%2) == 0:
            lista2.append(Palabras[i])
            encrypt2 = comprobar(encrypt, Palabras[i])
        if encrypt == encrypt2:
            encontrado = True
            palabra_enviar = Palabras[i]
            palabra_encriptada = encrypt2
            mensaje = grupo + palabra_enviar + ":" + palabra_encriptada
        i = i + 1
    return mensaje

def thread_busqueda():
    global pal
    evento.wait()
    pal = buscar()
    if(pal != "nada"):
        evento2.set()
def inicializar():
    pipeout = os.open(pipe_name, os.O_WRONLY)
    palabra_clave = "ROSie"
    os.write(pipeout, palabra_clave.encode())
    os.close(pipeout)

def thread_control():

    global line, pal
    pipein = open(pipe_name, 'r')
    line = pipein.readline()
    pipein.close()
    evento.set()
    evento2.wait()
    evento3.set()
    pipeenv = os.open(pipe_name_env, os.O_WRONLY)
    os.write(pipeenv, mensaje.encode())
    os.close(pipeenv)

def muestra():
    evento3.wait()
    pipeenv = open(pipe_name_env, 'r')
    line = pipeenv.readline()
    print(line)
    pipeenv.close()

if not os.path.exists(pipe_name_env):
    os.mkfifo(pipe_name_env)
if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)

lock = threading.Lock()
evento = threading.Event()
evento2 = threading.Event()
evento3 = threading.Event()

t = threading.Thread(target=inicializar, name="inicializar")
t2 = threading.Thread(target=thread_control, name="thread_control")
t3 = threading.Thread(target=thread_busqueda, name="thread_busqueda")
t4 = threading.Thread(target=thread_busqueda, name="thread_busqueda2")
t5 = threading.Thread(target=muestra, name="mostrar")
t.start()
t2.start()
t3.start()
t4.start()
t5.start()

# Ctrl+C
signal.signal(signal.SIGINT, method_exits)
# Ctrl+Z
signal.signal(signal.SIGTSTP, mostrar_palabras)
