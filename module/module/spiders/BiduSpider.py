# -*- coding: utf-8 -*-
import scrapy


class BiduSpider(scrapy.Spider):
    name = 'BiduSpider'
    allowed_domains = ['https://6034.vip/home/']
    start_urls = ['https://6034.vip/member/index#']

    def parse(self, response):
        pass
