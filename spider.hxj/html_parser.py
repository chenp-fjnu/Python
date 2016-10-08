#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import urllib.parse
class HtmlParser:
    def parse(self, content):
        if content is None:
            return
        soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
        
        new_data = self._get_new_data(soup)
        return new_data
    def _get_new_data(self, soup):
        res_data={}
        # <div class="WB_text W_f14" node-type="feed_list_content"><a class="a_topic" href="http://huati.weibo.com/k/%E9%9A%94%E5%A3%81%E8%83%A1%E5%B0%8F%E5%A7%90%E7%9A%84%E7%B3%9F%E5%BF%83%E5%BE%80%E4%BA%8B?from=501" target="_blank" suda-uatrack="key=topic_click&amp;value=click_topic" extra-data="type=topic" render="ext">#隔壁胡小姐的糟心往事#</a>我有一个情人，相处整整一年了，性生活和谐，他称我为尤物，直到我们的缘分结束了，我都不知道自己到底有没有爱过他，只知道那时候为他流过的眼泪，心酸是真的，想和他在一起一辈子也是真的，那种互不干涉家庭的基础上。可我有一件事耿耿于怀，到现在我他妈都不知道他的名字和他...<a class="WB_text_opt" href="/3289792374/E9Vl5vZRg" target="_blank" suda-uatrack="key=original_blog_unfold&amp;value=click_unfold:4023653677625954:3289792374" action-data="mid=4023653677625954&amp;is_settop&amp;is_sethot&amp;is_setfanstop&amp;is_setyoudao" action-type="fl_unfold">展开全文<i class="W_ficon ficon_arrow_down">c</i></a></div>
       
        content_node=soup.find('div', class_='WB_text W_f14').find('h1')
        
        res_data['content']=content_node
        res_data['content_text']=content_node.get_text()
        return res_data
