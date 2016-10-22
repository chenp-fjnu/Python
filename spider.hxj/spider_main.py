#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import html_downloader
import html_outputer
import html_parser
import sys
class SpiderMain(object):
    def __init__(self):
        self.downloader=html_downloader.HtmlDownloader()
        self.parser=html_parser.HtmlParser()
        self.outputer=html_outputer.HtmlOutputer()
    def craw(self, root_url):
        try:
            html_content=self.downloader.download(root_url)
            new_data = self.parser.parse(html_content)
            self.outputer.collect_data(new_data)
        except:
            e = sys.exc_info()
            print("<p>Error: %s</p>" % e )
        self.outputer.output_html()

if __name__=="__main__":
    # https://api.weibo.com/2/search/topics.json?access_token=2.00JbjGiB88nsLBeb9e23f61eBN2pJC&q=%E9%9A%94%E5%A3%81%E8%83%A1%E5%B0%8F%E5%A7%90%E7%9A%84%E7%B3%9F%E5%BF%83%E5%BE%80%E4%BA%8B
    root_url="http://weibo.com/p/100808203abae913c49270ad2a0b769cc32a87?k=%E9%9A%94%E5%A3%81%E8%83%A1%E5%B0%8F%E5%A7%90%E7%9A%84%E7%B3%9F%E5%BF%83%E5%BE%80%E4%BA%8B&from=501&_from_=huati_topic"
    obj_spider=SpiderMain()
    obj_spider.craw(root_url)