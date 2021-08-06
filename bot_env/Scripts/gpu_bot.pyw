from bs4 import BeautifulSoup
import requests
import urllib3
import time


def check_avail(version):
    url = "https://rptechindia.in/nvidia-geforce-rtx-" + version + ".html"
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
    http = urllib3.PoolManager()
    response = http.request("GET", url, hdr)
    soup = BeautifulSoup(response.data, "html.parser")
    try:
        span_text = soup.find_all("span", {"class": "rs2"})[0].text
    # adding exception for index errors
    except IndexError:
        print("\033[93m INDEX ERROR \033[0;0m")
        time.sleep(300)
        span_text = soup.find_all("span", {"class": "rs2"})[0].text

    current_time = time.strftime("%d-%m-%Y : %H:%M:%S", time.localtime())

    if "Out of stock" not in span_text:
        text = (
            version
            + "is in stock. \nGo to https://rptechindia.in/nvidia-geforce-rtx-"
            + version
            + ".html"
        )
        chat_id = "****"
        bot_secret = "******"
        data = {"text": f"{text}", "chat_id": f"{chat_id}"}
        requests.post(
            f"https://api.telegram.org/bot{bot_secret}/sendMessage", data=data
        )
        print(current_time, version + "\033[1;32;40m IN STOCK \033[0;0m")
    else:
        print(current_time, version + "\033[1;31;40m OUT OF STOCK \033[0;0m")


if __name__ == "__main__":
    while True:
        # checks for 3070
        check_avail("3070")

        # checks for 3060
        check_avail("3060-ti")
        # waits 10 minutes for next iteration
        time.sleep(600)
