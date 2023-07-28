import logging
import os
from http import HTTPStatus
from aiogram.dispatcher.filters.state import State, StatesGroup
import requests
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from bitarray import bitarray
from stiker import STIKER_ANGRY_HACKER, STIKER_FANNY_HACKER
import re
import json
import datetime as dt
import asyncio as asin

load_dotenv()


logging.basicConfig(
    format='%(asctime)s - %(funcName)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    filename=os.path.join(os.path.dirname(__file__), 'program.log'),
    encoding='utf-8',
)


TELEGRAM_TOKEN = os.getenv('TOKEN')
TELEGRAM_CHAT_ID = os.getenv('CHAT_ID')

RETRY_PERIOD = 10  # Период обращения


storage = MemoryStorage()
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot, storage=storage)


class ByteState(StatesGroup):
    """Машина состояния.

    Сохранение пользовательского ввода для конвертации в байт код.
    """

    name = State()


class ConvertState(StatesGroup):
    """Машина состояния.

    Сохранение пользовательского ввода для конвертации байт кода в utf-8.
    """

    name = State()


def convert_byte(words: str) -> bytes:
    """Ковнертирование любового символа входящих данных в байт код."""
    return ' '.join(format(x, '08b') for x in bytearray(words, 'utf-8'))


def transcript_byte(code: str) -> str:
    """Перевод байт кода в человекочитаемый формат."""
    try:
        bts = bitarray(code)
        symbol_utf = bts.tobytes().decode('utf-8')
        return symbol_utf
    except BaseException:
        return (
            'Увы! Но данные не являются двоичным '
            'кодом!\nПопробуйте ещё раз!'
        )


@dp.message_handler(commands=['byte'])
async def byte_message(message: types.Message):
    """Пользовательский ввод и состояние для конвертации."""
    await ByteState.name.set()
    await message.reply(
        'Введите ваше слово или имя, для конвертации '
        'его в машинное представление 🦾'
    )

    # await bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=text)


@dp.message_handler(commands=['transcript'])
async def transcript(message: types.Message):
    """Пользовательский ввод и состояние для дешифрации."""
    await ConvertState.name.set()
    await message.reply('Введите машинный код 📟 для дешифрации___ ')


@dp.message_handler(state=ConvertState.name)
async def process_transcript(message: types.Message, state: FSMContext):
    """Отправка сообщения с данными конвертации байт кода в utf-8"""
    chat_id = message.from_user.id
    await state.finish()

    messages = transcript_byte(message.text)
    await bot.send_message(
        chat_id=chat_id,
        text='Лучшие ученые мира принялись за расшифровку! 🧮🧮🧮',
    )
    await asin.sleep(3.5)
    await bot.send_sticker(
        chat_id=chat_id,
        sticker=STIKER_ANGRY_HACKER,
    )
    await asin.sleep(3)
    await bot.send_message(chat_id=chat_id, text='Получение данных ⚙️⚙️⚙️')
    await asin.sleep(3)
    await bot.send_message(
        chat_id=chat_id,
        text=f'Вернулся ответ. Читаем!\nРезультат'
        f':\n\t\t\t\t\t\t\t\t\t->\t\t\t{messages}',
    )


@dp.message_handler(state=ByteState.name)
async def process_name(message: types.Message, state: FSMContext):
    """Отправка сообщения с данными конвертированными в байт код."""
    chat_id = message.from_user.id
    await state.finish()
    messages = convert_byte(message.text)
    await bot.send_message(
        chat_id=chat_id,
        text='Происходит запрос 📡 на главные сервера планеты 📟📟📟',
    )
    await asin.sleep(3)
    await bot.send_sticker(
        chat_id=chat_id,
        sticker=STIKER_FANNY_HACKER,
    )
    await asin.sleep(3)
    await bot.send_message(chat_id=chat_id, text='Получение данных ⚙️⚙️⚙️')
    await asin.sleep(3)
    await bot.send_message(chat_id=chat_id, text=messages)


def get_api_answer_bit():
    """Запрос к Api курса БИТКА"""
    if (
        requests.get(
            'https://api.coindesk.com/v1/bpi/currentprice.json'
        ).status_code
        != HTTPStatus.OK
    ):
        logging.error('Сервис не доступен!')
        raise ConnectionError('Service status != 200')
    try:
        return requests.get(
            'https://api.coindesk.com/v1/bpi/currentprice.json'
        ).json()
    except Exception:
        logging.exception('ЖОПА')


