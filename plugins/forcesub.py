from pyrogram.errors import (ChatAdminRequired, ChatWriteForbidden,
                             UserNotParticipant)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import FSUB_CHANNEL, FSUB_TEXT

async def forcesub(app, msg):
    join = False
    chat_info = await app.get_chat(FSUB_CHANNEL)
    link = await app.export_chat_invite_link(FSUB_CHANNEL)
    title = chat_info.title

    try:
        try:
            await app.get_chat_member(-1001496036895, msg.from_user.id)
        except:
            join = True
        
        if join:
            try:
                buttons = [
                    [
                        InlineKeyboardButton(f"• Join {title} •", url=link)
                    ]
                ]
                await msg.reply(
                    FSUB_TEXT.format(title),
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
            return True
    except ChatAdminRequired:
        print(f"I'm not admin in the chat: {FSUB_CHANNEL} !")
    return False
