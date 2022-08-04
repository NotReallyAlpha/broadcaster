from pyrogram import Client, filters
from pyrogram.types import Message
import os
from Database import *
from YashuForever import broadcast

API_ID = int(os.environ['API_ID'])
API_HASH = os.environ['API_HASH']
MONGO_DB_URL = os.environ['MONGO_DB_URL']
CH = os.environ['COMMAND_HANDLER']
TOKEN1 = os.environ['TOKEN1']
TOKEN2 = os.environ['TOKEN2']
TOKEN3 = os.environ['TOKEN3']
TOKEN4 = os.environ['TOKEN4']
TOKEN5 = os.environ['TOKEN5']
SUDO = os.environ['SUDO_USERS'].split()
if SUDO:
    SUDOS = []
    for sudo in SUDO:
        SUDOS.append(int(sudo))




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

@END1.on_message(group=1)
async def cwf1(_, m):
    if m.chat.type == "private":
        return
    s = await is_served_chat(m.chat.id)
    if not s:
        await add_served_chat(m.chat.id)

@END2.on_message(group=1)
async def cwf2(_, m):
    if m.chat.type == "private":
        return
    s = await is_served_chat(m.chat.id)
    if not s:
        await add_served_chat(m.chat.id)

@END3.on_message(group=1)
async def cwf3(_, m):
    if m.chat.type == "private":
        return
    s = await is_served_chat(m.chat.id)
    if not s:
        await add_served_chat(m.chat.id)

@END4.on_message(group=1)
async def cwf4(_, m):
    if m.chat.type == "private":
        return
    s = await is_served_chat(m.chat.id)
    if not s:
        await add_served_chat(m.chat.id)

@END5.on_message(group=1)
async def cwf5(_, m):
    if m.chat.type == "private":
        return
    s = await is_served_chat(m.chat.id)
    if not s:
        await add_served_chat(m.chat.id)




@END1.on_message(filters.command(["broadcast", "pbroadcast"], CH) & filters.group & filters.user(SUDOS))
async def gc1(_, message):
    await broadcast(_, message)    

@END2.on_message(filters.command(["broadcast", "pbroadcast"], CH) & filters.group & filters.user(SUDOS))
async def gc2(_, message):
    await broadcast(_, message)

@END3.on_message(filters.command(["broadcast", "pbroadcast"], CH) & filters.group & filters.user(SUDOS))
async def gc3(_, message):
    await broadcast(_, message)

@END4.on_message(filters.command(["broadcast", "pbroadcast"], CH) & filters.group & filters.user(SUDOS))
async def gc4(_, message):
    await broadcast(_, message)

@END5.on_message(filters.command(["broadcast", "pbroadcast"], CH) & filters.group & filters.user(SUDOS))
async def gc5(_, message):
    await broadcast(_, message)
    
        
END1.run()
END2.run()
END3.run()
END4.run()
END5.run() 
