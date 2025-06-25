# Парсер вакансий с HeadHunter

## Полная документация функций

### Модули

class Vacancy:
    Класс для представления и работы с вакансиями
    
    Атрибуты:
        title (str): Название вакансии
        url (str): Ссылка на вакансию
        salary (dict): Зарплата в формате {'from': int, 'to': int, 'currency': str}
        description (str): Описание вакансии
        
    Методы:
        __init__(self, title, url, salary, description):
            Инициализирует объект вакансии с валидацией данных
            
        _validate_data(self):
            Проверяет корректность переданных данных:
            - title должен быть строкой
            - url должен быть строкой и начинаться с http
            - salary должен быть словарем или None
            
        get_salary_from(self) -> int:
            Возвращает нижнюю границу зарплаты или 0 если не указана
            
        to_dict(self) -> dict:
            Преобразует объект вакансии в словарь
            
        from_dict(cls, data) -> Vacancy:
            Создает объект Vacancy из словаря данных

class HHAPI:
    Класс для работы с API HeadHunter
    
    Методы:
        __init__(self):
            Инициализирует параметры запроса
            
        _connect_to_api(self) -> dict:
            Приватный метод для отправки запроса к API
            
        load_vacancies(self, query: str) -> list[Vacancy]:
            Загружает вакансии по поисковому запросу
            Возвращает список объектов Vacancy

class JSONSaver:
    Класс для сохранения и загрузки вакансий в JSON
    
    Методы:
        __init__(self, filename='vacancies.json'):
            Инициализирует путь к файлу
            
        save_vacancies(self, vacancies: list[Vacancy]):
            Сохраняет список вакансий в JSON файл
            
        load_vacancies(self) -> list[Vacancy]:
            Загружает вакансии из JSON файла
            
        delete_vacancies(self):
            Очищает файл с вакансиями

def filter_vacancies(vacancies: list[Vacancy], keywords: str) -> list[Vacancy]:
    Фильтрует вакансии по ключевым словам
    
    Аргументы:
        vacancies: Список объектов Vacancy
        keywords: Строка с ключевыми словами через пробел
        
    Возвращает:
        Отфильтрованный список вакансий

def sort_vacancies(vacancies: list[Vacancy]) -> list[Vacancy]:
    Сортирует вакансии по зарплате (по убыванию)
    
    Использует метод get_salary_from() объектов Vacancy

def get_top_vacancies(vacancies: list[Vacancy], top_n: int) -> list[Vacancy]:
    Возвращает топ N вакансий
    
    Аргументы:
        vacancies: Список вакансий
        top_n: Количество вакансий для возврата

def print_vacancies(vacancies: list[Vacancy]):
    Выводит вакансии в читаемом формате
    
    Формат вывода:
        1. Название вакансии
        2. Зарплата (от-до валюта)
        3. Описание
        4. Ссылка
    
def user_interaction():
    Основная функция взаимодействия с пользователем
    
    Логика работы:
        1. Получает поисковый запрос
        2. Загружает вакансии через HHAPI
        3. Сохраняет в JSON
        4. Фильтрует по ключевым словам (если нужно)
        5. Сортирует по зарплате
        6. Выводит топ-N вакансий