# -*- coding: utf-8 -*-
import scrapy


class SmcsSwSpider(scrapy.Spider):
    name = 'smcs_sw'

    def start_requests(self):
        base_url = "http://183.136.190.39:7070/smcs_sw/tm/icpWebsite/getPageModel.do"
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; U; Android 1.5; en-us; sdk Build/CUPCAKE) AppleWebkit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
            "Host": "183.136.190.39:7070",
            "Origin": "http://183.136.190.39:7070",
            "Cookie": "JSESSIONID=E84175C060B8B43DC918F6FCA5952173",
            "Referer": "http://183.136.190.39:7070/smcs_sw/system/redirect/redirectHomePage.do?path=tm/icpWebsite"
        }
        yield scrapy.Request(base_url, callback=self.parse, headers=headers, dont_filter=True)

    def parse(self, response):
        print(response.text)



