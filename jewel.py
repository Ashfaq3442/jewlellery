import scrapy


class JewelSpider(scrapy.Spider):
    name = "jewel"
    allowed_domains = ["cullenjewellery.com"]
    start_urls = ["https://cullenjewellery.com/engagement-rings"]

    def parse(self, response):
        pass
