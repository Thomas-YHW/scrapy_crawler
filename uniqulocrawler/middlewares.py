# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import scrapy.downloadermiddlewares
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger
import time

class UniqulocrawlerSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.
    def __init__(self,service_args=[]):
        self.logger = getLogger(__name__)
        #self.timeout = timeout
        option=webdriver.ChromeOptions()
        option.add_argument('lang=zh_CN.UTF-8')
        option.add_argument( 'user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"')
        self.browser  = webdriver.Chrome(service_args=service_args,chrome_options=option)#这里也就是初始化成员变量
        self.browser.set_window_size(1400, 700)
        #self.browser.set_page_load_timeout(self.timeout)
       # self.wait = WebDriverWait(self.browser, self.timeout)

    def __del__(self):
        self.browser.close()

    def process_request(self, request, spider):
        """
        改用chorme，这个函数对url进行请求
        :param request: Request对象
        :param spider: Spider对象
        :return: HtmlResponse
        """
        print(request.url)
        self.logger.debug('Chorme is Starting')
        self.browser.get(request.url)#加载当前的网页
        # self.logger.debug(self.browser.page_source)
        # search_box = self.browser.find_element_by_name('q')
        # search_box.send_keys('ChromeDriver')
        # search_box.submit()
        time.sleep(5)
        self.logger.debug(self.browser.page_source)
        #self.logger.debug(self.browser.execute_script("return document.documentElement.outerHTML"))
        return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8',status=200)#page_source为解析后的html


    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'),
    #                service_args=crawler.settings.get('PHANTOMJS_SERVICE_ARGS'))
'''
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class UniqulocrawlerDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

'''
