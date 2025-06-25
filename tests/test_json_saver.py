import json
from unittest.mock import mock_open, patch

import pytest

from src.json_saver_vacancy import JSONSaver
from src.vacancy import Vacancy


@pytest.fixture
def original_data_file():
    """Фикстура с путем к оригинальному файлу данных"""
    return "data/vacancies.json"


@pytest.fixture
def saver_with_mock():
    """Фикстура создает saver с mock вместо реального файла"""
    with patch("builtins.open", mock_open()) as mock_file:
        saver = JSONSaver("data/vacancies.json")
        yield saver, mock_file


@pytest.fixture
def sample_vacancies():
    return [
        {
            "title": "Python Developer",
            "url": "http://example.com/1",
            "salary": {"from": 100000},
            "description": "Python",
        },
        {
            "title": "Java Developer",
            "url": "http://example.com/2",
            "salary": {"from": 80000},
            "description": "Java",
        },
    ]


def test_load_existing_vacancies(original_data_file):
    """Тест загрузки существующих вакансий без модификации файла"""
    saver = JSONSaver(original_data_file)
    vacancies = saver.load_vacancies()

    # Проверяем что загрузка работает и возвращает список
    assert isinstance(vacancies, list)
    if vacancies:  # Если файл не пустой
        assert all(isinstance(v, Vacancy) for v in vacancies)


def test_save_with_mock(saver_with_mock, sample_vacancies):
    """Тест сохранения с mock файлом"""
    saver, mock_file = saver_with_mock
    saver.save_vacancies([Vacancy.from_dict(v) for v in sample_vacancies])

    # Проверяем что файл пытались открыть для записи
    mock_file.assert_called_with("data/vacancies.json", "w", encoding="utf-8")


def test_load_with_mock(saver_with_mock, sample_vacancies):
    """Тест загрузки с mock данными"""
    saver, mock_file = saver_with_mock
    mock_file.return_value.read.return_value = json.dumps(sample_vacancies)

    vacancies = saver.load_vacancies()
    assert len(vacancies) == 2
    assert vacancies[0].title == "Python Developer"


def test_delete_with_mock(saver_with_mock):
    """Тест очистки с mock файлом"""
    saver, mock_file = saver_with_mock
    saver.delete_vacancies()

    # Проверяем что файл был перезаписан пустым списком
    mock_file.return_value.write.assert_called_with("[]")


@patch("builtins.open", side_effect=PermissionError("Access denied"))
def test_permission_errors(mock_open):
    """Тест обработки ошибок доступа"""
    saver = JSONSaver("data/vacancies.json")

    # Проверяем что методы не падают при ошибках доступа
    assert saver.load_vacancies() == []
    saver.save_vacancies([])  # Не должен вызывать исключение
    saver.delete_vacancies()  # Не должен вызывать исключение
