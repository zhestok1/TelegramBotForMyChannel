# Matershinik Bot

**Telegram-бот с искусственным интеллектом, который высмеивает стикеры и защищает создателя**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![aiogram](https://img.shields.io/badge/aiogram-3.x-blue.svg)](https://docs.aiogram.dev/)
[![OpenRouter](https://img.shields.io/badge/OpenRouter-API-green.svg)](https://openrouter.ai/)

---

## Возможности

### 1. **Высмеивание стикеров**
Бот распознаёт стикеры в любых чатах и генерирует язвительные, саркастичные ответы через нейросеть.

### 2. **Защита создателя**
Анализирует эмоциональный окрас текстовых сообщений:
- **Позитив/нейтрал** → дружелюбное общение
- **Негатив/критика** → жёсткий ответ с защитой создателя

### 3. **Работает везде**
- Личные сообщения (Private)
- Группы (Group)
- Супергруппы (Supergroup)

---

## Технологии

- **Python 3.10+** — основной язык
- **aiogram 3.x** — асинхронный фреймворк для Telegram
- **OpenRouter API** — доступ к GPT-3.5-turbo (бесплатно)
- **python-dotenv** — управление переменными окружения
- **httpx** — асинхронные HTTP-запросы

---

## Быстрый старт

### Установка

```bash
# Клонируйте репозиторий
git clone https://github.com/ваш-логин/BotMatershink.git
cd BotMatershink

# Создайте виртуальное окружение
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate     # Windows

# Установите зависимости
pip install -r requirements.txt