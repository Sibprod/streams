import requests

url = "https://www.france.tv/france-2/direct.html"
data = {
    "username": "sibalden@gmail.com"
    "password": "@GuiWaf1705"
}

response = requests.post(url, data=data)

if response.status_code = 200
    # L'authentification a réussi, tu peux ensuite extraire le jeton d'authentification et continuer le reste du processus.
        token = response.json().get("token")
else:
        print("playlist.m3u8")