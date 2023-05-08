import poe
import os
from .options import *
from .webhook import *

options = app_options_parse()

webhook = options.webhook
language = options.language
topic = options.topic


POE_TOKEN = os.environ["POE_TOKEN"]

client = poe.Client(POE_TOKEN)

def prompt_text(topic, language):
    return """
    explain to me {topic} in {language} and the maximum characters should not exceed 200
    also make it simple and concise. I expect the format to be markdown
    """.format(topic=topic, language=language)

def prompt(bot, message):
    for chunk in client.send_message(bot, message):
        pass
    return chunk["text"]


def boot():
    for key in client.bot_names:
        globals()[f"prompt_{key}"] = lambda message: prompt(key, message)

def main():
    boot()
    text = prompt_text(topic, language)
    r = prompt_0xprog(text)
    content = webhook_builder(r)

    # send to the webhook


