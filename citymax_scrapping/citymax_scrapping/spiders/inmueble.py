import scrapy
#from scrapy.shell import inspect_response
from citymax_scrapping.items import ActiveItem

class TripSpider(scrapy.Spider):
    name = "actives"
    start_urls = ['https://www.citymax-gt.com/resultados-busqueda/']

    def parse(self, response):
        for place in response.css('#ID-41'):
            url = place.css('.property-title > a').attrib.get('href')
            yield response.follow(url, callback=self.parse_data)

        # Explore next page
        next_page = response.xpath('//a[@rel="Next"]/@href').get()
        if next_page:
            url = response.urljoin(next_page)
            yield scrapy.Request(url, callback=self.parse)
        
    def parse_data (self, response):
        #Description        
        description = response.css('#description').css('*::text').getall()
        description = ' '.join(description).replace('\t', '').replace('\n', '')
        
        detail = response.css('#detail').css('*::text').getall()
        index_type = detail.index('Tipo:') + 1
        index_operation = detail.index('Operación:') + 1
        index_price = detail.index('Precio: ') + 1
        name = response.css('.header-detail').xpath("//h1/text()").get()
        yield ActiveItem (
            name = name,
            operation = detail[index_operation].strip(),
            price = detail[index_price].strip(),
            type = detail[index_type].strip(),
            description = description.strip()
        )