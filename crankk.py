import requests
import json

discord_webhook_url = 'https://discord.com/api/webhooks/<embded>'
url = "http://127.0.0.1:17080/wallet/balance"
authorization_key = ""

headers = {
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

headers["Authorization"] = f"Basic {authorization_key}"

response = requests.get(url, headers=headers, verify=False)

if response.status_code == 200:
    data = response.json()
    balance_0 = data['balance']['0']
    balance_19 = data['balance']['19']

    combined_kda = "{:.2f}".format(balance_0['kda'] + balance_19['kda'])
    combined_crkk = "{:.2f}".format(balance_0['crkk'] + balance_19['crkk'])

    payload = {
        "embeds": [
            {
                "title": "Crankk Wallet",
                "thumbnail": {"url": "https://i.imgur.com/LkrU6Vd.png"},
                "fields": [
                    {"name": "CRKK Balance", "value": f"{combined_crkk}"},
                    {"name": "KDA Balance", "value": f"{combined_kda}"}
                ],
                "color": 4930809
            },
        ],
    }

    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(discord_webhook_url, json=payload, headers=headers)
        response.raise_for_status()
        print("Discord webhook sent successfully")
    except requests.exceptions.RequestException as e:
        print(f"Error sending Discord webhook: {e}")
else:
    print("Failed to retrieve data:", response.status_code)
