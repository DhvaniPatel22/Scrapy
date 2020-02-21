import scrapy
from ..items import QuotetutorialItem
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class AuthorSpider(scrapy.Spider):
    name = 'author'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for href in response.css('.author + a::attr(href)'):
            yield response.follow(href, self.parse_author)

        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, self.parse)

    def parse_author(self, response):
        items = QuotetutorialItem()

        name = response.css('h3.author-title::text').extract(),
        birthdate = response.css('.author-born-date::text').extract()
        bio = response.css('.author-description::text').extract()

        items['name'] = name
        items['birthdate'] = birthdate
        items['bio'] = bio

        yield items




