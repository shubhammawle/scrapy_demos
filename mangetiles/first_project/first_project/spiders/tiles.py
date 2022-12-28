import scrapy


class TilesSpider(scrapy.Spider):
    name = 'tiles'
    allowed_domains = ['www.magnatiles.com']
    start_urls = ['http://www.magnatiles.com/products/']

    def parse(self, response):
        products = response.css('ul.products li')
        for p in products:
            yield{
                'name': p.css('h2::text').get(),
                'sku': p.css('a.button::attr(data-product_sku)').get(),
                'price':  p.css('span.price bdi::text').get(),
                 }

