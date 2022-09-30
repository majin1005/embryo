from operator import mod
import nextcord
from nextcord.ext import commands
from core.classes import Cog_Extension
import json
import random, os, asyncio

"""
1.5 重大更新需加入intents 詳細請閱讀官方文件
https://discordpy.readthedocs.io/en/latest/intents.html#intents-primer
"""
# 啟用所有 intents
intents = nextcord.Intents.all() 
intents.members = True
intents.message_content = True

# 讀取設定檔 load settings
with open('setting.json', 'r', encoding= 'utf8') as jfile:
	jdata = json.load(jfile)

"""
command_prefix: 指令前綴
owner_ids: 擁有者ID
"""
bot = commands.Bot(command_prefix= jdata['Prefix'],  owner_ids= jdata['Owner_id'], intents=intents)

# Bot完成啟動後事件
@bot.event
async def on_ready():
	print(">> Bot is online <<")

# 載入cmds資料夾內所有cog

for filename in os.listdir('./cmds'):
	if filename.endswith('.py'):
		bot.load_extension(f"cmds.{filename[:-3]}")
'''
initial_extensions = ['cmds.event','cmds.main','cmds.mod','cmds.owner',]

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)
'''


if __name__ == "__main__":
	bot.run(jdata['TOKEN'])