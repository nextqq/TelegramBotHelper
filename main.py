import logging
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
import os

from dotenv import load_dotenv

from handlers import handlers_router

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)
load_dotenv()


async def on_startup(bot: Bot) -> None:
    pass


async def on_shutdown(application):
    pass


async def main():
    bot = Bot(token=os.environ.get('BOT_TOKEN'))
    dp = Dispatcher(name='dp')

    dp.startup.register(on_startup)
    dp.include_routers(
        handlers_router,
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
