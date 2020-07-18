from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import time
while True:
    time_now = time.strftime("%M:%S", time.localtime())  # 刷新
    if time_now == "00:30": #此处设置每天定时的时间


        if __name__ == '__main__':
            process = CrawlerProcess(get_project_settings())
            process.crawl('tianqispider')  # 你需要将此处的spider_name替换为你自己的爬虫名称
            process.start()

        time.sleep(10)


