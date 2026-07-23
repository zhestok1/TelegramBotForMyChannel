# 🤖 Matershinik Bot

**Telegram-бот с искусственным интеллектом, который высмеивает стикеры, защищает создателя и принимает донаты через Telegram Stars**

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![aiogram](https://img.shields.io/badge/aiogram-3.x-blue.svg)](https://docs.aiogram.dev/)
[![OpenRouter](https://img.shields.io/badge/OpenRouter-API-green.svg)](https://openrouter.ai/)

---

## 🎯 Возможности

### 1. 📸 Высмеивание стикеров
Отправьте стикер в чат или личные сообщения — бот сгенерирует язвительный ответ через нейросеть.

### 2. 🛡️ Защита создателя
Бот анализирует эмоциональный окрас сообщений:
- **Позитивные и нейтральные** → дружелюбный ответ
- **Негативные и критические** → аргументированный отпор с защитой создателя

### 3. 💬 Работа в комментариях
Бот обрабатывает сообщения в группах и комментарии к постам канала. Сообщения в канале игнорируются.

### 4. 📝 Анализ контекста
Бот определяет эмоциональный тон сообщения и адаптирует стиль ответа.

### 5. ⭐ Поддержка проекта
Приём донатов через Telegram Stars. Пользователи могут поддержать проект, выбрав сумму от 10 до 200 звёзд.

---

## 🛠️ Технологии

- **Python 3.10+** — основной язык
- **aiogram 3.x** — асинхронный фреймворк для Telegram
- **OpenRouter API** — доступ к нейросетям (GPT-3.5-turbo)
- **Telegram Stars** — приём донатов
- **python-dotenv** — управление переменными окружения
- **Railway** — хостинг и деплой

---

## 🚀 Быстрый старт

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