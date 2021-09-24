import scrapy


class QuotesSpider(scrapy.Spider):
    name = "players"
    start_urls = [
        'https://lolchess.gg/leaderboards?mode=ranked&region=na&tier=master&page=1',
        'https://lolchess.gg/leaderboards?mode=ranked&region=na&tier=master&page=2'
    ]

    def parse(self, response):
        page = response.url.split('=')[-1]
        filename = f'masters-accounts-{page}.html'
        count = 0
        for player in response.selector.xpath('//*[@id="wrapper"]/div[3]/table/tbody/tr'):
            count += 1
            yield {
                'rank': response.selector.xpath('//*[@id="wrapper"]/div[3]/table/tbody/tr[' + str(count) +
                                                ']/td[1]/text()').get(),
                'name': response.selector.xpath('//*[@id="wrapper"]/div[3]/table/tbody/tr[' + str(count) +
                                                ']/td[2]/a/text()').get().strip(),
                'lp': response.selector.xpath('//*[@id="wrapper"]/div[3]/table/tbody/tr[' + str(count) +
                                              ']/td[4]/text()').get().strip()
            }
