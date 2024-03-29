# -*- coding: utf-8 -*-
import scrapy


class BiduSpider(scrapy.Spider):
    name = 'BiduSpider'
    # allowed_domains = ['https://6034.vip/home/']
    # start_urls = ['https://6034.vip/member/index#']

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
