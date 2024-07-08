# pyTelegramBotWrapper

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/telebot_wrapper)
![GitHub Release](https://img.shields.io/github/v/release/HamletSargsyan/pyTelegramBotAPIWrapper)
![PyPI - Version](https://img.shields.io/pypi/v/pyTelegramBotApiWrapper)
![GitHub License](https://img.shields.io/github/license/HamletSargsyan/pyTelegramBotApiWrapper)


## Install

```bash
pip install --upgrade telebot_wrapper
```

## Examples

### Callback query
```python
from telebot.types import CallbackQuery,  Message
from telebot.util import quick_markup

from telebot_wrapper.utils import compress_string, decompress_string

TOKEN = ""
bot = Bot(token=TOKEN)


@bot.callback_query_handler(lambda call: decompress_string(call.data) == "any")
def handle_callback_query(call: CallbackQuery, parsed_data: list[str]):
    print("ANY")
    bot.send_message(call.message.chat.id, f"Any | Parsed data: {parsed_data}")

@bot.callback_query_handler(lambda call: True)
def callback_query(call: CallbackQuery, parsed_data: list[str]):
    print("default")
    bot.send_message(call.message.chat.id, f"Parsed data: {parsed_data}")
    
    
        
@bot.message_handler(func=lambda message: True)
def message_handler(message: Message):
    markup = quick_markup({
        "btn": {"callback_data": compress_string("any")}
    })
    
    bot.reply_to(message, "txt", reply_markup=markup)

if __name__ == "__main__":
    bot.infinity_polling()
```
