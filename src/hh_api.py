from typing import Any, Dict, Optional

import requests

from src.vacancy import Vacancy


class HHAPI:
    BASE_URL = "https://api.hh.ru/vacancies"

    def __init__(self):
        self.params = {"text": "", "per_page": 100, "page": 0, "only_with_salary": True}

    def _connect_to_api(self) -> Optional[Dict[str, Any]]:
        """Приватный метод подключения к API"""
        try:
            response = requests.get(self.BASE_URL, params=self.params, timeout=10)
            response.raise_for_status()
            return response.json()
        except (requests.RequestException, ValueError) as e:
            print(f"API connection error: {e}")
            return None

    def load_vacancies(self, query: str) -> list[Vacancy]:
        """Загружает вакансии по поисковому запросу"""
        self.params["text"] = query
        self.params["page"] = 0
        try:
            data = self._connect_to_api()
            if not data or not isinstance(data.get("items"), list):
                return []

            vacancies = []
            for item in data["items"]:
                try:
                    vacancies.append(Vacancy.from_dict(item))
                except ValueError as e:
                    print(f"Ошибка создания вакансии: {e}")
                    continue

            return vacancies
        except Exception as e:
            print(f"Ошибка при загрузке вакансий: {e}")
            return []
