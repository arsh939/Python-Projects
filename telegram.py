import json
import requests
import time
import urllib
import config
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


TOKEN = ''
URL = "https://api.telegram.org/bot{}/".format(TOKEN)
stop = 0
number = 0
def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def handle_updates(updates):
    for update in updates["result"]:
        global chat
        try:
            text = update["message"]["text"]
            palavras = text.split()
            chat = update["message"]["chat"]["id"]
          
        except KeyError:
            text = "Invalid Input"
            chat = update["message"]["chat"]["id"]
            send_message(text,chat)
            pass
        if text == "/stop":
            global stop
            die()
            stop = 1
            
            send_message("Bot is Stopped. Type /url to start again.", chat)
        elif text == "/start":
            send_message("Welcome to Amazon Stock Checker by Arsh.\nEnter the /url command below to start the Bot.", chat)
        elif text == "/url":
            send_message("Enter the product URL below.", chat)
        elif text.startswith('0') or text.startswith('1') or text.startswith('2') or text.startswith('3') or text.startswith('4') or text.startswith('5') or text.startswith('6') or text.startswith('7') or text.startswith('8') or text.startswith('9') :
            send_message("Enter how many times you want to check stock.", chat)
            number = text
        elif text.startswith("/"):
            continue
        elif text.startswith("https://www.amazon.in/dp") or text.startswith("https://www.amazon.in/gp"):
            #print(number)
            i=5
            while(i != 0):
                i = i - 1
                #number = number - 1
                print(i)
                message = text
                url= message
                chrome_options = Options()  
                chrome_options.add_argument("--headless") 
                with Chrome(options=chrome_options) as browser:
                    browser.get(url)
                    html = browser.page_source
                soup = BeautifulSoup(html, "html.parser")
                title = soup.title.string
                cart  = soup.find('span', { "id" : "submit.add-to-cart-announce"})
                buy  = soup.find('span', { "id" : "submit.buy-now-announce"})
                price  = soup.find('span', { "id" : "priceblock_dealprice"})
                if str(cart) == "None" or str(buy) == "None":
                    print("Not in Stock")
                else:
                    print(cart.get_text(),buy.get_text())
                    if text.startswith("https://www.amazon.in/gp"):
                        
                        a = telegram_bot_sendtext(title + '\n\nPRODUCT IN STOCK\n\n' + price.get_text() + '\n\n' + url)
                        print(a)
                    else:
                        
                        a = telegram_bot_sendtext(title + '\n\nPRODUCT IN STOCK\n\n' + '\n\n' + url)
                        print(a)
        else:
            send_message("Invalid Input", chat)


def telegram_bot_sendtext(bot_message):
           global chat
           
           bot_token = str(TOKEN)
           
           bot_chatID = str(chat)
           bot_message = urllib.parse.quote_plus(bot_message)
           send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown' + '&text=' + bot_message
           
           response = requests.get(send_text)
           return response.json()

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)



def send_message(text, chat_id, reply_markup=None):
    text = urllib.parse.quote_plus(text)
    url = URL + "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(text, chat_id)
    if reply_markup:
        url += "&reply_markup={}".format(reply_markup)
    get_url(url)


def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
