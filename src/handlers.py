import logging

from telegram import Update

from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Обработка команды /start."""

    user_name = update.effective_user.first_name if update.effective_user else "Читатель"

    message_text = (

        f"Привет, {user_name}! 👋\n\n"

        "Я твой персональный помощник по чтению.\n"

        "Доступные команды:\n"

        "/track — Зафиксировать прогресс чтения\n"

        "/recommend — Получить рекомендацию книги\n"

        "/stats — Посмотреть статистику\n"

        "/help — Справка"

    )

    await update.message.reply_text(message_text)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Обработка команды /help."""

    help_text = (

        "📖 Как пользоваться ботом:\n\n"

        "1. Для добавления прогресса используйте /track.\n"

        "2. Для получения случайной рекомендации выберите /recommend.\n"

        "3. Ваша личная статистика доступна по /stats."

    )

    await update.message.reply_text(help_text)


async def track_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Заглушка для команды отслеживания чтения /track."""

    logger.info("Пользователь %s вызвал /track", update.effective_user.id)

    await update.message.reply_text(

        "📝 Функция добавления прочитанных страниц находится в разработке.\n"

        "Скоро вы сможете вводить название книги и текущую страницу!"

    )


async def recommend_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Заглушка для команды рекомендаций /recommend."""

    logger.info("Пользователь %s вызвал /recommend", update.effective_user.id)

    recommendation = (

        "📚 Рекомендация дня:\n\n"

        "«1984» — Джордж Оруэлл\n"

        "Жанр: Роман-антиутопия\n"

        "Описание: Классическое произведение о тоталитарном обществе."

    )

    await update.message.reply_text(recommendation)


async def stats_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    """Заглушка для команды статистики /stats."""

    logger.info("Пользователь %s вызвал /stats", update.effective_user.id)

    await update.message.reply_text(

        "📊 Ваша статистика:\n\n"

        "Книг прочитано в этом году: 0\n"

        "Текущая цель: 12 книг\n"

        "Всего прочитано страниц: 0"

    )

