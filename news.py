# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest

class NewsSpider(scrapy.Spider):
	name = 'news'
	def start_requests(self):
		return[scrapy.FormRequest("https://news.ycombinator.com/login",formdata=
			{'goto':'news','acct':'scrape1123','pw':'scrape1123'},callback=self.parse)]
	def parse(self, response):
		jobs=response.xpath('//td[@class="subtext"]')
		for job in jobs:
			score=job.xpath('span[@class="score"]/text()').extract_first()
			name=job.xpath('a/text()').extract_first()
			yield{'score':score,'name':name}