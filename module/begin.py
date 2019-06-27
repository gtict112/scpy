from scrapy import cmdline

cmdline.execute("scrapy crawl BiduSpider -o quotes.json".split())