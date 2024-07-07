from functools import wraps
from typing import Callable
from telebot import TeleBot
from telebot.types import CallbackQuery

from utils import decompress_string


class Bot(TeleBot):
    def __init__(self, token: str, *args, **kwargs):
        super().__init__(token, *args, **kwargs)

    def callback_query_handler(self, *args, **kwargs):
        def decorator(func: Callable[[CallbackQuery, list[str]], None]):
            @wraps(func)
            def wrapper(call: CallbackQuery):
                call.data = decompress_string(call.data)
                data_list = call.data.split(";")
                return func(call, data_list)

            handler = super(Bot, self).callback_query_handler(*args, **kwargs)(wrapper)
            return handler

        return decorator
