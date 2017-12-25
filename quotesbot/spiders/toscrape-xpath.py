# -*- coding: utf-8 -*-
import scrapy
from quotesbot.items import QuotesbotItem

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'toscrape-xpath'
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    def parse(self, response):
        item=QuotesbotItem()
        for quote in response.xpath('//div[@class="quote"]'):
            item['text']=quote.xpath('./span[@class="text"]/text()').extract_first()
            item['author']=quote.xpath('.//small[@class="author"]/text()').extract_first()
            item['authorlink']=quote.xpath('./span[2]/a/@href').extract_first()
            item['tags']=quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').extract_first()
            yield item
            

        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))

