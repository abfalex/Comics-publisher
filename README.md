# Comics publisher

This project implements a TG bot that sends a random xkcd comic upon startup.

## Installation

1. Make sure you have Python installed. You can download it from [official website](https://www.python.org/downloads/).

2. Download or clone the repository:

   ```bash
   git clone https://github.com/abfalex/Comics-publisher.git
   ```

3. Create a virtual environment (recommended):

   ```bash
   python -m venv <venv_name>
   ```

4. Activate the virtual environment:

  - On Windows:

     ```bash
     <venv_name>\Scripts\activate
     ```

- On macOS and Linux:

     ```bash
     source <venv_name>/bin/activate
     ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Create a `.env` file in the root of the project and add to it the token from your TG bot, as well as the telegram channel tag:

```
TG_BOT_TOKEN=tg_bot_token
TG_CHAT_ID=@tg_channel_tag
```

## Launch
Before launching, you must add your telegram bot to a telegram channel or group, giving it admin rights.

To start you need to enter:

```bash
python bot.py
```

Extra options:
- --folder <folder_name>

This parameter is required if you do not yet have a comic book directory created. If you do not specify this parameter or enter a non-existent directory name, there will be no error and the folder will be created automatically.

Example with extra option `--folder`:

```bash
python bot.py --folder Comics
```

## Results
After launching the bot, an automatic message with a comic and a comment from the author will be sent to your Telegram channel.
