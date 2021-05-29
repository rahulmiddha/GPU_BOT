from bs4 import BeautifulSoup
import requests
import urllib3
import time


def check_avail(url, hdr, version):
    http = urllib3.PoolManager()
    response = http.request("GET", url, hdr)
    soup = BeautifulSoup(response.data, "html.parser")
    span_text = soup.find_all("span", {"class": "rs2"})[0].text

    current_time = time.strftime("%d-%m-%Y : %H:%M:%S", time.localtime())

    if version == "3070":
        if "Out of stock" not in span_text:
            text = "3070 is in stock. Go to https://rptechindia.in/nvidia-geforce-rtx-3070.html"
            chat_id = "1792211518"
            bot_secret = "1871383574:AAFOCtshtRQx78qPZPEWGeODiP2cDYCkjDg"
            data = {"text": f"{text}", "chat_id": f"{chat_id}"}
            requests.post(
                f"https://api.telegram.org/bot{bot_secret}/sendMessage", data=data
            )
            print(current_time, "3070 IN STOCK")
        else:
            print(current_time, "3070 OUT OF STOCK")

    if version == "3060":
        if "Out of stock" not in span_text:
            text = "3060 is in stock. Go to https://rptechindia.in/nvidia-geforce-rtx-3060-ti.html"
            chat_id = "1792211518"
            bot_secret = "1871383574:AAFOCtshtRQx78qPZPEWGeODiP2cDYCkjDg"
            data = {"text": f"{text}", "chat_id": f"{chat_id}"}
            requests.post(
                f"https://api.telegram.org/bot{bot_secret}/sendMessage", data=data
            )
            print(current_time, "3060 IN STOCK")
        else:
            print(current_time, "3060 OUT OF STOCK")


def main():

    url_3070 = "https://rptechindia.in/nvidia-geforce-rtx-3070.html"
    url_3060 = "https://rptechindia.in/nvidia-geforce-rtx-3060-ti.html"
    hdr = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 "
            "(KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
        ),
        "Accept": (
            "text/html,application/xhtml+xml," "application/xml;q=0.9,*/*;q=0.8"
        ),
        "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
        "Accept-Encoding": "none",
        "Accept-Language": "en-US,en;q=0.8",
        "Connection": "keep-alive",
    }
    # checks for 3070
    check_avail(url_3070, hdr, "3070")

    # checks for 3060
    check_avail(url_3060, hdr, "3060")


if __name__ == "__main__":
    while True:
        main()
        # waits 10 minutes for next iteration
        time.sleep(600)
