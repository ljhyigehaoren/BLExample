# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider

class BlSpider(RedisSpider):
    name = 'bl'
    allowed_domains = ['wanfangdata.com.cn']
    #start_urls = ['http://baidu.com/']
    redis_key = 'bl:start_urls'

    def parse(self, response):
        print(response.status,response.url)

        # 获取下一页
        nextUrls = response.xpath('//p[@class="pager"]//a[@class="page"]/@href').extract()
        if len(nextUrls):
            for nextUrl in nextUrls:
                nextUrl = response.urljoin(nextUrl)
                print(nextUrl)
                yield scrapy.Request(url=nextUrl, callback=self.parse)
