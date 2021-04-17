Steps to create a spider:
* Create a virtual environment called webscrape in Anaconda
* install scrapy (Use pip install scrapy and not conda install scrapy)
* Anaconda prompt commands:   
    * cd .../project1
    * activate webscrape
    * scrapy crawl Books
* Spyder script - firstspider.py
## Scrapy Shells
* Interactive shell for debugging without the need for running Spyder
* Anaconda prompt
   * scrapy shell https://books.toscrape.com/index.html
   * use inspect element: bookstoscrape , inspect All products copy the xpath
   * response.xpath('//*[@id="default"]/div/div/div/div/div[1]/h1').get()
   
   CSS Method:
   * response.css('img').xpath('@src').getall() #return images
