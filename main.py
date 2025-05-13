from pyrogram import Client, filters
import asyncio

import random 
# Konfigurasi akunmu
api_id = 6973446  # Ganti dengan API ID kamu
api_hash = "d3a6dbd3e466159f7170f6af7fb35ac1"  # Ganti dengan API Hash kamu
session = "BQBqaAYAlRD7Is4yeAS34BC7tMiaPXfqJhhSgodk3cs4mz6n3bR1AfCsixwXlpmCbk1SSDYkXTwRCOG0EGHxge61v39OdazqjHG9SJ2shlaqc-faFIwn7_8cIQnrbPxCURUFEY65NjGdXR1nGWQ_f8o7uqS4nLQ9T0PLi8-uhP1Qb94qMnqpA9zMGl-TYDYspS4I2MLmIIjLDiXv4y4DaAtEMhry3B00BY36pvkbCtL9hd9bwYx1OknJAf_IqN-bLnEIucTIkfrG-2a3_LhCgXzJUonkKwUJQ-9BJT-YYDbNy5BRkgNDlsc4pl6ov2vn2V7PdygTL-axrMLRT_dP7Aj2Dy4_GwAAAAB1B3HOAA"

# ID atau username bot anonymous (contoh)
bot_username = "chatbot"

# ID stiker yang mau dikirim
sticker_id = "CAACAgUAAxkDAAEFHvtoDnfTve9yrixL5v76zLW61hg6kAACMRkAApGMcVR642NGfTJX-R4E"  # Ganti dengan file_id stikermu

app = Client("akak", api_id=api_id, api_hash=api_hash, session_string=session)

# State Tracking
chatting = False
current_chat = None
kata_kata = [
    "Gabung grup sifa dong,nanti ada yang spesial klik stiker diatas",
    "sifa punya grup,join ya klik stiker diatas",
    "temenin sifa ngobrol,klik stiker diatas",
]
@app.on_message(filters.bot & filters.chat(bot_username))
async def handle_messages(client, message):
    global chatting, current_chat

    # Cek kalau dapat pesan "Partner disconnected" (berarti lawan skip)
    if "😞" in message.text.lower() or "Your partner has stopped the chat" in message.text.lower():
        chatting = False
        await start_new_chat()

    # Cek kalau match dengan orang baru
    if "/next" in message.text.lower():
        chatting = True
        current_chat = message.chat.id
        katanya = random.choice(kata_kata)

        # Kirim stiker
        await asyncio.sleep(2)  # Biar natural
        await client.send_message(bot_username, "ce")
        await asyncio.sleep(1)
        await client.send_sticker(bot_username, "CAACAgUAAyEGAASTIE8vAAIBz2gjb5Yq3kb7-1eQ2HEbxwJd_kjlAAI7FQACAkh4VMu11jWyYQZ7HgQ")
        await client.send_message(bot_username, katanya)

        # Tunggu 10 detik, kalau belum di-skip, kita auto skip
        await asyncio.sleep(10)
        if chatting:
            await skip_chat()

async def start_new_chat():
    await asyncio.sleep(1)
    await app.send_message(bot_username, "🚀 Find a partner")  # Sesuaikan dengan tombol/bahasa bot-nya

async def skip_chat():
    global chatting
    chatting = False
    await app.send_message(bot_username, "/next")  # Sesuaikan dengan tombol/bahasa bot-nya
    await asyncio.sleep(3)
#    await start_new_chat()

@app.on_message(filters.sticker & filters.me)
async def start_command(client, message):
    await message.reply("Userbot Started!")
    await start_new_chat()

app.run()
