from telethon import TelegramClient, events
from telethon.events import NewMessage
from dotenv import load_dotenv
import os
import requests
load_dotenv()
api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("TOKEN")


api_link = "http://127.0.0.1:8000"
bot = TelegramClient('anon', api_id, api_hash).start(bot_token=bot_token)


@bot.on(NewMessage(pattern = r'\.help'))
async def responseHelp(event):
    await event.reply("""
        GET METHODS - .get all | .get air | .get sea | .get land
        CREATE METHODS - .create sea | .create air | .create land
    """)
@bot.on(NewMessage(pattern=r"\.get"))
async def respondGet(event):
    text = event.raw_text
    response = "invalid. type '.help' for help"
    if "all" in text:
        response = get_from_api(f"{api_link}/get/all")
    elif "air" in text:
        response = get_from_api(f"{api_link}/get/air")
    elif "sea" in text:
        response = get_from_api(f"{api_link}/get/sea")
    elif "land" in text:
        response = get_from_api(f"{api_link}/get/land")
    await event.reply(str(response))

@bot.on(NewMessage(pattern=r"\.create"))
async def respondCreate(event):
    text : str = event.raw_text
    r = "invalid. type '.help' for help"
    if "air" in text:
        r = create_animal("air", text)
    elif "sea" in text:
        r = create_animal("sea", text)
    elif "land" in text:
        r = create_animal("land", text)

    await event.reply(str(r))
def get_from_api(url):
    response = requests.get(url)
    return response.json()

def create_from_api(url, attrs):
    u = f"{url}?animalType={attrs.pop('type')}"
    response = requests.post(u, json=attrs)
    return response.text
def create_animal(environment, text):
    attributes = {}
    text = text.replace(f".create {environment}", "")
    # Extract attributes and values from the message
    for part in text.split(","):
        key_value = part.strip().split("=")
        if len(key_value) == 2:
            attributes[key_value[0].strip()] = key_value[1].strip()

    # Check if required attributes are present
    required_attributes = ["name", "type", "color", "size", "gender"]
    if all(attr in attributes for attr in required_attributes):
        # Prepare the API request
        api_request = f"{api_link}/create/{environment}"
        response = create_from_api(api_request, attributes)
    else:
        response = f"Missing required attributes for {environment}. Format should be: .create {environment} name=bob, type=Tiger, color=brown, size=52.1, gender=male"

    return response
bot.start()
bot.run_until_disconnected()
