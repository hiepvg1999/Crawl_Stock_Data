Crawl Stock Data

Setup:
'''bash pip install scrapy'''

'''bash scrapy startproject StockData'''

+)Copy and paste Stock_spider.py into spider directory.

+)Copy and paste items.py into StockData directory.

'''bash scrapy crawl stock -o stock.csv'''

Note:After have stock.csv with un-sorted data,copy and paste sorted_data.py in order to sort data with datetime col 
--
in terminal, run "python3 sorted_data.py"  
--
Change path of file csv.
--
