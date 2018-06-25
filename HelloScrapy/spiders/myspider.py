# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request

from HelloScrapy.items import HelloscrapyItem


class MyspiderSpider(scrapy.Spider):
    name = 'myspider'
    allowed_domains = ['www.x23us.com']
    bash_url = 'https://www.x23us.com/class/'
    bashurl = '.html'

    def start_requests(self):
        for i in range(1, 11):
            url = self.bash_url + str(i) + '_1' + self.bashurl
            yield Request(url, self.parse)

    def parse(self, response):
        max_num=int(response.xpath("//*[@id='pagelink']/a[14]/text()").extract_first())
        baseurl=str(response.url)[:30]
        for i in range(1,max_num+1):
            u=baseurl+str(i)+self.bashurl
            yield Request(url=u, callback=self.parse_name)

    def parse_name(self, response):
        name_list=response.xpath('//*[@id="content"]/dd[1]/table/tr/td[1]/a[2]/text()').extract()
        author_list = response.xpath('//*[@id="content"]/dd[1]/table/tr/td[3]/text()').extract()
        url_list=response.xpath('//*[@id="content"]/dd[1]/table/tr/td[1]/a[1]/@href').extract()
        for n,u,a in zip(name_list,url_list,author_list):
            yield Request(u,callback=self.parse_detail,meta={'name':n,'author':a})

    def parse_detail(self, response):
        collect_num_str = response.xpath('//*[@id="at"]/tr[2]/td[1]/text()').extract_first()  # 网页中含有&nbsp; ==> \xa0
        collect_num = int("".join(collect_num_str.split()))  # 去掉空格的编码 收藏数
        #print(response.meta['name'], response.meta['author'], response.url, collect_num)
        item = HelloscrapyItem()
        item['title'] = response.meta['name']
        item['author'] = response.meta['author']
        item['link'] = response.url
        item['collect'] = collect_num
        yield item