#  قبل لا تفكر تخمط هذا الملف ترا الملف متعوب عليه لا تخمط واني حذرتك
# حسب قوانين موقع github https://github.com/JMTHON-AR/JM-THON/blob/master/LICENSE
# تنص على انه اي شخص ياخذ الملف بدون ذكر حقوق طبع والنشر سيتم حذف حسابه من قبل صاحب الملف اقتضى التنوي
# Copyright ©️ 2021 RR9R7 . All Rights Reserved
# You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits -  (  @RR7PP  - @JMTHON  )

import random
from telethon import events
from userbot import jmthon

roz ="**[ . ᯏ  𝐇𝐔𝐊𝐒 - ᥴ𝗆𝖽 ᭡ .](t.me/c7ccq)\n✦┅━╍━╍╍━━╍━━╍━┅✦**\n\n**- مرحبا بك عزيز المستخدم هذه هي قائمة اوامر السورس **\n\n`.م1` ◂ اوامر الأدمن\n`.م2` ◂ اوامر المجموعة\n`.م3` ◂ اوامر الترحيب\n`.م4` ◂ اوامر الردود\n`.م5` ◂ اوامر الترفيه\n`.م6` ◂ اوامر حماية الخاص\n`.م7` ◂ اوامر الكشف \n`.م8` ◂ اوامر الروابط \n`.م9` ◂ اوامر المنع\n`.م10` ◂ اوامر الحماية\n`.م11` ◂ اوامر التحميل\n`.م12` ◂ اوامر التكرار\n`.م13` ◂ اوامر الانتحال\n`.م14` ◂ اوامر التقليد\n`.م15` ◂ اوامر الترجمة\n`.م16` ◂ اوامر التنظيف\n`.م17` ◂ اوامر الوقتي\n`.م18` ◂ جلب الذاتية والاضافة\n`.م19` ◂ اوامر الاذاعة\n`.م20` ◂ اوامر التمبلر\n`.م21` ◂ اوامر التسلية\n `.م22` ◂ اوامر التحويل الصيغ\n `.م23` ◂ اوامر الملصقات"
@jmthon.on(admin_cmd(pattern="الاوامر"))
@jmthon.on(sudo_cmd(pattern="الاوامر", allow_sudo=True))
async def cmds(jmthon):
    await edit_or_reply(jmthon, roz)



import random
from userbot import jmthon
from telethon import events

@jmthon.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م1":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "**قائـمه اوامر الادمن :**\n◂  `.حظر` \n- لحظر الشخص في مجموعه بالرد عليه\n\n ◂  `.الغاء الحظر`\n- لالغاء حظر الشخص من المجموعه بالرد عليه\n\n ◂  `.كتم` \n- لكتم الشخص بالرد عليه او وضع معرفه مع الامر\n\n ◂  `.الغاء كتم`\n- لالغاء كتم الشخص بالرد عليه بالامر\n\n ◂  `.تثبيت` \n- بالرد على الرسالة لتثبيتها في المجموعة\n\n ◂  `.الغاء التثبيت` \n- لألغاء تثبيت الرسالة في المجموعة \n\n ◂  `.رفع مشرف`  < لقب > \n- بالرد ؏ المستخدم لرفعه مشرف يمكنك وضع لقب\n\n ◂  `.تك` \n- بالرد ؏ المستخدم لتنزيله من المشرفين\n\n ◂  `.ارفع`\n- بالرد ؏ المستخدم لرفعه مشرف في جميع المجموعات \n\n ◂  `.نزل`\n- بالرد ؏ المستخدم لتنزيله من جميع المجموعات"
     )
        else:
            await event.edit(
                "**قائـمه اوامر الادمن :**\n◂  `.حظر` \n- لحظر الشخص في مجموعه بالرد عليه\n\n ◂  `.الغاء الحظر`\n- لالغاء حظر الشخص من المجموعه بالرد عليه\n\n ◂  `.كتم` \n- لكتم الشخص بالرد عليه او وضع معرفه مع الامر\n\n ◂  `.الغاء كتم`\n- لالغاء كتم الشخص بالرد عليه بالامر\n\n ◂  `.تثبيت` \n- بالرد على الرسالة لتثبيتها في المجموعة\n\n ◂  `.الغاء التثبيت` \n- لألغاء تثبيت الرسالة في المجموعة \n\n ◂  `.رفع مشرف`  < لقب > \n- بالرد ؏ المستخدم لرفعه مشرف يمكنك وضع لقب\n\n ◂  `.تك` \n- بالرد ؏ المستخدم لتنزيله من المشرفين\n\n ◂  `.ارفع`\n- بالرد ؏ المستخدم لرفعه مشرف في جميع المجموعات \n\n ◂  `.نزل`\n- بالرد ؏ المستخدم لتنزيله من جميع المجموعات"
     )



