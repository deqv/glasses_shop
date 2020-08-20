import scrapy


class GlassesFromGlassesshopSpider(scrapy.Spider):
    name = 'glasses_from_glassesshop'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        for product in response.xpath("//div[@class='col-12 pb-5 mb-lg-3 col-lg-4 product-list-row text-center']"):
            yield {
                'product_url': product.xpath(".//div[@class='p-title-block']/div[@class='mt-3']/div[@class='row no-gutters']/div[@class='col-6 col-lg-6']/div[@class='p-title']/a/@href").get(),
                'product_name': product.xpath(".//div[@class='p-title-block']/div[@class='mt-3']/div[@class='row no-gutters']/div[@class='col-6 col-lg-6']/div[@class='p-title']/a/text()").get(),
                'product_image_link': product.xpath(".//div[@class='product-img-outer']/a/img[@class='lazy d-block w-100 product-img-default']/@src").get(),
                'product_price': product.xpath(".//div[@class='p-title-block']/div[@class='mt-3']/div[@class='row no-gutters']/div[@class='col-6 col-lg-6']/div[@class='p-price']/div/span/text()").get()
            }

        next_page = response.xpath("//div[@class='row d-lg-none mb-5']/div/ul/li[@class='page-item col-6 p-0']/a/@href").get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
