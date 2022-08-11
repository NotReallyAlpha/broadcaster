from pyrogram import Client, filters, idle
from pyrogram.types import Message
import os
from Database.client import *

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

async def broadcast(_, message):
    if message.reply_to_message:
        x = message.reply_to_message.message_id
        y = message.chat.id
    else:
        if len(message.command) < 2:
            return await message.reply_text(
                "**Usage**:\n/broadcast [MESSAGE] or [Reply to a Message]"
            )
        query = message.text.split(None, 1)[1]
    sent = 0
    pinned = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            if message.reply_to_message:
                ok = await _.forward_messages(i, y, x)
                sent += 1
                if message.text.split()[0][1] == "p":
                    try:
                        await _.pin_chat_message(i, ok.message_id)
                        pinned += 1
                    except:
                        continue 
            else:
                ok = await _.send_message(i, query)
                sent += 1
                if message.text.split()[0][1] == "p":
                    try:
                        await _.pin_chat_message(i, ok.message_id)
                        pinned += 1
                    except:
                        continue
        except FloodWait as e:
            flood_time = int(e.x)
            if flood_time > 200:
                continue
            await asyncio.sleep(flood_time)
        except Exception:
            continue
    try:
        await message.reply_text(
            f"**Broadcasted Message In {sent} Chats and pinned in {str(pinned)} Chats**"
        )
    except:
        pass


if TOKEN1:
    END1 = Client(":END1:", API_ID, API_HASH, TOKEN1)
if TOKEN2:
    END2 = Client(":END2:", API_ID, API_HASH, TOKEN2)
if TOKEN3:
    END3 = Client(":END3:", API_ID, API_HASH, TOKEN3)
if TOKEN4:
    END4 = Client(":END4:", API_ID, API_HASH, TOKEN4)
if TOKEN5:
    END5 = Client(":END5:", API_ID, API_HASH, TOKEN5)

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
    
        
END1.start()
ME1 = END1.get_me()
UN1 = ME1.username
END2.start()
ME2 = END2.get_me()
UN2 = ME2.username
END3.start()
ME3 = END3.get_me()
UN3 = ME3.username
END4.start()
ME4 = END4.get_me()
UN4 = ME4.username
END5.start() 
ME5 = END5.get_me()
UN5 = ME5.username
idle()