def get_api_answer_cb():
    """Запрос к Api Центрального банка РФ"""
    if (
        requests.get('https://www.cbr-xml-daily.ru/daily_json.js').status_code
        != HTTPStatus.OK
    ):
        logging.error('Сервис ЦБ не доступен!')
        raise ConnectionError('Service CB status != 200')
    try:
        return requests.get(
            'https://www.cbr-xml-daily.ru/daily_json.js'
        ).json()
    except Exception:
        logging.exception('ЖОПА в ЦБ')


def parse_data_cb(data: dict) -> str:
    """Распарс json ЦБ()."""
    if 'Valute' in data:
        сurrency = data['Valute']

        currency_VND_name = сurrency['VND']['Name']
        currency_VND_now = сurrency['VND']['Value']

        currency_GBP_name = сurrency['GBP']['Name']
        currency_GBP_now = сurrency['GBP']['Value']

        currency_USD_name = сurrency['USD']['Name']
        currency_USD_now = сurrency['USD']['Value']

        currency_EUR_name = сurrency['EUR']['Name']
        currency_EUR_now = сurrency['EUR']['Value']

        currency_CNY_name = сurrency['CNY']['Name']
        currency_CNY_now = сurrency['CNY']['Value']
        message = (
            f'Выяснил 🧑‍💻:\n'
            f'{currency_USD_name}. Стоимость: {currency_USD_now}.\n'
            f'{currency_EUR_name}. Стоимость: {currency_EUR_now}.\n'
            f'{currency_CNY_name}. Стоимость: {currency_CNY_now}.\n'
            f'{currency_GBP_name}. Стоимость: {currency_GBP_now}.\n'
            f'{currency_VND_name}.🤣 Стоимость: {currency_VND_now}.😳\n'
        )
        return message
    logging.error('Изменился json получаемый от API.')
    raise Exception('Жопа ЦБ')


def parse_data_bt(data: dict) -> str:
    """Распарс json битка()."""
    try:
        now_time = data['time']['updated']
        currency_name = data['chartName']
        usd_currency_price = data['bpi']['USD']['rate']
        eur_currency_price = data['bpi']['EUR']['rate']

        message = (
            f'На сегодня - {now_time} стоимость {currency_name} составляет: \n'
            f'USD - {usd_currency_price}.\nEUR - {eur_currency_price} '
        )
        return message
    except Exception:
        logging.exception('Че-то с распарсом json Bitcoin')


@dp.message_handler(commands=['kurs'])
async def send_message_(message: types.Message):
    """Отправка сообщения о курсе национальных валют."""
    chat_id = message.from_user.id
    data = get_api_answer_cb()
    text = parse_data_cb(data)

    await bot.send_message(chat_id=chat_id, text=text)


@dp.message_handler(commands=['bit'])
async def send_message(
    message: types.Message,
):
    """Отправка сообщения о курсе битка."""
    chat_id = message.from_user.id
    data = get_api_answer_bit()
    text = parse_data_bt(data)

    await bot.send_message(chat_id=chat_id, text=text)


@dp.message_handler(commands=['*'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton(text='/bit')
    button_1 = types.KeyboardButton(text='/kurs')
    button_2 = types.KeyboardButton(text='/byte')
    button_3 = types.KeyboardButton(text='/transcript')
    keyboard.add(button, button_1, button_2, button_3)

    await message.reply(
        'Привет!\nИнфа по битку 🤞 -жми-> /bit'
        '\nИнфа по гос.валютам к рублю 💸 -> /kurs'
        '\nА если хочешь увидеть, как выглядит любой символ, '
        'или мб твоё имя в байтовом представлении - жми -> /byte\n'
        '\nИли нажми на кнопки внизу 👇🥶👇',
        reply_markup=keyboard,
    )


FILE_PATH = "projectK/links.json"


@dp.message_handler()
async def handle_all_messages(message: types.Message):
    """Если сообщение в чате ссылка, то..."""
    if links := re.findall(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
        message.text,
    ):
        save_links(message.message_id, links)
        await message.reply("Захавал!")


def save_links(message_id, links):
    """Сохранение ссылки в файл."""
    try:
        with open(FILE_PATH, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data[str(dt.date.today())] = links

    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