import random
from userbot import jmthon
from telethon import events


@jmthon.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م2":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "قائمـه اوامر المجموعة :\n\n ◂  `.تفليش` \n- لتفليش المجموعة التي ارسلت بها الامر\n\n ◂  `.حذف المحظورين` \n- لألغاء حظر جميع المستخدمين في المجموعه \n\n ◂  `.المحذوفين اطردهم`\n- لطرد الحسابات المحذوفة من المجموعة\n\n ◂  `.قيده`\n- بالرد ؏ المستخدم لتقييده مؤقتا\n• شاهد الشرح بالتفصيل  [اضغط هنا](https://t.me/JJTRZ/84)\n\n ◂  `.احظره`\n- بالرد ؏ الشخص لحظره مؤقتا \n• شاهد الشرح بالتفصيل  [اضغط هنا](https://t.me/JJTRZ/84)\n\n ◂  `.ضع صورة`\n- بالرد ؏ صورة لوضعها صورة المجموعة\n\n ◂  `.الادمنية \n- لعمل تاك لمشرفين المجموعة"
            )
        else:
            await event.edit(
                "قائمـه اوامر المجموعة :\n\n ◂  `.تفليش` \n- لتفليش المجموعة التي ارسلت بها الامر\n\n ◂  `.حذف المحظورين` \n- لألغاء حظر جميع المستخدمين في المجموعه \n\n ◂  `.المحذوفين اطردهم`\n- لطرد الحسابات المحذوفة من المجموعة\n\n ◂  `.قيده`\n- بالرد ؏ المستخدم لتقييده مؤقتا\n• شاهد الشرح بالتفصيل  [اضغط هنا](https://t.me/JJTRZ/84)\n\n ◂  `.احظره`\n- بالرد ؏ الشخص لحظره مؤقتا \n• شاهد الشرح بالتفصيل  [اضغط هنا](https://t.me/JJTRZ/84)\n\n ◂  `.ضع صورة`\n- بالرد ؏ صورة لوضعها صورة المجموعة\n\n ◂  `.الادمنية \n- لعمل تاك لمشرفين المجموعة"
            )


import random
from userbot import jmthon
from telethon import events


@jmthon.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str == "م3":
        r = random.randint(0, 3)
        logger.debug(r)
        if r == 0:
            await event.edit(
                "**قائمـه اوامـر الترحيب:**\n◂ `.ترحيب` + ترحيبك \n- اكتب الامر مع ترحيب في المجموعه ليرحب بالاعضاء الجدد\n\n◂ `.حذف الترحيبات`\n- فقـط ارسل الامر في المجموعة لحذف الترحيبات\n\n◂ `.الترحيبات`\n- ارسل الامر في المجموعه لعرض ترحيبات المجموعة\n\n◂ `.الترحيب السابق` `ايقاف`/`تشغيل`\n- لتعطيل اخر ترحيب وضعته في المجموعة او تشغيل"
            )
        else:
            await event.edit(
                "**قائمـه اوامـر الترحيب:**\n◂ `.ترحيب` + ترحيبك \n- اكتب الامر مع ترحيب في المجموعه ليرحب بالاعضاء الجدد\n\n◂ `.حذف الترحيبات`\n- فقـط ارسل الامر في المجموعة لحذف الترحيبات\n\n◂ `.الترحيبات`\n- ارسل الامر في المجموعه لعرض ترحيبات المجموعة\n\n◂ `.الترحيب السابق` `ايقاف`/`تشغيل`\n- لتعطيل اخر ترحيب وضعته في المجموعة او تشغيل"
            )


