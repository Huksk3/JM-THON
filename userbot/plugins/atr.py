from telethon import events
import random, re
from userbot.utils import admin_cmd
import asyncio 


@borg.on(admin_cmd("نيك?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit(" :::  === :::  === :::===  :::===  :::  === :::  === :::     :::    ======== ===  ===  =====   ===== ===  === ===  ===     ===     ======  ===  ======  ======  ====== ")
        await asyncio.sleep(0.5)
        await event.edit("--->   ⒪")
        await asyncio.sleep(0.6)
        await event.edit(" ---> ⒪")
        await asyncio.sleep(0.5)
        await event.edit("     --⒪")
        await asyncio.sleep(0.5)
        await event.edit("     --⒪")
        await asyncio.sleep(0.5)
        await event.edit("   --->⒪")
        await asyncio.sleep(0.5)
        await event.edit("--->   ⒪")
        await asyncio.sleep(0.6)
        await event.edit(" ---> ⒪")
        await asyncio.sleep(0.5)
        await event.edit("     --⒪")
        await asyncio.sleep(0.5)
        await event.edit("     --⒪")
        await asyncio.sleep(0.5)
        await event.edit("تم النيج 😂")