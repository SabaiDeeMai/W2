import pytest

from src.vacancy import Vacancy


def test_vacancy_creation():
    """Тест создания вакансии с корректными данными"""
    vacancy = Vacancy(
        title="Python Developer",
        url="https://hh.ru/vacancy/123",
        salary={"from": 100000, "to": 150000, "currency": "RUR"},
        description="Требуется опыт работы с Python",
    )
    assert vacancy.title == "Python Developer"
    assert vacancy.url == "https://hh.ru/vacancy/123"
    assert vacancy.salary["from"] == 100000


def test_vacancy_validation():
    """Тест валидации некорректных данных"""
    with pytest.raises(ValueError):
        Vacancy(
            title=123, url="invalid", salary=None, description=""
        )  # Неправильный тип title

    with pytest.raises(ValueError):
        Vacancy(
            title="Valid", url=123, salary=None, description=""
        )  # Неправильный тип url


def test_get_salary_from():
    """Тест метода get_salary_from()"""
    v1 = Vacancy("A", "http://example.com", {"from": 100}, "")
    v2 = Vacancy("B", "http://example.com", None, "")
    assert v1.get_salary_from() == 100
    assert v2.get_salary_from() == 0


def test_vacancy_comparison():
    """Тест сравнения вакансий"""
    v1 = Vacancy("A", "http://example.com", {"from": 100}, "")
    v2 = Vacancy("B", "http://example.com", {"from": 200}, "")
    assert v1 < v2
    assert v2 > v1
