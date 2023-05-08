import poe
import os
from .options import *
from discord_webhook import DiscordWebhook
from dotenv import load_dotenv

load_dotenv()
options = app_options_parse()

language = options.language
topic = options.topic


WEBHOOK_URL = os.environ["WEBHOOK_URL"]
POE_TOKEN = os.environ["POE_TOKEN"]

client = poe.Client(POE_TOKEN)
webhook = DiscordWebhook(WEBHOOK_URL)

def prompt_text(topic, language):
    return """
    explain to me {topic} in {language} and the maximum characters should not exceed 200
    also make it simple and concise. I expect the format to be markdown
    """.format(topic=topic, language=language)

def prompt(bot, message):
    for chunk in client.send_message(bot, message):
        pass
    return chunk["text"]

def prompt_0xprog(message):
    return prompt("0xprog", message)



def main():
    text = prompt_text(topic, language)
    r = prompt_0xprog(text)
    webhook.set_content(r)
    webhook.execute()
    # send to the webhook


