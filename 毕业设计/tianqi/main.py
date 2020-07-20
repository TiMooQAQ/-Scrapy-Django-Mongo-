import time,datetime
import os

time_now = time.strftime("%M:%S", time.localtime())  # 刷新

while True:
    time_now = time.strftime("%M:%S", time.localtime())  # 刷新
    time.sleep(1)
    print(f'\r{datetime.datetime.now()}', end='')

    if time_now == "00:00":  # 此处设置每天定时的时间
        qq = os.system("scrapy crawl tianqispider")
        print(qq)
        time.sleep(20)
