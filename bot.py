import logging
import os
import asyncio
import argparse

from save_tools import download_comics
from aiogram import Dispatcher, Bot, types
from dotenv import load_dotenv


async def main():
    load_dotenv()

    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")

    tg_bot_token = os.getenv('TG_BOT_TOKEN')
    tg_chat_id = os.getenv('TG_CHAT_ID')

    bot = Bot(token=tg_bot_token)
    dp = Dispatcher()

    parser = argparse.ArgumentParser(description='Отправка комиксов в Телеграм-канал')
    parser.add_argument('--folder',
                        type=str,
                        default='Files',
                        help='Путь к директории с комиксом')

    args = parser.parse_args()
    comics_directory = args.folder

    comics_comment = download_comics()
    comics_files = os.listdir(comics_directory)

    first_file_path = os.path.join(comics_directory, comics_files[0])
    last_file_path = os.path.join(comics_directory, comics_files[-1])

    if not comics_files:
        logging.info(f'Папка {comics_directory} пуста.')
        return

    if len(comics_files) > 1:
        os.remove(last_file_path)

    try:
        with open(first_file_path, 'rb'):
            input_file = types.FSInputFile(first_file_path)
            await bot.send_photo(chat_id=tg_chat_id, photo=input_file, caption=comics_comment)
            logging.info(f'Отправка фотографии: {first_file_path}')

        os.remove(first_file_path)
    except Exception as e:
        logging.error(f"Ошибка при отправке фотографии {first_file_path}: {e}")

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

