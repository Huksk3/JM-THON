import random

from Jmthon.razan._islam import *
from userbot import jmthon

plugin_category = "extra"

# by ~ @RR9R7
@jmthon.ar_cmd(
    pattern="اذكار الصباح",
    command=("اذكار الصباح", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        roze = random.choice(razan)
        return await event.edit(f"{roze}")


# by ~ @RR9R7
@jmthon.ar_cmd(
    pattern="اذكار المساء$",
    command=("اذكار المساء", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        ror = random.choice(roz)
        return await event.edit(f"{ror}")


# by ~ @RR 9R7
@jmthon.ar_cmd(
    pattern="احاديث$",
    command=("احاديث", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        me = random.choice(roza)
        return await event.edit(f"{me}")


@jmthon.ar_cmd(
    pattern="اذكار الاستيقاظ$",
    command=("اذكار الاستيقاظ", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        az = random.choice(rozan)
        return await event.edit(f"{az}")


@jmthon.ar_cmd(
    pattern="اذكار النوم$",
    command=("اذكار النوم", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        rr = random.choice(rozmuh)
        return await event.edit(f"{rr}")


@jmthon.ar_cmd(
    pattern="اذكار الصلاة$",
    command=("اذكار الصلاة", plugin_category),
)
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        rm = random.choice(rzane)
        return await event.edit(f"{rm}")


@jmthon.ar_cmd(
    pattern="اوامر الاذكار$",
    command=("اوامر الاذكار", plugin_category),
)
async def _(event):
    await event.edit(
        "قائمة اوامر الاذكار :\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n ⌯︙اختر احدى هذه القوائم\n\n- ( `.اذكار الصباح` ) \n- ( `.اذكار المساء` )   \n- (`.اذكار النوم`)\n- ( `.اذكار الصلاة`) \n- ( `.اذكار الاستيقاظ` ) \n- ( `.احاديث` )\n\n➖➖➖➖➖➖➖➖➖➖➖➖➖\n⌔︙CH : @DDDD0DD"
    )
