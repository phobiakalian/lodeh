from pyrogram import Client, filters
import asyncio

# Konfigurasi akunmu
api_id = 12345678  # Ganti dengan API ID kamu
api_hash = "your_api_hash"  # Ganti dengan API Hash kamu
session = "BQBqaAYAeEDq0DsANq8B7-Wt_ddQe0hG4ee859GS1Svws8CeTWXrebXeekUTPy1rG3xRYmYWPrb2jfsBu0AViEyGtKtA7cDLGaw4st-uxfnK35CPH1X680sjIfhG2YlLSuARV2fg2s4LyyHE_mXsZDt2F0V10u7HDPNzt-8-eYko69hNWbmxGt6ZJXgEaKoS8PVCYSuU9_Qk9L_qjl0q2CVt1vWmSefeLDMb6sfadhFG-UD7z7PY8jwa2pahMhDXYzBIekILQEqX0B5e1KUBet-aHKTUyycD9njTplcEZ6nFQV4LdjwK2FZjP6a205gjccw3TqMHI6gEidPMLFzhDRPr4OCBYgAAAAB1B3HOAA"  # Ganti dengan session string kamu

# ID atau username bot anonymous (contoh)
bot_username = "chatbot"

# ID stiker yang mau dikirim
sticker_id = "CAACAgUAAxkDAAEFHcJoDm0_l3esQe1BeZ-ZETOEGuBh8gAC0QADyESkOcWkYPEOb5EGHgQ"  # Ganti dengan file_id stikermu

app = Client("akak", api_id=api_id, api_hash=api_hash, session_string=session)

# State Tracking
chatting = False
current_chat = None

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

        # Kirim stiker
        await asyncio.sleep(2)  # Biar natural
        await client.send_sticker(bot_username, sticker_id)

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
