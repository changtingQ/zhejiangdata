# -*- coding: utf-8 -*-
import scrapy
import demjson
from smcs.items import SmcsItem


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
            yield scrapy.FormRequest(base_url, callback=self.parse, headers=headers, dont_filter=True, cookies=cookies,
                                     formdata=formdata)

    def parse(self, response):
        list_data = demjson.decode(response.text)
        rows_data = list_data.get("rows")

        if rows_data:
            item = SmcsItem()
            for person_data in rows_data:
                item = self.parse_detail(person_data)
                yield item

    def parse_detail(self, person_data):
        data_deal = dict()
        data_deal["wzfzr"] = person_data.get("wzfzr")
        data_deal["wzfzrdh"] = person_data.get("wzfzrSjhm", "")
        data_deal["site_name"] = person_data.get("siteName", "")
        data_deal["license_key"] = person_data.get("licenseKey", "")
        data_deal["top_domain"] = person_data.get("topDomain", "")
        data_deal["belonging_city"] = person_data.get("belongingCity", "")
        data_deal["wzfzr_sjhm"] = person_data.get("wzfzrSjhm", "")
        data_deal["ztfzrdh"] = person_data.get("wzfzrdh", "")
        data_deal["ztfzr"] = person_data.get("ztfzr", "")
        data_deal["ztfzr_sjhm"] = person_data.get("ztfzrSjhm", "")

        return data_deal


if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute("scrapy crawl smcs_sw".split())
