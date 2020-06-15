# -*- coding: utf-8 -*-
import os
import sys
import scrapy
from pm25.items import Pm25Item


class Pm25Spider(scrapy.Spider):
    name = 'Pm25'
    allowed_domains = ['www.aqistudy.cn']
    start_urls = ['https://www.aqistudy.cn/historydata/monthdata.php?city=%E5%BE%B7%E5%B7%9E']
    hrefPrefix = 'https://www.aqistudy.cn/historydata/'

    def parse(self, response):
        lis = response.xpath('//ul[@class="unstyled1"]/li/a')
        item = {}

        for li in lis:
            item['month_href'] = self.hrefPrefix + li.xpath('@href')[0].extract()
            item['month'] = item['month_href'][-6:]

            # exec nodejs: node js-parser.js city month
            os.system('/usr/bin/node js-parser.js 德州 ' + item['month'])