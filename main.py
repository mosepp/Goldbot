import requests
from bs4 import BeautifulSoup
import telebot
from apscheduler.schedulers.blocking import BlockingScheduler

TOKEN = "7461879443:AAFf6YQXXe7AcOguLUEL-KbrZBnNmNNSYRw"
CHAT_ID = "79176954"

bot = telebot.TeleBot(TOKEN)
scheduler = BlockingScheduler()

def fetch_prices():
    try:
        url = "https://www.tgju.org/"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        gold_tag = soup.find("td", attrs={"data-title": "قیمت طلا ۱۸ عیار"})
        ounce_tag = soup.find("td", attrs={"data-title": "اونس طلا"})
        
        gold_price = gold_tag.text.strip() if gold_tag else "نامشخص"
        ounce_price = ounce_tag.text.strip() if ounce_tag else "نامشخص"
        
        message = f"قیمت طلا ۱۸ عیار: {gold_price}\nقیمت انس جهانی: {ounce_price}"
        bot.send_message(CHAT_ID, message)
    except Exception as e:
        bot.send_message(CHAT_ID, f"خطا در دریافت قیمت: {e}")

scheduler.add_job(fetch_prices, 'interval', minutes=1)
scheduler.start()
