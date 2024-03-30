from aiogram import Router
from handlers.commands.base import video_chat_router


commands_router = Router(name='command')

commands_router.include_routers(
    video_chat_router,
)

