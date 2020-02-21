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


# process = CrawlerProcess(get_project_settings())

# process.crawl('quotes','http://quotes.toscrape.com/page/1/')
# process.start()

        # for quote in response.css('div.quote'):
        #name = response.css('.author + a::attr(href)').css('h3.author-title::text').extract()       
        # for a in response.css('.author + a::attr(href)'):
        #     name = a.css('h3.author-title::text').extract()

        #     items['name'] = name

        #     yield items


    # def parse_author(self, response):
    #     items = QuotetutorialItem()

    #     name = response.css('h3.author-title::text').extract(),
    #     birthdate = response.css('.author-born-date::text').extract()
    #     bio = response.css('.author-description::text').extract()

    #     items['name'] = name
    #     items['birthdate'] = birthdate
    #     items['bio'] = bio

    #     yield items
                

        

        # for href in response.css('.author + a::attr(href)'):
        #     yield response.follow(href, self.parse_author)

        # for href in response.css('li.next a::attr(href)'):
        #     yield response.follow(href, self.parse)

    

        
            #yield {
                #'text': quote.css('span.text::text').get(),
                #'author': quote.css('span small::text').get(),
                #'tags': quote.css('div.tags a.tag::text').getall(),
                #}
        

 
    
        
         

       

        