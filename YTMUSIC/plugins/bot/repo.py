from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from YTMUSIC import app
from config import BOT_USERNAME
from YTMUSIC.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """**
✪ ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ˹ ᴛʜᴜɴᴅᴇʀ-ᴍᴜsɪᴄ™ ˼ ʙᴏᴛ ✪
 
 ❍ • ʙsᴅᴋ ʀᴇᴘᴏ ʟᴇɢᴀ ◉‿◉ •
 
 ❍ • ᴘᴇʜʟᴇ ᴍɪᴄᴋᴇʏ ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟ •
 
 ❍ • ᴄʜᴜᴘ ᴄʜᴜᴘ ʙᴏᴛ ʟᴇᴋᴇ ɴɪᴋᴀʟ •
 
 ❍ • ʀᴇᴘᴏs ᴛᴏ ɴᴀʜɪ ᴍɪʟᴇɢᴀ ʙᴇᴛᴀ ⊂◉‿◉ •
 
 ❍ • ᴀɢʀ ᴄʜᴀʜɪʏᴇ ᴛᴏ ᴍɪᴄᴇʏ ᴋᴏ ᴘᴀᴘᴀ ʙᴏʟɴᴀ ᴘᴀᴅᴇɢᴀ •
 
 ❍ • ɪsᴛᴋʜᴀʀ ᴘᴀᴘᴀ • **"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("•ᴀᴅᴅ ᴍᴇ•", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("•sᴜᴘᴘᴏʀᴛ•", url="https://t.me/THUNDERDEVS"),
          InlineKeyboardButton("•ᴏᴡɴᴇʀ•", url="https://t.me/ll_THUNDER_lll"),
          ],
               [
                InlineKeyboardButton("•ᴜᴘᴅᴀᴛᴇs•", url="https://t.me/THUNDERDEVS"),

],
[
              InlineKeyboardButton("•ᴄʟᴀssʏ-ᴍᴜsɪᴄ•", url=f"https://t.me/ClassyMusicRobot"),
              InlineKeyboardButton("︎•ᴀᴀʀᴏʜɪ-ᴍᴜsɪᴄ•", url=f"https://t.me/AAROHI_MUSICBOT"),
              ],
              [
              InlineKeyboardButton("•ʙᴀʙʏ-ᴍᴜsɪᴄ•", url=f"https://t.me/baby_x_music_bot"),
InlineKeyboardButton("•ᴄʜᴀᴛ ʙᴏᴛ•", url=f"https://t.me/Queen_Chat_robot"),
],
[
InlineKeyboardButton("•ᴘᴜʀᴠɪ-ᴍᴜsɪᴄ•", url=f"https://t.me/purvi_music_bot"),
InlineKeyboardButton("•𝐒ᴀɴᴠɪ-ᴍᴜsɪᴄ•", url=f"https://t.me/SanviMusicRobot"),
],
[
              InlineKeyboardButton("•ᴀᴜᴛᴏʀᴇᴀᴄᴛɪᴏɴ-ʙᴏᴛ•", url=f"https://t.me/THUNDERDEVS"),
              InlineKeyboardButton("•ᴀʟᴇxᴀ-ᴍᴜsɪᴄ•︎", url=f"https://t.me/AlexaXmusicRobot"),
              ],
              [
              InlineKeyboardButton("•ᴋʜᴜsʜʙᴜ-ᴍᴜsɪᴄ•", url=f"https://t.me/KhushbuMusic_bot"),
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://files.catbox.moe/zrjno8.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
 
   
# --------------


@app.on_message(filters.command("repo", prefixes="#"))
@capture_err
async def repo(_, message):
    async with httpx.AsyncClient() as client:
        response = await client.get("https://api.github.com/repos/BABY-MUSIC/BABYTUNE/contributors")
    
    if response.status_code == 200:
        users = response.json()
        list_of_users = ""
        count = 1
        for user in users:
            list_of_users += f"{count}. [{user['login']}]({user['html_url']})\n"
            count += 1

        text = f"""[•ʙᴏᴛ-ᴏᴡɴᴇʀ•](https://t.me/UTTAM470) | [•ᴜᴘᴅᴀᴛᴇs•](https://t.me/BABY09_WORLD)
| 𝖢𝖮𝖭𝖳𝖱𝖨𝖡𝖴𝖳𝖮𝖱𝖲 |
----------------
{list_of_users}"""
        await app.send_message(message.chat.id, text=text, disable_web_page_preview=True)
    else:
        await app.send_message(message.chat.id, text="Failed to fetch contributors.")