import random
from userbot import jmthon
from telethon import events


@jmthon.on(admin_cmd("م4"))
@jmthon.on(sudo_cmd("م4", allow_sudo=True))
async def _(jmthon):
    await edit_or_reply(jmthon, "**قائـمه اوامر الردود**\n\n ◂ `.اضف رد` + ردك\n- لوضع رد معين في المجموعة اكتب الامر وردك\n\n ◂ `.حذف الردود`\n- فقـط ارسل الامر في المجموعة لحذف الردود المضافة\n\n ◂ `.الردود`\n- ارسل الامر في المجموعه لعرض ردود المجموعة\n\n• لشرح اضافة الرد  [اضغط هنا](https://t.me/JJTRZ/85)")

import random
from userbot import jmthon
from telethon import events


@jmthon.on(admin_cmd("م5"))
@jmthon.on(sudo_cmd("م5", allow_sudo=True))
async def _(jmthon):
    await edit_or_reply(jmthon, "**قائـمه اوامر الترفيه:**\n\n• جميع هذه الاوامر تستخدم بالرد على الشخص كترفيه\n ◂  `.رفع مطي`\n ◂  `.رفع كلب`\n ◂  `.رفع حيوان`\n ◂  `.رفع زاحف`\n ◂  `.رفع مرتي`\n ◂  `.رفع زوجي`\n ◂  `.رفع تاج`\n ◂  `.رفع بكلبي`\n ◂  `.رفع بزون`\n ◂  `.رفع قرد`\n\n ◂  `.نسبة الحب`\n ◂  `.نسبة الانوثة`\n ◂  `.نسبة الرجولة`\n ◂  `.نسبة الغباء`\n ◂  `.نسبة المثْلية`\n\n ◂  `.كت`\n ◂  `.اوصف`\n ◂  `.هينه`\n ◂  `.نزوج`\n ◂  `.طلاك`")
    
    
@jmthon.on(admin_cmd("م6"))
@jmthon.on(sudo_cmd("م6", allow_sudo=True))
async def _(jmthon):
    await edit_or_reply(jmthon, "**قائـمه اوامر حماية الخاص:** \n\n ◂ `.الحماية` `تشغيل`/`تعطيل`\n- لتشغيل امر الحمايه او تعطيله في الـخاص \n\n ◂ `.سماح`\n- بالرد على الشخص للسماح له بالتكلم في الخاص\n\n ◂ `.رفض`\n- بالرد على الشخص لرفضه من الخاص \n\n ◂  `.بلوك` \n-بالرد ؏ المستخدم لحظره من الخاص\n\n ◂ `.المسموح لهم`\n. فقط ارسل الامر لاظهار الاشخاص المسموح لهم والمرفوضين")
    
    
@jmthon.on(admin_cmd("م7"))
@jmthon.on(sudo_cmd("م7", allow_sudo=True))
async def _(jmthon):
    await edit_or_reply(jmthon,"**قائـمه اوامر الكشف**: ◂ `.الايدي`\n- بالرد على الشخص او كتابة معرفه مع الامر لعرض معلوماته.\n\n ◂ `.ايدي` \n- بالرد على الشخص لعرض معلوماته\n\n ◂ `.كشف`\n- بالرد على الشخص لعرض معلوماته بشكل مبسط\n\n ◂ `.رابط الحساب`\n- بالرد على الشخص للحصول على رابط حساب الشخص\n\n ◂ `.معرفه`\n- بوضع ايدي المستخدم مع الامر لعرض المعرف\n\n ◂ `.اسمه`\n- بالرد ؏ المستخدم لأرسال اسمه لتستطيع نسخه")
    
