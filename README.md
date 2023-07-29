# TG_bot-Exchange-rate

## Application Functions

The project is a bot for the Telegram messenger,
developed using the aiogram framework. The bot has the following functions:

Send the latest information about bitcoin exchange rate. The bot will update the information regularly,
if necessary, about bitcoin exchange rate and send it to users.

Provide rates of national currencies such as dollar and euro.
The bot has the ability to get up-to-date exchange rates and send them to users upon request.

## Others

The bot is developed using the aiogram framework, which makes it easy to create and manage bots for Telegram.
It provides convenient tools for working with Telegram API and processing incoming messages.

To run the bot, you need to install the dependencies specified in the requirements.txt file and configure the Telegram API token.
Detailed instructions on installation and configuration can be found below.

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

You can also call the api used in the project manually,
and see the json response structure used in the project:

Open the requests.http file and use the ctrl + LMB key combinations

### License

TG_bot-Exchange-rate is released under the MIT License.
