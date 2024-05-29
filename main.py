import os
from datetime import datetime
from pathlib import Path

import requests
from apscheduler.schedulers.blocking import BlockingScheduler
from dotenv import load_dotenv
from PyPtt import PTT

load_dotenv()


def log(*messages, console: bool = False):
    """Basic Log to Record Progress.

    Args:
        `messages`: Logging message.
    """

    log_path = Path('log')
    log_path.mkdir(parents=True, exist_ok=True)

    today = datetime.now().strftime('%Y-%m-%d') + '.log'

    file_path = Path(log_path, today)

    with open(file_path, 'a', encoding='utf-8') as f:
        print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), *messages, file=f)

    if console:
        print(messages)


def send_message(cid, message):
    """Send message to Telegram.

    Args:
        `cid`: Chat ID.
        `message`: Message to send.

    Returns:
        True if success, False if fail.
    """

    token = os.environ.get("tg_token")

    url = (
        'https://api.telegram.org/bot{}'
        '/sendMessage?chat_id={}&parse_mode=HTML&text={}'.format(
            token, cid, message
        )
    )

    res = requests.get(url)

    log(
        '[telegram_lib]',
        f'send message: {res.status_code} {res.text}',
    )


def login(ptt_username: str, ptt_password: str, chat_id: str):

    ptt = PTT.API(log_level=PTT.log.INFO)
    log(ptt_username, ptt_password, chat_id)

    try:
        ptt.login(ptt_username, ptt_password, kick_other_session=True)
        log("[ptt]", f"Login Success: {ptt_username}")
    except Exception as e:
        log("[ptt]", str(e))
        send_message(
            chat_id, f"PTT {ptt_username} Login Fail\nError: {str(e)}"
        )
        return
    else:
        username = ptt.get_user(ptt_username)
        response_message = (
            f"PTT {ptt_username} Login Success\nLogin Count:"
            f" {username.get('login_count')}"
        )
        ptt.logout()

        send_message(chat_id, response_message)


def main():
    scheduler = BlockingScheduler(timezone="Asia/Taipei")

    scheduler.add_job(
        login,
        trigger="cron",
        hour=11,
        minute=30,
        args=[
            os.environ.get("ptt_username"),
            os.environ.get("ptt_password"),
            os.environ.get("tg_chat_id"),
        ],
    )

    scheduler.start()


if __name__ == "__main__":
    main()
