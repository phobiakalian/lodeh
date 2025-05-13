from pyrogram import Client, filters
import asyncio
import random

# Konfigurasi akunmu
api_id = 6973446
api_hash = "d3a6dbd3e466159f7170f6af7fb35ac1"
session = "BQBqaAYAlRD7Is4yeAS34BC7tMiaPXfqJhhSgodk3cs4mz6n3bR1AfCsixwXlpmCbk1SSDYkXTwRCOG0EGHxge61v39OdazqjHG9SJ2shlaqc-faFIwn7_8cIQnrbPxCURUFEY65NjGdXR1nGWQ_f8o7uqS4nLQ9T0PLi8-uhP1Qb94qMnqpA9zMGl-TYDYspS4I2MLmIIjLDiXv4y4DaAtEMhry3B00BY36pvkbCtL9hd9bwYx1OknJAf_IqN-bLnEIucTIkfrG-2a3_LhCgXzJUonkKwUJQ-9BJT-YYDbNy5BRkgNDlsc4pl6ov2vn2V7PdygTL-axrMLRT_dP7Aj2Dy4_GwAAAAB1B3HOAA"

bot_username = "chatbot"
sticker_id = "CAACAgUAAyEGAASTIE8vAAIBz2gjb5Yq3kb7-1eQ2HEbxwJd_kjlAAI7FQACAkh4VMu11jWyYQZ7HgQ"

kata_kata = [
    "Gabung grup sifa dong, nanti ada yang spesial klik stiker di atas!",
    "Sifa punya grup, join ya! Klik stiker di atas.",
    "Temenin Sifa ngobrol, klik stiker di atas!",
    "Gabung grup Sifa yuk! Banyak kejutan seru nunggu kamu~ 😚 Klik stikernya ya!",
    "Kamu keliatan asik, join grup Sifa deh... siapa tau jodoh di sana 😜",
    "Ngerasa kesepian? Grup Sifa siap nemenin kamu tiap hari! 🫶 Klik stiker di atas!",
    "Ayo ngobrol lebih seru bareng Sifa dan teman-teman lainnya 💬✨ Klik stikernya yuk!",
    "Grup Sifa lagi rame banget, dan kamu harus ada di sana! 😍 Klik stiker di atas ya!",
    "Pengen ngobrol bebas tanpa judge? Sifa punya tempatnya 😏 Klik stikernya!",
    "Daripada scroll doang, join grup Sifa yuk! Siapa tau nemu yang nyantol 💘",
    "Sstt... grup Sifa punya sesuatu yang kamu cari 😳 Klik stikernya dan cari tahu~",
    "Cuma orang spesial yang bisa gabung ke grup ini. Kamu salah satunya? 😇 Klik stiker!",
    "Jangan cuma diam dong... gabung grup Sifa dan rasain keseruannya 💥"
]

app = Client("akak", api_id=api_id, api_hash=api_hash, session_string=session)

chatting = False
current_chat = None

@app.on_message(filters.bot & filters.chat(bot_username))
async def handle_messages(client, message):
    global chatting, current_chat

    if not message.text:
        return  # Jangan proses kalau pesan tidak ada teksnya

    text = message.text.lower()

    # Deteksi chat berakhir
    if "😞" in text or "your partner has stopped the chat" in text:
        chatting = False
        print("Partner disconnected. Mulai cari baru...")
        await start_new_chat()

    # Deteksi match baru
    elif "/next" in text and not chatting:
        chatting = True
        current_chat = message.chat.id

        # Pilih salah satu kata secara acak
        katanya = random.choice(kata_kata)

        # Kirim stiker dan pesan
        print("Partner ditemukan, kirim pesan dan stiker...")
        await asyncio.sleep(2)
        await client.send_message(bot_username, "ce")  # Trigger reaksi
        await asyncio.sleep(1)
        await client.send_sticker(bot_username, sticker_id)
        await asyncio.sleep(1)
        await client.send_message(bot_username, katanya)

        # Tunggu beberapa detik lalu skip jika belum skip otomatis
        await asyncio.sleep(20)
        if chatting:
            print("Auto skip karena tidak ada respon.")
            await skip_chat()

@app.on_message(filters.sticker & filters.me)
async def start_command(client, message):
    print("Userbot Started by sending sticker.")
    await message.reply("Userbot Started!")
    await start_new_chat()

async def start_new_chat():
    await asyncio.sleep(1)
    print("Mencari partner baru...")
    await app.send_message(bot_username, "🚀 Find a partner")

async def skip_chat():
    global chatting
    chatting = False
    print("Melewati partner...")
    await app.send_message(bot_username, "/next")
    await asyncio.sleep(3)

app.run()
