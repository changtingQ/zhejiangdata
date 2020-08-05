# -*- coding: utf-8 -*-
import scrapy


class SmcsSwSpider(scrapy.Spider):
    name = 'smcs_sw'

    def start_requests(self):
        base_url = "http://183.136.190.39:7070/smcs_sw/tm/icpWebsite/getPageModel.do"
        cookies = {
            "JSESSIONID": "E84175C060B8B43DC918F6FCA5952173"
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Linux; U; Android 1.5; en-us; sdk Build/CUPCAKE) AppleWebkit/528.5  (KHTML, like Gecko) Version/3.1.2 Mobile Safari/525.20.1",
            "Host": "183.136.190.39:7070",
            "Origin": "http://183.136.190.39:7070",
            "Referer": "http://183.136.190.39:7070/smcs_sw/system/redirect/redirectHomePage.do?path=tm/icpWebsite"
        }

        for page_num in range(1, 3):
            formdata = {'fuzzy': 'false', 'page': "{}".format(page_num),
                        "rows": "30", "sort": "id", "order": "asc"}
            print(formdata)
            yield scrapy.FormRequest(base_url,callback=self.parse, headers=headers, dont_filter=True, cookies=cookies,
                                     formdata=formdata)

    def parse(self, response):
        print("-------------------------")
        print(response.text)



if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute("scrapy crawl smcs_sw".split())
