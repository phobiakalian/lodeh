from pyrogram import Client, filters
import asyncio
import random

# Konfigurasi akunmu
api_id = 1234
api_hash = "0dkjdkjoa"
session = "1jijeq919jeiqj"

bot_username = "chatbot"
sticker_id = "CAACAgUAAyEGAASTIE8vAAIBz2gjb5Yq3kb7-1eQ2HEbxwJd_kjlAAI7FQACAkh4VMu11jWyYQZ7HgQ"

kata_kata = [
    "Kalau kamu penasaran, coba cari @caritemansini di pencarian Telegram 😏",
    "Grupnya Sifa? Rahasia sih... tapi coba deh cari @caritemansini 😜",
    "Tempat ngobrol seru? Cari aja di Telegram: @caritemansini 💬✨",
    "Kamu bakal nemuin banyak hal seru di @caritemansini. Coba cari sekarang juga!",
    "Ssst... tempat asik buat nyari temen? Cari aja @caritemansini di Telegram 👀",
    "Grup Sifa gak sembarangan, cuma buat yang nemu @caritemansini 🤫",
    "Cuma orang penasaran yang bisa nemu tempat spesial ini 😇 Cari aja @caritemansini",
    "Masih sendirian? Coba cari @caritemansini, siapa tau berubah status 💘",
    "Kamu tipe penasaran? Buktikan! Cari @caritemansini sekarang juga 😎",
    "Ada yang spesial nunggu kamu di sana... cari aja @caritemansini 🧲",
    "Lagi nyari tempat ngobrol yang beda? Cari aja @caritemansini di Telegram 😏",
    "Grup Sifa tuh kayak harta karun... tapi yang nemu cuma yang cari @caritemansini 🔍",
    "Penasaran ngobrol sama yang seru-seru? Coba cari @caritemansini 💬✨",
    "Gak semua orang tau tempat ini... tapi kamu bisa cari @caritemansini dan masukin! 🤫",
    "Tempat curhat paling aman dan seru? Cari di Telegram: @caritemansini 😇",
    "Mau kenal orang baru yang asik? Awali langkahmu dengan cari @caritemansini 🫶",
    "Gak usah malu, tinggal buka Telegram dan ketik: @caritemansini 😚",
    "Grup seru yang bikin betah ngobrol? Cari @caritemansini di pencarian 🔥",
    "Klik stiker kalau penasaran... abis itu langsung cari @caritemansini! 😍",
    "Kamu jomblo? Gabung ke grup yang bisa bikin kamu lupa status 😜 Cari: @caritemansini",
    "Kalau kamu orangnya penasaran, kamu pasti bakal cari @caritemansini sekarang juga 😎",
    "Mau kenalan sama orang baru tiap hari? Sifa kasih jalannya~ cari @caritemansini 😘",
    "Daripada nunggu yang gak pasti, mending cari grupnya Sifa di @caritemansini 💘",
    "Cuma orang keren yang bisa nemuin @caritemansini tanpa dikasih tau banyak 🕵️‍♂️",
    "Bosen ngobrol di sini terus? Coba deh cari tempat yang lebih rame: @caritemansini",
    "Gak percaya ada grup asik? Buktikan sendiri, cari @caritemansini 🤯",
    "Mau grup yang isinya bukan robot semua? Cari @caritemansini sekarang juga 😅",
    "Di balik nama @caritemansini, ada banyak cerita seru. Berani cari? 😳",
    "Gak semua grup bisa bikin betah, tapi @caritemansini beda ceritanya 😍",
    "Kalau kamu baca ini, berarti kamu ditakdirkan buat cari @caritemansini 🫣",
    "Masuk ke dunia baru, penuh candaan dan obrolan seru. Cari: @caritemansini 🚪",
    "Masih ngobrol di sini? Grup aslinya ada di @caritemansini! 😆",
    "Ada banyak kejutan kalau kamu ketik @caritemansini di kolom search 😲",
    "Kamu gak salah baca, cari aja @caritemansini dan rasain bedanya 😇",
    "Grup rahasia yang mulai viral. Jangan ketinggalan! Cari: @caritemansini 🧨",
    "Mau yang rame, seru, tapi gak toxic? Cari @caritemansini! 😎",
    "Yang jomblo masuk, yang baper minggir 😜 Cari aja @caritemansini",
    "Mau cari temen curhat? Atau temen diskusi? Ada semua di @caritemansini 💬",
    "Satu langkah kecil buat kamu, tapi satu dunia baru di @caritemansini 😍",
    "Terlalu banyak chat kosong di sini? Pindah ke obrolan asli: cari @caritemansini",
    "Gak perlu nunggu link, cukup ketik @caritemansini di search 🔎",
    "Yang lagi gabut pasti cocok join ke @caritemansini 😆",
    "Banyak yang udah gabung, kamu kapan? Cari @caritemansini sekarang juga 🥳",
    "Udah bukan zamannya chat random doang, masuk grup beneran di @caritemansini 🧠",
    "Coba cari @caritemansini. Kalau gak cocok, gak usah join 😏 Tapi pasti cocok 😎"
]


app = Client("akak", api_id=api_id, api_hash=api_hash, session_string=session)

chatting = False
current_chat = None
lock = asyncio.Lock()  # Tambahkan lock global

@app.on_message(filters.bot & filters.chat(bot_username))
async def handle_messages(client, message):
    global chatting, current_chat

    if not message.text:
        return

    text = message.text.lower()

    async with lock:
        if "😞" in text or "your partner has stopped the chat" in text:
            chatting = False
            print("Partner disconnected. Mulai cari baru...")
            await start_new_chat()

        elif "/next" in text and not chatting:
            chatting = True
            current_chat = message.chat.id
            katanya = random.choice(kata_kata)

            print("Partner ditemukan, kirim pesan dan stiker...")

            await asyncio.sleep(2)
            await client.send_message(bot_username, "ce")  # Trigger
            await asyncio.sleep(4)
            await client.send_sticker(bot_username, sticker_id)
            await asyncio.sleep(1)
            await client.send_message(bot_username, katanya)

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
