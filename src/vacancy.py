from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class Vacancy:
    __slots__ = ("title", "url", "salary", "description")

    title: str
    url: str
    salary: Optional[Dict[str, Any]]
    description: str

    def __post_init__(self):
        self._validate_data()

    def _validate_data(self):
        """Валидация данных при инициализации"""
        if not isinstance(self.title, str):
            raise ValueError("Title must be a string")
        if not isinstance(self.url, str):
            raise ValueError("URL must be a string")
        if self.salary and not isinstance(self.salary, dict):
            raise ValueError("Salary must be a dictionary or None")

    def get_salary_from(self) -> int:
        """Возвращает нижнюю границу зарплаты или 0"""
        if not self.salary or not isinstance(self.salary, dict):
            return 0
        salary_from = self.salary.get("from")
        return int(salary_from) if salary_from is not None else 0

    def __lt__(self, other) -> bool:
        """Сравнение вакансий по зарплате (меньше)"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.get_salary_from() < other.get_salary_from()

    def __gt__(self, other) -> bool:
        """Сравнение вакансий по зарплате (больше)"""
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.get_salary_from() > other.get_salary_from()

    def to_dict(self) -> Dict[str, Any]:
        """Конвертация в словарь"""
        return {
            "title": self.title,
            "url": self.url,
            "salary": self.salary,
            "description": self.description,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Создание объекта из словаря"""
        return cls(
            title=data.get("title") or data.get("name", ""),
            url=data.get("url") or data.get("alternate_url", ""),
            salary=data.get("salary"),
            description=data.get("description")
            or data.get("snippet", {}).get("requirement", ""),
        )
