import scrapy
from urllib.parse import urljoin



class JewelSpider(scrapy.Spider):
    name = "jewel"
    allowed_domains = ["cullenjewellery.com"]
    start_urls = ["https://cullenjewellery.com/engagement-rings"]

    def parse(self, response):
        pass