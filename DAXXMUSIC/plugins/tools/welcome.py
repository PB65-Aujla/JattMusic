import os
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import *
from pyrogram.types import *
from logging import getLogger
from DAXXMUSIC import app





LOGGER = getLogger(__name__)

class WelDatabase:
    def __init__(self):
        self.data = {}

    async def find_one(self, chat_id):
        return chat_id in self.data

    async def add_wlcm(self, chat_id):
        self.data[chat_id] = {}  # You can store additional information related to the chat
        # For example, self.data[chat_id]['some_key'] = 'some_value'

    async def rm_wlcm(self, chat_id):
        if chat_id in self.data:
            del self.data[chat_id]

wlcm = WelDatabase()

class temp:
    ME = None
    CURRENT = 2
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None

# ... (rest of your code remains unchanged)

# ... (FUCK you randi ke bacvhhe )

def circle(pfp, size=(500, 500)):
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

def welcomepic(pic, user, chatname, id, uname):
    background = Image.open("DAXXMUSIC/assets/wel2.png")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp)
    pfp = pfp.resize((825, 824))
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('DAXXMUSIC/assets/font.ttf', size=110)
    welcome_font = ImageFont.truetype('DAXXMUSIC/assets/font.ttf', size=60)
    draw.text((2100, 1420), f'{user}', fill=(12000, 12000, 12000), font=font)
    pfp_position = (1990, 435)
    background.paste(pfp, pfp_position, pfp)
    background.save(f"downloads/welcome#{user}.png")
    return f"downloads/welcome#{user}.png"

# FUCK you bhosadiwale 


@app.on_message(filters.command("welcome") & ~filters.private)
async def auto_state(_, message):
    usage = "**Usage:**\n⦿/welcome➤ [on|off]"
    if len(message.command) == 1:
        return await message.reply_text(usage)
    chat_id = message.chat.id
    user = await app.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in (
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.OWNER,
    ):
        A = await wlcm.find_one(chat_id)
        state = message.text.split(None, 1)[1].strip().lower()
        if state == "on":
            if A:
                return await message.reply_text("Special Welcome Already Enabled")
            elif not A:
                await wlcm.add_wlcm(chat_id)
                await message.reply_text(f"Enabled Special Welcome in {message.chat.title}")
        elif state == "off":
            if not A:
                return await message.reply_text("Special Welcome Already Disabled")
            elif A:
                await wlcm.rm_wlcm(chat_id)
                await message.reply_text(f"Disabled Special Welcome in {message.chat.title}")
        else:
            await message.reply_text(usage)
    else:
        await message.reply("Only Admins Can Use This Command")

# ... (copy paster teri maa ki chut  )

@app.on_chat_member_updated(filters.group, group=-3)
async def greet_group(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
    A = await wlcm.find_one(chat_id)  # Corrected this line
    if not A:
        return
    if (
        not member.new_chat_member
        or member.new_chat_member.status in {"banned", "left", "restricted"}
        or member.old_chat_member
    ):
        return
    user = member.new_chat_member.user if member.new_chat_member else member.from_user
    try:
        pic = await app.download_media(
            user.photo.big_file_id, file_name=f"pp{user.id}.png"
        )
    except AttributeError:
        pic = "DAXXMUSIC/assets/upic.png"
    if (temp.MELCOW).get(f"welcome-{member.chat.id}") is not None:
        try:
            await temp.MELCOW[f"welcome-{member.chat.id}"].delete()
        except Exception as e:
            LOGGER.error(e)
    try:
        welcomeimg = welcomepic(
            pic, user.first_name, member.chat.title, user.id, user.username
        )
        temp.MELCOW[f"welcome-{member.chat.id}"] = await app.send_photo(
            member.chat.id,
            photo=welcomeimg,
            caption=f"""
**Wᴇʟᴄᴏᴍᴇ Tᴏ {member.chat.title}\n
➖➖👉𝚈𝙾𝚄𝚁 𝚂𝙴𝙻𝙵👈➖➖\n
Nᴀᴍᴇ ✧ {user.mention}\n
Iᴅ ✧ {user.id}\n
➖➖𝐅ᴏʟʟᴏᴡ 𝐑ᴜʟᴇꜱ➖➖\n
╰➢𝙽𝙾 𝙳𝙸𝚁𝚃𝚈 𝚃𝙰𝙻𝙺𝚂 🔉\n
╰➢𝙳𝙾𝙽'𝚃 𝙰𝙱𝚄𝚂𝙴 🚫\n
╰➢𝙳𝙾𝙽'𝚃 𝚂𝙿𝙰𝙼 ⚠️\n
╰➢𝙳𝙾𝙽'𝚃 𝙳𝙼/𝙿𝙼 💢\n
╰➢𝙳𝙾𝙽'𝚃 𝙳𝙸𝚂𝚁𝙴𝚂𝙿𝙴𝙲𝚃 🤬\n
╰➢𝙻𝙰𝙽𝙶. 𝙿𝙽𝙱, 𝙷𝙸𝙽 & 𝙴𝙽𝙶 🗣️\n
╰➢𝐀ηу 𝐏яσвℓєм 𝐓уρє @admin 🍀\n
➖➖𝚃𝚑𝚊𝚗𝚔𝚜 𝙵𝚘𝚛 𝙹𝚒𝚘𝚗➖➖**
""",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"🔐𝚂𝙴𝙲𝚄𝚁𝙴 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿🔐", url=f"https://t.me/MissSardarniBot?startgroup=true")]])
        )
    except Exception as e:
        LOGGER.error(e)
    try:
        os.remove(f"downloads/welcome#{user.mention}.png")
        os.remove(f"downloads/pp{user.mention}.png")
    except Exception as e:
        pass

# ... (resfuxbk 

@app.on_message(filters.new_chat_members & filters.group, group=-1)
async def bot_wel(_, message):
    for u in message.new_chat_members:
        if u.id == app.me.id:
            await app.send_message(LOG_CHANNEL_ID, f"""
**NEW GROUP
➖➖➖➖➖➖➖➖➖➖➖
NAME: {message.chat.title}
ID: {message.chat.id}
USERNAME: @{message.chat.username}
➖➖➖➖➖➖➖➖➖➖➖**
""")
