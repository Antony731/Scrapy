# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import scrapy

class FirstSpider(scrapy.Spider):
    name = "Books"
    start_urls = [
        "https://books.toscrape.com/index.html",
        "https://books.toscrape.com/catalogue/category/books/science_22/index.html",
        ]
    
    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'books-%s.html' % page
        with open(filename, "wb") as f:
            f.write(response.body)