import os, time, sys, calcula_numero, logging
pipe_name_env = 'so_server'

def child( ):
    logging.debug('Comienza el programa')
    pipeout = os.open(pipe_name_env, os.O_WRONLY)
    logging.info('Ya se ha abierto comunicacion con el pipe so_server')
    logging.info('Se va a proceder a buscar el numero')
    mensaje = calcula_numero.getMensaje()
    logging.info('Mensaje con la palabra clave, la palabra encriptada y el numero de grupo recibido y calculado correctamente.')
    if(mensaje != "nada"):
        os.write(pipeout, mensaje.encode())
        logging.info('Mensaje escrito correctemente en el pipe so_server.')

    os.close(pipeout)

def parent( ):
    logging.info('Se va a proceder a mostrar por pantalla el mensaje escrito para comprobar que esta bien.')
    pipein = open(pipe_name_env, 'r')
    line = pipein.readline()
    print (line)
    pipein.close()
    logging.info('Mensaje mostrado.')

""" Create named pipe """
if not os.path.exists(pipe_name_env):
    os.mkfifo(pipe_name_env)

""" Create child """
pid = os.fork()
if pid != 0:
    parent()
else:
    child()
