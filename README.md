Crawl Stock Data
<a href="https://www.cophieu68.vn">Crawl Data Page</a>
I use Scrapy to crawl <a href = "https://www.cophieu68.vn/historyprice.php?id=MWG">MWG(The gioi di dong)</a> stock data,you can change id by other name.  

Setup:
<ul>
 <li>pip install scrapy</li>

 <li>scrapy startproject StockData</li>

 <li>Copy and paste Stock_spider.py into spider directory.</li>

 <li>Copy and paste items.py into StockData directory.</li>

 <li>scrapy crawl stock -o stock.csv</li>
</ul>
Note:After have stock.csv with un-sorted data,copy and paste sorted_data.py in order to sort data with datetime col 
--
in terminal, run "python3 sorted_data.py"  
--
Remember change path of file csv.
--
