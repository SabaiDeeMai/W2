import pytest

from src.json_saver_vacancy import JSONSaver
from src.vacancy import Vacancy


@pytest.fixture
def sample_vacancy():
    return Vacancy(
        name="Python Developer",
        url="https://hh.ru/vacancy/123",
        salary={"from": 100000, "to": 150000, "currency": "RUR"},
        description="Разработка на Python",
    )


@pytest.fixture
def sample_vacancies():
    return [
        Vacancy("Python Developer", "url1", {"from": 100000}, "Python experience"),
        Vacancy("Java Developer", "url2", {"from": 90000}, "Java experience"),
        Vacancy("DevOps Engineer", "url3", {"from": 120000}, "Docker experience"),
    ]


@pytest.fixture
def json_saver(tmp_path):
    test_file = tmp_path / "test_vacancies.json"
    return JSONSaver(str(test_file))
