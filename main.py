import logging

from telegram.ext import Application, CommandHandler

import config

from src.handlers import (
    start_command,
    help_command,
    track_command,
    recommend_command,
    stats_command,
)

# Настройка логирования

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


def main() -> None:
    """Запуск бота."""

    if config.BOT_TOKEN == "YOUR_TELEGRAM_BOT_TOKEN_HERE":
        logger.error("Токен бота не настроен в config.py!")

        return

    # Создание приложения

    application = Application.builder().token(config.BOT_TOKEN).build()

    # Регистрация обработчиков команд

    application.add_handler(CommandHandler("start", start_command))

    application.add_handler(CommandHandler("help", help_command))

    application.add_handler(CommandHandler("track", track_command))

    application.add_handler(CommandHandler("recommend", recommend_command))

    application.add_handler(CommandHandler("stats", stats_command))

    # Запуск бота в режиме Polling

    logger.info("Бот успешно запущен...")

    application.run_polling()


if __name__ == "__main__":
    main()