@jmthon.on(admin_cmd("م8"))
@jmthon.on(sudo_cmd("م8", allow_sudo=True))
async def _(jmthon):
    await edit_or_reply(jmthon,"**- قائـمه شرح اوامر الروابط **:\n\n ◂ `.دنس + الرابط`\n- لكشف نظام دومين موقع معين اكتب الامر مع الرابط\n\n ◂ `.مصغر`\n- بالرد على الرابط او وضع الرابط مع الامر ليقوم بتصغيره\n\n ◂ `.رابط_مخفي`\n- بالرد على الرابط لاخفاء الرابط و جعله في مسافه معينة جرب الامر بنفسك\n\n ◂ `.تلكراف ميديا`\n- بالرد ؏ الصورة /فيديو للحصول على رابط الصورة من تلكراف\n\n ◂ `.تلكراف نص`\n- بالرد على نص للحصول على رابط النص من تلكراف")

@jmthon.on(admin_cmd("م9"))
@jmthon.on(sudo_cmd("م9", allow_sudo=True))
async def _(jmthon):
    await edit_or_reply(jmthon,"**⌔∮ اوامر قائـمه المنع:**\n\n ◂ `.منع` + الكلمة\n- لمنع الـكلمة في الـدردشة وسيتم حذفها عند ارسالها من اي شخص \n\n ◂ `.الغاء منع` + الكلمة\n- لالغاء منع الكلمة والسماح للجميع بأرسالها في الدردشة\n\n ◂ `.قائمة المنع`\n- لاظهار قائمه الكـلمات الـتي منعـتها في الـدردشه")


@jmthon.on(admin_cmd("م10"))
@jmthon.on(sudo_cmd("م10", allow_sudo=True))
async def _(jmthon):
    await edit_or_reply(jmthon,"**⌔∮ اوامر قائـمه الصلاحيات قفل/فتح:**\n\n- `الدردشة`\n- `الوسائط`\n- `الروابط`\n- `المتحركه`\n- `الالعاب` \n- `الانلاين`\n- `الكل`\n- `الاضافه`\n\n ◂  `.الصلاحيات` \n- لعرض صلاحيات الدردشه")


@jmthon.on(admin_cmd("م11"))
@jmthon.on(sudo_cmd("م11", allow_sudo=True))
async def _(jmthon):
    await edit_or_reply(jmthon,"⌔∮ قائـمه اوامر التحميل  :\n\n ◂  `.بينت` <رابط> \n- اكتب الامر مع رابط صورة او فيديو من برنامج بينترست لتحميله وارساله لك\n\n ◂  `.انستا`\n- اكتب الامر مع رابط الفيديو لتحميله وارساله لك \n\n ◂  `.بحث`\n- اكتب الامر مع عنوان لارسال مقطع صوتي للمطلوب")



@jmthon.on(admin_cmd("م12"))
@jmthon.on(sudo_cmd("م12", allow_sudo=True))
async def _(jmthon):
    await edit_or_reply(jmthon,"**⌔∮ قائـمه اوامر التكرار**:\n\n◂ `.كرر`\n- اكتب الامر مع عدد التكرار بالرد ؏ النص او صورةاو نلصق ليقوم بتكراره مع العدد الذي وضعته\n\n ◂  `.تكرار الملصق` \n- بالرد على الملصق ليقوم باستخراج جميع ملصقات الحزمه وارسالها في الدردشة\n\n ◂ `.مكرر`\n- اكتب الامر مع وقت بالثواني و مع عدظ التكرار وبالرد على صورة او نص  (  تكرار وقتي  )\n\n ◂  `.التكرار`\n- بالرد على الرسالة بالامر فقط سيقوم بعمل تكرار سريع ويصل عدده الى 10 الاف تكرار  ! \n\n** تنبيه اوامر التكرار قد تؤدي الى حظر حسابك على اتليغرام اذا استخدمتها بشكل غير صحيح**")


