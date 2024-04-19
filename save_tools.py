import requests
import logging
import random
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def download_and_save_file(url, folder_path, file_name):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(os.path.join(folder_path, file_name), 'wb') as file:
            file.write(response.content)
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to download and save file from {url}: {e}", exc_info=True)


def get_comic_info(comic_number):
    comic_url = f"https://xkcd.com/{comic_number}/info.0.json"
    try:
        response = requests.get(comic_url)
        response.raise_for_status()
        comic = response.json()

        comic_image_url = comic.get("img", "")
        comic_comment = comic.get("alt", "")

        return comic_image_url, comic_comment
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to fetch comic info from {comic_url}: {e}", exc_info=True)
        return None, None


def save_comic(directory_path):
    try:
        number_first_comic = 1
        latest_comic_number = 2917

        comic_number = random.randint(number_first_comic, latest_comic_number)
        comic_title = f"comic_{comic_number}.png"

        comic_image_url, comic_comment = get_comic_info(comic_number)

        if comic_image_url:
            download_and_save_file(
                url=comic_image_url,
                folder_path=directory_path,
                file_name=comic_title
            )
            return comic_comment
    except requests.exceptions.RequestException as e:
        logging.error(f"An error occurred while downloading comic: {e}", exc_info=True)
        return None
