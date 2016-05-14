# -*- coding: utf-8 -*-
import scrapy
from downloadcases.items import DownloadcasesItem


class OhchrSpider(scrapy.Spider):
    name = "ohchr"
    allowed_domains = ["ohchr.org"]
    start_urls = [ ]
    
    url_left = 'http://juris.ohchr.org/Search/Details/'

    def __init__(self, *args, **kwargs):
        super(OhchrSpider, self).__init__(*args, **kwargs)
        
        for i in range(1, 2500):
            url = self.url_left + str(i)
            self.start_urls.append(url)
    
    def parse(self, response):
        #print(response.url)
        Id_string_array = response.xpath('//section[@id=\'download-listings\']/h2/text()')
        if len(Id_string_array) > 0:
            item = DownloadcasesItem()            

            Id_string = Id_string_array[0].extract()
            item['Id_string'] = Id_string
            
            headers = response.xpath('//dl')[0].xpath('//dt').xpath('./text()').extract()
            values = response.xpath('//dl')[0].xpath('//dd')            
            for (h, v) in zip(headers, values):
                header = h.strip().replace(' ', '_')
                if 'Communication_number(s)' in header:
                    header = 'Communication_numbers'
                li = v.xpath('./li/text()').extract()
                if len(li) > 0:
                    item[header] = li
                else:
                    item[header] = v.xpath('./text()')[0].extract().strip()
            
#            for tr in response.xpath('//tr'):
#                tds = tr.xpath('//td')
#                print("Has " + str(len(tds)) + " tds")
#                if(len(tds) > 0 and tds[0].xpath('./text()').extract()[0].strip() == u'English'):
#                    print("Found the english one")
#                    for td in tds[1:]:
#                        a = td.xpath('./a')
#                        if len(a) > 0:
#                            if 'pdf' in a[0].xpath('./img/@title'):
#                                item['file_urls'] = [a.xpath('./@href')]
#                                item['files'] = [Id_string.replace('/', '_') + '.pdf']
            for tr in response.xpath('//table/tbody/tr'):
                tds = tr.xpath('./td')
                if(len(tds) > 0 and 
                   tds[0].xpath('./text()')[0].extract() == u'English'):
                    for td in tds[1:]:
                        if(len(td.xpath('./a/img/@title')) > 0 and 
                           u'pdf' in td.xpath('./a/img/@title')[0].extract()):
                            url = td.xpath('./a/@href')[0].extract()
                            item['file_urls'] = [url]
                            item['files'] = [Id_string.replace('/', '_') + '.pdf']

            yield(item)