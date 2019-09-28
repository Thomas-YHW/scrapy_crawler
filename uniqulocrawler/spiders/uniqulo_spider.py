# -*- coding: utf-8 -*-
from scrapy import Spider,Request
class UniquloSpiderSpider(Spider):
    name = 'uniqulo_spider'
    #allowed_domains = ['https://www.uniqlo.cn']
    start_urls = ['http://www.uniqlo.cn/c/NVZHUANG.html/']
    # def parse(self, response):
    #     yield Request(url='http://https://www.uniqlo.cn/c/NVZHUANG.html/')
    #    pass
    def start_requests(self):
        yield Request(url='http://www.uniqlo.cn/c/NVZHUANG.html/')
    def parse(self, response):
        response.selector.css('.picture-img').xpath('@src').extract_first()
        self.logger.debug(response.selector.css('.picture-img').getall())
        pass





