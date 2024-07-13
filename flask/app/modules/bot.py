import logging
import discord
import threading
from discord.ext import commands

from ..config import TOKEN


log = logging.getLogger(__name__)


class DiscordBotSync(commands.Bot):
    """The discord bot object."""

    def __init__(self, command_prefix: str = None, **options) -> None:
        super().__init__(self, intents=discord.Intents.all(), **options)
        self.command_prefix = (
            command_prefix
            if commands.when_mentioned_or(command_prefix)
            else commands.when_mentioned_or("-")
        )
        

    def run_thread(self, token: str = TOKEN, **kwargs) -> None:
        thread = threading.Thread(
            target=super().run, args=(token,), kwargs=kwargs, daemon=True
        )
        thread.start()
        

    def load_data(self, data: dict) -> dict | None:
        userid = data["id"]
        user = self.get_user(userid)
        if user is not None:
            flags = [flag.name for flag in user.public_flags.all()]
            data.update(
                {
                    "username": user.name,
                    "avatar": user.avatar.url,
                    "url": user.jump_url,
                    "flags": flags,
                    "created_at": user.created_at.strftime("%Y-%m-%d %H:%M:%S")
                }
            )
            return data


bot = DiscordBotSync()
