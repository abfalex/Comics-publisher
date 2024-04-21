import requests
import logging
import random
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def save_comic(folder_path):
    number_first_comic = 1
    latest_comic_number = 2917

    comic_number = random.randint(number_first_comic, latest_comic_number)
    comic_image_url, comic_comment = get_comic_info(comic_number)
    comic_title = f"comic_{comic_number}.png"

    response = requests.get(comic_image_url)
    response.raise_for_status()

    with open(os.path.join(folder_path, comic_title), 'wb') as file:
        file.write(response.content)

    if comic_image_url:
        return comic_comment


def get_comic_info(comic_number):
    comic_url = f"https://xkcd.com/{comic_number}/info.0.json"
    response = requests.get(comic_url)
    response.raise_for_status()
    comic = response.json()

    comic_image_url = comic.get("img", "")
    comic_comment = comic.get("alt", "")

    return comic_image_url, comic_comment
