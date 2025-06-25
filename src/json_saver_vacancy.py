import json
import os
from typing import List

from src.vacancy import Vacancy


class JSONSaver:
    def __init__(self, filename: str = "data/vacancies.json"):
        self.filename = filename

    def save_vacancies(self, vacancies: List[Vacancy]) -> None:
        """Сохраняет список вакансий в JSON файл (без перезаписи существующего)"""
        try:
            # Читаем существующие данные
            existing = self.load_vacancies()
            existing_dicts = [v.to_dict() for v in existing]

            # Добавляем новые
            new_dicts = [v.to_dict() for v in vacancies if v not in existing]
            combined = existing_dicts + new_dicts

            # Сохраняем обратно
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(combined, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Error saving vacancies: {e}")

    def load_vacancies(self) -> List[Vacancy]:
        """Загружает вакансии из JSON файла"""
        try:
            if not os.path.exists(self.filename):
                return []

            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                return [
                    Vacancy.from_dict(item) for item in data if isinstance(item, dict)
                ]
        except Exception as e:
            print(f"Error loading vacancies: {e}")
            return []

    def delete_vacancies(self) -> None:
        """Очищает файл с вакансиями (не трогает оригинальный)"""
        try:
            if not os.path.exists(self.filename):
                return

            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump([], f)
        except Exception as e:
            print(f"Error clearing vacancies: {e}")
