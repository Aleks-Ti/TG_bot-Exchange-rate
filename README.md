# TG_bot-Exchange-rate

## Application Functions

Проект представляет собой бота для мессенджера Telegram,
разработанного с использованием фреймворка aiogram. Бот имеет следующие функции:

Присылать свежую информацию о курсе биткоина. Бот будет регулярно обновлять информацию,
если потребуеться, о курсе биткоина и отправлять ее пользователям.

Предоставлять курсы национальных валют, таких как доллар и евро.
Бот имеет возможность получать актуальные курсы валют и отправлять их пользователям по запросу.

## Others

Бот разработан с использованием фреймворка aiogram, который облегчает создание и управление ботами для Telegram.
Он предоставляет удобные инструменты для работы с API Telegram и обработки входящих сообщений.

Для запуска бота необходимо установить зависимости, указанные в файле requirements.txt, и настроить токен Telegram API.
Подробные инструкции по установке и настройке читаем ниже.


## Installation

Clone the TG_bot-Exchange-rate repository to your local machine.

```bash
git clone https://github.com/Aleks-Ti/TG_bot-Exchange-rate.git
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
```

Activate virtual environment:

```bash
source venv/Sourse/activate (windows) / source venv/bin/activate (unix)
```

Install dependencies from the file requirements.txt:

```bash
pip install -r requirements.txt
```

## Перед запуском

```bash
cd projectK/
```

For the bot to work, you need to create a file in the .env folder and specify two keys:

Telegram bot token (required!)
Account id (optionally(not necessarily))

```bash
TOKEN = "your TG token of the channel bot"
CHAT_ID = 0123456789  # your personal ID (optionally)
```

### Start

```bash
cd projectK/
```

```bash
python main.py
```

### Additionally

Так же можно прозвонить используемые api в проекте вручную,
и посмотреть структуру json ответа используемую в проекте:

Откройте файл requests.http и с помощью комбинаций клавишь ctrl + LMB

### License

TG_bot-Exchange-rate is released under the MIT License.
