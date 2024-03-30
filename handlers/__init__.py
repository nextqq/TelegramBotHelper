from handlers.commands import commands_router
from aiogram import Router

handlers_router = Router(name='handlers')

handlers_router.include_routers(
    commands_router,
)
