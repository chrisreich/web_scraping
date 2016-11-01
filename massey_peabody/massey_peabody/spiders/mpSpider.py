import scrapy


class MasseyPeabodyNFLSpider(scrapy.Spider):
    name = "NFL_mp"
    start_urls = ["http://massey-peabody.com/nfl-2016-rankings-week/"]

    def parse(self, response):

        fileStr = response.xpath('//a[contains(@href, "uploads")]/text()').extract_first()

        if "eek 9" in fileStr:

            target = open("/Users/creich/web_scraping/massey_peabody/nfl_flag.txt", "w")
            target.truncate()

            target.write("YES")
            target.close()



class MasseyPeabodyCFBSpider(scrapy.Spider):
    name ="CFB_mp"
    start_urls = ["http://massey-peabody.com/college-football-2016-weekly-rankings/"]

    def parse(self, response):

        fileStr = response.xpath('//a[contains(@href, "uploads")]/text()').extract_first()

        if "eek 10" in fileStr:
            target = open("/Users/creich/web_scraping/massey_peabody/cfb_flag.txt", "w")
            target.truncate()
            target.write("YES")
            target.close()
