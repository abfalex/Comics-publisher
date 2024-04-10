import requests
import logging
import random
import os


def download_file(url, folder_path, file_path):
    response = requests.get(url)
    response.raise_for_status()

    os.makedirs(folder_path, exist_ok=True)

    with open(f"{folder_path}/{file_path}", 'wb') as file:
        file.write(response.content)


def download_comics():
    comics_number = random.randint(1, 2917)
    comics_title = f"comics_{comics_number}.png"

    url = f"https://xkcd.com/{comics_number}/info.0.json"

    response = requests.get(url)
    response.raise_for_status()

    if not response.ok:
        return logging.error(f'Ошибка при обработке запроса {url}', exc_info=True)

    comics_image_url = response.json().get("img", "")
    comics_comment = response.json().get("alt", "")

    download_file(
        url=comics_image_url,
        folder_path="Files",
        file_path=comics_title
    )

    return comics_comment
