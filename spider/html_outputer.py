#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class HtmlOutputer(object):
    def __init__(self):
        self.datas =[]
    def collect_data(self,data):
        if data is None:
            return
        self.datas.append(data)
    def output_html(self):
        fout=open('output.html',mode='w',encoding="utf-8")
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        #ascii
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'].encode('gb2312'))
            fout.write("<td>%s</td>" % data['summary'].encode('gb2312'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
        