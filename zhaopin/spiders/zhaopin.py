import scrapy
from ..items import ZhaopinItem


class MySpider(scrapy.spiders.Spider):
    name = 'zhaopin'
    allowed_domains = ["zhaopin.com/"]
    start_urls = ["http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw=python&p=1&isadv=0",
                  ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        jobitem = ZhaopinItem()
        jobs = response.xpath("//table[@class='newlist']")
        for each_job in jobs:
            job = each_job.xpath("string(.//td[@class='zwmc']/div/a)").extract()
            company = each_job.xpath("string(.//td[@class='gsmc']/a)").extract()
            pay = each_job.xpath("string(.//td[@class='zwyx'])").extract()
            jobitem['job'] = job
            jobitem['company'] = company
            jobitem['pay'] = pay
            yield jobitem

#爬取一串内容
#        jobs = response.xpath("//table[@class]")
#        f = open(filename,'w')
#        for each_job in jobs:
#            job = each_job.xpath('normalize-space(string(.))').extract()
#            str_job = str(job) + '\n'
#            print(len(str_job))
#            f.write(str_job)
#            print("fuckfuckfuck\n\n\n")
#        f.close()