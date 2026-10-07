from dataclasses import dataclass

from typing import Optional


@dataclass

class Book:

    """Модель сущности книги."""

    title: str

    author: str

    total_pages: int

    current_page: int = 0

    status: str = "не начато"

    def get_progress_percentage(self) -> float:

        """Возвращает процент прочитанного текста."""

        if self.total_pages == 0:

            return 0.0

        return round((self.current_page / self.total_pages) * 100, 2)


@dataclass

class UserProfile:

    """Модель профиля пользователя."""

    user_id: int

    username: Optional[str] = None

    target_books_per_year: int = 12

