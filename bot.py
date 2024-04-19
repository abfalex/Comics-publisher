import logging
import os
import asyncio
import argparse

from save_tools import save_comic
from aiogram.exceptions import TelegramAPIError
from aiogram import Dispatcher, Bot, types
from dotenv import load_dotenv


async def main():
    load_dotenv()

    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")

    tg_bot_token = os.environ['TG_BOT_TOKEN']
    tg_chat_id = os.environ['TG_CHAT_ID']

    bot = Bot(token=tg_bot_token)
    dp = Dispatcher()

    parser = argparse.ArgumentParser(description='Отправка комиксов в Телеграм-канал')
    parser.add_argument('--folder',
                        type=str,
                        default='Files',
                        help='Путь к директории с комиксом')

    args = parser.parse_args()
    comic_directory = args.folder

    os.makedirs(comic_directory, exist_ok=True)

    comic_comment = save_comic(comic_directory)
    comic_files = os.listdir(comic_directory)

    first_file_path = os.path.join(comic_directory, comic_files[0])

    try:
        with open(first_file_path, 'rb'):
            input_file = types.FSInputFile(first_file_path)
            await bot.send_photo(chat_id=tg_chat_id, photo=input_file, caption=comic_comment)
            logging.info(f'Submitting a comic: {first_file_path}')
    except TelegramAPIError as e:
        logging.error(f"Error sending comic {first_file_path}: {e}")
    finally:
        os.remove(first_file_path)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

