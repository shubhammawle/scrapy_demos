import scrapy


class SunglassesSpider(scrapy.Spider):
    name = 'sunglasses'
    allowed_domains = ['sunglasshut.com']
    start_urls = ['https://sunglasshut.in/ext/algolia/application/api/v1.0/collections/men/items?page_id=1&page_size=12']

    def parse(self, response):
        print(response.body)
        pass
