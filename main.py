from aiogram import Bot, Dispatcher, executor, types
from handlers import start, language, message_forwarder, admin_panel
import config

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

# Handlers
start.register_handlers(dp)
language.register_handlers(dp)
message_forwarder.register_handlers(dp)
admin_panel.register_handlers(dp)

if __name__ == "__main__":
    print("Bot started!")
    executor.start_polling(dp, skip_updates=True)
