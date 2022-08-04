from pyrogram import Client, filters
from pyrogram.types import Message
import os
from Database import *

API_ID = int(os.environ['API_ID'])
API_HASH = os.environ['API_HASH']
MONGO_DB_URL = os.environ['MONGO_DB_URL']
PATH = os.environ['DATABASE_PATH']
TOKEN1 = os.environ['TOKEN1']
TOKEN2 = os.environ['TOKEN2']
TOKEN3 = os.environ['TOKEN3']
TOKEN4 = os.environ['TOKEN4']
TOKEN5 = os.environ['TOKEN5']
SUDO = os.environ['SUDO_USERS'].split()
if len(SUDO) > 1:
    SUDOS = []
    for sudo in SUDO:
        SUDOS.append(int(sudo))
else:
    SUDOS = int(SUDO)



if TOKEN1:
    END1 = Client(":END1:", API_ID, API_HASH, TOKEN1)
if TOKEN2:
    END1 = Client(":END2:", API_ID, API_HASH, TOKEN2)
if TOKEN3:
    END1 = Client(":END3:", API_ID, API_HASH, TOKEN3)
if TOKEN4:
    END1 = Client(":END4:", API_ID, API_HASH, TOKEN4)
if TOKEN5:
    END1 = Client(":END5:", API_ID, API_HASH, TOKEN5)


        
        
        
        
    
