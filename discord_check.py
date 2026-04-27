import requests


URL = "https://discord.com/api/v9/users/@me/pomelo-attempt"
HEADERS = {
    "Authorization": "Token_Here",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

username = input("Enter the username to check: ")

payload = {
    "username": username,
    "discriminator": "0000"
}
response = requests.post(URL, json=payload, headers=HEADERS)

print(response.json())
