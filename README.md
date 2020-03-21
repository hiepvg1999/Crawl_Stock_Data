Crawl Stock Data

I use Scrapy to crawl <a href = "https://www.cophieu68.vn/historyprice.php?id=MWG">MWG(Th</a> stock data: 

Setup:

+)pip install scrapy

+)scrapy startproject StockData

+)Copy and paste Stock_spider.py into spider directory.

+)Copy and paste items.py into StockData directory.

+)scrapy crawl stock -o stock.csv

Note:After have stock.csv with un-sorted data,copy and paste sorted_data.py in order to sort data with datetime col 
--
in terminal, run "python3 sorted_data.py"  
--
Remember change path of file csv.
--