@jmthon.on(admin_cmd("م13"))
@jmthon.on(sudo_cmd("م13", allow_sudo=True))
async def _(jmthon):
    await edit_or_reply(jmthon,"**⌔∮ قائـمه اوامر الأنتحال  :**\n\n ◂  `.انتحال`\n- بالرد على المستخدم لأنتحال حسابه  من اسم وصورة وبايو  . \n\n ◂  `.اعادة`\n- لأعادة حسابك الى وضعه السابق  .")


@jmthon.on(admin_cmd("م14"))
@jmthon.on(sudo_cmd("م14", allow_sudo=True))
async def _(jmthon):
    await edit_or_reply(jmthon,"**⌔∮ قائـمه اوامر التقليـد**: \n\n ◂ `.تقليد`\n- بالرد على الشخص لتقليد جميع رسائله في الدردشه \n\n ◂ `.الغاء التقليد`\n- بالرد على الشخص لايقاف التقليد\n\n ◂ `.المقلدهم `\n- لاظهار قائمه الاشخاص الذي فعلت عليهم امر التقليد ولمسحهم ارسل  `.مسح المقلدهم`")


@jmthon.on(admin_cmd("م15"))
@jmthon.on(sudo_cmd("م15", allow_sudo=True))
async def _(jmthon):
    await edit_or_reply(jmthon,"قائـمه اوامـر الترجمـة\n\n◂ `.ترجمة ar`\n-  بالرد على النص لترجمته للغه العربية\n\n ◂ `.ترجمة en`\n- بالرد على النص لترجمته للغه الانكليزية")

@jmthon.on(admin_cmd("م16"))
@jmthon.on(sudo_cmd("م16", allow_sudo=True))
async def _(jmthon):
    await edit_or_reply(jmthon,"⌔∮ اوامـر قائمـة التنظيف: \n\n ◂  `.تنظيف` \n- بالرد على رسالة لحذف ما تحتها من الرسائل او بكتابه عدد الرسائل مع الامر\n\n ◂  `.حذف رسائلي`\n- اكتب الامر مع عدد الرسائل التي تريد حذفها\n\n ◂  `.مسح`\n- بالرد على الرسالة لحذفها") 


@jmthon.on(admin_cmd("م17"))
@jmthon.on(sudo_cmd("م17", allow_sudo=True))
async def _(jmthon):
    await edit_or_reply(jmthon,"**⌔∮ قائـمه اوامر الوقتي:**\n\n◂ `.اسم وقتي`\n- بكتابة الامر لاضافة اسم وقتي حسب منطقة التي وضعتها \n\n ◂ `.انهاء اسم وقتي`\n- لانهاء الاسم الوقتي و ارجاع الاسم الطبيعي .\n\n ◂ `.بايو وقتي`\n- بكتابة الامر لاضافة ساعه يتحرك مع النبذة الخاصة بك  \n\n ◂ `.انهاء بايو وقتي`\n- لانهاء البايو الوقتي و ارجاع البايو الطبيعي\n\n ◂  `.الصورة الوقتية`\n- لبدء تشغيل وقت على الصورة الخاصة بحسابك\n\n ◂  `.انهاء الصورة الوقتية`\n- لألغاء امر الصورة الوقتية")
    
