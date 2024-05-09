import json
from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
import time
from pydo import Client


def get_second():
    return int(str(int(time.time()))[-1]) # see this logic ? its so complex. yet so simple

logo_link = "https://raw.githubusercontent.com/SurajBhari/droplet_maitainer/main/256_droplet_maintainer.png"
project_name = "Droplet Maintainer"
count = 1
last_second = get_second()

while True:
    while last_second == get_second():
        time.sleep(0.1)
    last_second = get_second()
    config = json.load(open('config.json', "r"))
    for instance in config.keys():
        if count % config[instance]['interval'] != 0:
            print(f"{count}. Not time to check {instance}...")
            continue # Skip if not time to check
        print(f"Checking {instance}...")
        location = config[instance]['location']
        url = location['url']
        headers = location['headers']
        tolerance = config[instance]['tolerance']
        timeout = location['timeout']
        ok = False
        while tolerance > 0:
            time.sleep(1)
            try:
                response = requests.get(url, headers=headers, timeout=timeout)
            except Exception as e:
                print(f"{instance} is down!")
                tolerance -= 1
                continue
            if response.status_code == location["response_code"]:
                print(f"{instance} Responded with correct code!")
                ok = True
                break
            print(f"{instance} said {response.status_code}!")
            tolerance -= 1
        if ok:
            continue
        if config[instance]['discord']:
            embed = DiscordEmbed(
                title=f"{url} is down!", 
                color=0xf54242,
                description=f"{instance} is down! Restarting now..."
            )
            webhook = DiscordWebhook(
                username = project_name, 
                avatar_url=logo_link, 
                url=config[instance]['discord'], 
                embeds=[embed]
            )
            response = webhook.execute()
        droplet = client = Client(token=config[instance]['digitalocean_token']) 
        # insert code for restarting the droplet here
        if config[instance]['discord']:
            embed = DiscordEmbed(
                title=f"{instance} has been restarted!", 
                color=0x00ab00,
            )
            webhook = DiscordWebhook(
                username = project_name,
                avatar_url=logo_link,
                url=config[instance]['discord'], 
                embeds=[embed]
            )
            response = webhook.execute()

    count += 1

