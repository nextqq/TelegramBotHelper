import asyncio
from aiogram import Router, types, F
video_chat_router = Router(name='start')


@video_chat_router.message(
    F.content_type.in_({
        types.ContentType.VIDEO_CHAT_PARTICIPANTS_INVITED,
        types.ContentType.VIDEO_CHAT_SCHEDULED,
        types.ContentType.VIDEO_CHAT_STARTED,
        types.ContentType.VIDEO_CHAT_ENDED,
        types.ContentType.VIDEO_NOTE,
    }),
)
async def delete_video_chat_messages(message: types.Message):
    await asyncio.sleep(150)
    await message.delete()
