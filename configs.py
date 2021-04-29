# (c) @AbirHasan2005

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
	LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
	ABOUT_BOT_TEXT = f"""

𝐓𝐡𝐢𝐬 𝐢𝐬 𝐏𝐞𝐫𝐦𝐚𝐧𝐞𝐧𝐭 𝐅𝐢𝐥𝐞𝐬 𝐒𝐭𝐨𝐫𝐞 𝐁𝐨𝐭!

𝐒𝐞𝐧𝐝 𝐦𝐞 𝐚𝐧𝐲 𝐟𝐢𝐥𝐞 𝐈 𝐰𝐢𝐥𝐥 𝐬𝐚𝐯𝐞 𝐢𝐭 𝐢𝐧 𝐦𝐲 𝐃𝐚𝐭𝐚𝐛𝐚𝐬𝐞. 𝐀𝐥𝐬𝐨 𝐰𝐨𝐫𝐤𝐬 𝐟𝐨𝐫 𝐜𝐡𝐚𝐧𝐧𝐞𝐥. 𝐀𝐝𝐝 𝐦𝐞 𝐭𝐨 𝐜𝐡𝐚𝐧𝐧𝐞𝐥 𝐚𝐬 𝐀𝐝𝐦𝐢𝐧 𝐰𝐢𝐭𝐡 𝐄𝐝𝐢𝐭 𝐏𝐞𝐫𝐦𝐢𝐬𝐬𝐢𝐨𝐧, 𝐈 𝐰𝐢𝐥𝐥 𝐚𝐝𝐝 𝐒𝐚𝐯𝐞 𝐔𝐩𝐥𝐨𝐚𝐝𝐞𝐝 𝐅𝐢𝐥𝐞 𝐢𝐧 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 & 𝐚𝐝𝐝 𝐒𝐡𝐚𝐫𝐚𝐛𝐥𝐞 𝐁𝐮𝐭𝐭𝐨𝐧 𝐋𝐢𝐧𝐤

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** @Deeks_04_8



"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:**  @Deeks_04_8










Developer is Super Noob. Just Learning from Official Docs. Please Donate the developer for Keeping the Service Alive.

Also remember that developer will Delete Adult Contents from Database. So better don't Store Those Kind of Things.

"""
	HOME_TEXT = """

ʜᴀɪ ᴛʜᴀʀᴇ,  [{}](tg://user?id={})\n\n

ᴛʜɪs ɪs ᴘᴇʀᴍᴀɴᴇɴᴛ **ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ**.

sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ ɪ ᴡɪʟʟ ɢɪᴠᴇ ʏᴏᴜ ᴀ ᴘᴇʀᴍᴀɴᴇɴᴛ sʜᴀʀᴀʙʟᴇ ʟɪɴᴋ. ɪ sᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ ᴀʟsᴏ! 

ᴊᴏɪɴ ᴏᴜʀ ɢʀᴏᴜᴘ  ~> @UM_Requests

⚔️ᴍᴀɪɴᴛɪɴᴇᴅ ʙʏ 😎 =>  @Deeks_04_8
 
🏅© @UNI_MOVIES_BOX.🏅"""








