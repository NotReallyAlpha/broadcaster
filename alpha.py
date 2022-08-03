from pyrogram import Client, filters
from pyrogram.types import Message
import os

API_ID = int(os.environ['API_ID'])
API_HASH = os.environ['API_HASH']
PATH = os.environ['DATABASE_PATH']
TOKEN = os.environ['TOKEN']
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


if TOKEN:
    END = Client(":END:", API_ID, API_HASH, TOKEN)
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

@END.on_message(filters.command(["broadcast", "pbroadcast"]) & filters.private & filters.user(SUDOS) & ~filters.edited)
async def broadcaster(_, m):
    reply = m.reply_to_message:
    if m.reply_to_message:
        x = m.reply_to_message.message_id
        y = m.chat.id
    else:
        if len(m.command) < 2:
            return await m.reply_text(
                "**Usage**:\n/broadcast [MESSAGE] or [Reply to a Message]"
            )
        query = m.text.split(None, 1)[1]
        chat_list = await _.ask(m.from_user.id, "Enter chats as [-123 -234 -345]", filters.text)
        for chat in chat_list:
            chat = int(chat)
            
        
    
