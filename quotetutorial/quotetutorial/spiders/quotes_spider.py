import scrapy
from ..items import QuotetutorialItem
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class QuoteSpider(scrapy.Spider):
    name= 'quotes'
    start_urls=[
        "http://quotes.toscrape.com/page/1/"
    ]

    def parse(self, response):

        items = QuotetutorialItem()
        all_quotes = response.css("div.quote")
        for quotes in all_quotes:
            title = quotes.css(".text::text").extract()
            author = quotes.css(".author::text").extract()
            tag = quotes.css("a.tag::text").extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag
                
            yield items
            
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)




       

        
