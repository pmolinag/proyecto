from fabric.api import *
import os

def descargar():
    run ('sudo rm -rf proyecto')
    run('sudo apt-get install -y python3-pip')
    run ('sudo git clone https://github.com/pmolinag/proyecto')

def iniciar():
    run ('cd ~/proyecto && sudo -E python3 ./FlyFinderBot/vuelos_rest.py',pty=False)


def borrar():
    run ('rm -rf proyecto')

def testear():
        run ('cd ~/proyecto &&  python3 ./FlyFinderBot/test_vuelos.py')

def instalar():
    run ('cd ~/proyecto && sudo pip3 install -r requirements.txt')

def recargar():
    run("sudo supervisorctl reload")
