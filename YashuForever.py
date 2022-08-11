from pyrogram import Client
from pyrogram.types import Message
from Database.client import get_served_chats

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
