import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.contrib.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy import log
from reddit.items import RedditItem

class RedditSpider(scrapy.Spider):
	name = "reddit"

	def start_requests(self):
		url = [
		'https://www.reddit.com/'
		]
		for u in url:
			yield scrapy.Request(url=u, callback=self.parse)

	def parse(self, response):
		print ("Start scrapping Review info....")
		hxs = Selector(response)
		l_venue = RedditItem()
		
		reddit_titles = hxs.xpath("//div[@class = 'content']/div[@class = 'spacer']/div[@id='siteTable']/div[@data-type='link']/div[@class = 'entry unvoted']/div[@class='top-matter']/p[@class='title']/a/text()")
		l_venue['title'] = reddit_titles.extract()
		yield l_venue