from scrapy import  Spider
from scrapy.selector import  Selector
from StockData.items import StockdataItem

class StockSpider(Spider):
    name = "stock"
    allowed_domains = ["cophieu68.vn"]
    start_urls = [
        "https://www.cophieu68.vn/historyprice.php?id=MWG"
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//*[@id="content"]/table//tr')
        for question in questions[1:]:
            item = StockdataItem()
            #item['STT'] = question.xpath('td[1]//text()').extract_first()
            item['Ngay']= question.xpath('td[2]//text()').extract_first()
            item['Giathamchieu'] = question.xpath('td[3]//text()').extract_first()
            item['Thaydoi'] = question.xpath('td[4]/span//text()').extract_first()
            item['Thaydoiphantram'] = question.xpath('td[5]/span//text()').extract_first()
            item['Dongcua'] = question.xpath('td[6]/span/strong//text()').extract_first()
            item['Khoiluong'] = question.xpath('td[7]//text()').extract_first()
            item['Mocua'] = question.xpath('td[8]//text()').extract_first()
            item['Caonhat'] = question.xpath('td[9]//text()').extract_first()
            item['Thapnhat'] = question.xpath('td[10]//text()').extract_first()
            item['GDthoathuan'] = question.xpath('td[11]//text()').extract_first()
            item['Nuocngoaimua'] = question.xpath('td[12]//text()').extract_first()
            item['Nuocngoaiban'] = question.xpath('td[13]//text()').extract_first()
            item['Giatri'] = question.xpath('td[14]//text()').extract_first()
            yield item
        next_page = Selector(response).xpath('//*[@id="navigator"]/li/a')
        for page in next_page[1:]:
            if page is not None:
                yield response.follow(page, callback=self.parse)