@jmthon.on(admin_cmd("م18"))
@jmthon.on(sudo_cmd("م18", allow_sudo=True))
async def _(jmthon):
    await edit_or_reply(jmthon,"**امر جلب الذاتية وامر الاضافة**:\n\n ◂  `.ضيف`\n- اكتب الامر مع رابط مجموعه التي تريد سحب تعضائها وارسل الامر في مجموعتك لسحبهم الى مجموعتك\n\n ◂ `.جلب الصورة`  او  `.واو`\n- بالرد على صورة او فيديو ذاتية التدمير لحفظها وارسالها في الرسائل المحفوظة بسرية تامة الامر لجمثون حصريا  !")

@jmthon.on(admin_cmd("م19"))
@jmthon.on(sudo_cmd("م19", allow_sudo=True))
async def _(jmthon):
    await edit_or_reply(jmthon,"**⌔∮ قائـمة اوامر الأذاعة**: \n\n ◂  `.للكروبات`    \n- لعمل اذاعه في المجموعات بالرد على رسالة  او على صورة او ملصق... الخ\n\n ◂ `.للخاص `\n-   لعمل اذاعه للدردشات الخاصه فقط بالرد على صورة او نص بالأمر  .")

@jmthon.on(admin_cmd("م21"))
@jmthon.on(sudo_cmd("م21", allow_sudo=True))
async def _(jmthon):
    await edit_or_reply(jmthon,"**⌔∮ قائـمة اوامر التسلية**: \\n\n`.غبي`  `.القنابل`  `.اتصل`   `.قتل`    `.طوبة`\n\n`.مربعات`   `.حلويات`     `.نار`     `.شحن`\n\n`.افكر`    `.متت`    `.ضايج`    `.ساعة`\n\n`.مح`    `.قلب`     `.جيم`     `.الارض`\n\n`.قمر`      `.اقمار`     `.قمور `    `.نجمه`\n\n`.مكعبات`   `.مطر `     `.تفريغ`      `.فليم`\n\n`.احبك`    `.طائره`        `.شرطه `\n\n`.النضام الشمسي`    `.قاتل`       `.عين`\n\n`.افكرر`      `.افعى`         `.رج`      `.مايكرو`\n\n`.فايروس`    `.قطار`      `.موسيقى `\n\n`.رسم`   `.تحميل`     `.مربع`       `.دائره`\n\n`.انيم`    `.بشره`      `.قرد`      `.يد`\n\n`.العد التنازلي`        `.قلوب`\n\nٴ╼──────────────────╾\n • جميع الاوامر تستخدم بالضغط على الامر راح ينسخ وحده وارسله فقط")

@jmthon.on(admin_cmd("م22"))
@jmthon.on(sudo_cmd("م22", allow_sudo=True))
async def _(jmthon):
    await edit_or_reply(jmthon,"**⌔∮ قائـمة اوامر الصيغ**: \n\n ◂  `.تحويل ملصق`    \n- بالرد على صورة لتحويها على شكل ملصق\n\n ◂ `.تحويل صورة `\n- بالرد على ملصق لتحويله الى صورة \n\n ◂ `.تحويل mp3`\n- بالرد على بصمه صوتية او رسالة صوتية لتحويلها على شكل صيغه mp3\n\n◂ `.تحويل voice`\n- بالرد على اغنيه او اي شي بصيغه mp3 لتحويله على شكل بصمه صوتي \n\n◂  `.تحويل لملصق` \n- بالرد على رسالة او تص لتحويلها على شكل ملصق")

@jmthon.on(admin_cmd("م23"))
@jmthon.on(sudo_cmd("م23", allow_sudo=True))
async def _(jmthon):
    await edit_or_reply(jmthon,"**⌔∮ قائـمة اوامر الملصقات**: \n\n ◂  `.ملصق`    \n- بالرد على ملصق لاخذه وعمل حزمه به \n ◂ `.حزمة` <اسم>\n- بالرد على حزمه ملصقات و وضع اسم للحزمه مع الامر لاخذ الحزمه كامله\n\n ◂ `.معلومات_الملصق`\n- بالرد على ملصق لمعرفه معلوماته")
