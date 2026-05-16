import requests
import time

TOKEN = "8966942896:AAFtG3fx7k0AlBb-UZyRpGjj8_SjhL3P7rg"
CHAT_ID = "-1003913508774"
URL = "https://api.rapira.net/open/market/rates"


def get_prices():
    try:
        response = requests.get(URL, timeout=10)
        data = response.json()["data"]

        result = "📊 Курсы:\n\n"

        for item in data:
            symbol = item.get("symbol", "")

            if "/USDT" in symbol:
                coin = symbol.split("/")[0]

                ask = item.get("askPrice", "—")
                bid = item.get("bidPrice", "—")

                result += f"❗️ {coin}\n"
                result += f"USDT → {coin}: {ask}\n"
                result += f"{coin} → USDT: {bid}\n\n"

        return result

    except Exception as e:
        return f"Ошибка получения данных: {e}"


def send_message(text):
    try:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

        requests.post(url, data={
            "chat_id": CHAT_ID,
            "text": text
        }, timeout=10)

    except Exception as e:
        print("Ошибка отправки:", e)


while True:
    text = get_prices()
    send_message(text)

    print("Отправлено:", time.strftime("%H:%M:%S"))

    time.sleep(60)
