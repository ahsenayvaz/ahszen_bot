import requests
import time

# Ayarlar
USERNAME = "ahszen"  # Takip etmek istediğin kullanıcı adı
CHECK_INTERVAL = 3600  # Kontrol aralığı (saniye cinsinden) -> 1 saat

# Telegram Bot Ayarları
TELEGRAM_TOKEN = "7772722232:AAFnHWnyJ5iZ29hXOXrNlVmlVsJC18N6Yl4"
TELEGRAM_CHAT_ID = "1528216898"

def check_username_availability(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    if response.status_code == 404:
        return True
    else:
        return False

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    requests.post(url, data=payload)

def main():
    while True:
        if check_username_availability(USERNAME):
            message = f"✅ Username '{USERNAME}' is now available on Instagram!"
            send_telegram_message(message)
            print(message)
            break
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()
