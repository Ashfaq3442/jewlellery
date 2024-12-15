import scrapy
from urllib.parse import urljoin


class JewelSpider(scrapy.Spider):
    name = "jewel"
    allowed_domains = ["cullenjewellery.com"]
    start_urls = ["https://cullenjewellery.com/engagement-rings"]

    def parse(self, response):
        # Base URL for joining relative paths
        base_url = "https://cdn.shopify.com/s/files/1/0644/3067/0060/files/"
        
        # Extract image URLs
        image_urls = response.css('img.thumb_image::attr(src)').getall()
        image_urls = [urljoin(base_url, url) for url in image_urls]
        
        # Extract video thumbnails with their video play icon
        video_urls = response.css('div.thumb_video_icon').xpath('./../img/@src').getall()
        video_urls = [urljoin(base_url, url) for url in video_urls]

        # Yield image requests
        for img_url in image_urls:
            yield scrapy.Request(url=img_url, callback=self.save_file)

        # Yield video requests (modify to actual video URL if required)
        for video_url in video_urls:
            yield scrapy.Request(url=video_url, callback=self.save_file)

    def save_file(self, response):
        # Extract the file name from the URL
        file_name = response.url.split("/")[-1]
        file_path = f"downloads/{file_name}"  # Save to 'downloads/' folder

        # Save the file
        with open(file_path, 'wb') as f:
            f.write(response.body)
