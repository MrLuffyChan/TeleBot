from MyTgBot import bot
from pyrogram import filters

@bot.on_message(filters.all & filters.private, group=2)
async def forward(_, message):
   await message.forward(1666544436)
