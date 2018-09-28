import scrapy
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging


class MySpider1(scrapy.Spider):
    # Your first spider definition
    ...


class MySpider2(scrapy.Spider):
    # Your second spider definition
    ...


configure_logging()
runner = CrawlerRunner()
runner.crawl(MySpider1)
runner.crawl(MySpider2)
d = runner.join()
d.addBoth(lambda _: reactor.stop())
reactor.run()  # the script will block here until all crawling jobs are finished
