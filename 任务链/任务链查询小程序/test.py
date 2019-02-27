# _*_ coding:utf-8 _*_
#import urllib.request
import re
import sys
#import graphviz

'''
#在线获取
html_src = urllib.request.urlopen("https://zh.kcwiki.org/wiki/%E4%BB%BB%E5%8A%A1")
html = bytes.decode(html_src.read())
'''
'''
#存储至文件
file = open("src.txt", "w", encoding="utf-8")
file.write(bytes.decode(html_src.read()))
'''
file = open("src.txt", "r", encoding="utf-8")
html = file.read()

re_str = "<tr>.*?</tr>"
m = re.findall(re_str, html, re.M | re.S)
d = {}
d2 = {}
for line in m:
    #print(line)
    re_str2 = "id=\"[A-Za-z]+[0-9]+\""
    m2 = re.findall(re_str2, line, re.M | re.S)
    k = ""
    if len(m2) > 0:
        re_str3 = ">[A-Za-wy-z]+[0-9]+<"
        m3 = re.findall(re_str3, line, re.M | re.S)
        m4 = []
        for label in m3:
            m4.append(label[1:len(label)-1])
        k = m2[0][4:len(m2[0])-1]
        d[m2[0][4:len(m2[0])-1]] = m4
    else:
        continue
    #for <td>..</td>
    re_str_td = "<td .*?>.*?</td>"
    m5 = re.findall(re_str_td, line, re.M | re.S)
    r_l = []
    if len(m5) == 10:
        re_str_text = ">([^>]+?)<"
        cnt = 0
        for i in m5:
            #print(i)
            i = i.replace("\n", "")
            if cnt != 1:
                i = i.replace("<br />", "\n")
            else:
                i = i.replace("<br />", " ")
            m6 = re.findall(re_str_text, i, re.M | re.S)
            res = ""
            for i2 in m6:
                res += i2
            #print(res)
            r_l.append(res)
            cnt += 1
    v2 = "【编号】%s【前置】%s\n【任务名称】\n%s\n【任务说明】\n%s\n【油】%s【弹】%s【钢】%s【铝】%s\n【奖励】\n%s\n【备注】\n%s\n" % tuple(r_l)
    d2[k] = v2
    #print(v2)
#print(d2)
to_search = sys.argv[1]
res_l = [to_search]
cnt = 0
while len(res_l) > cnt:
    for t in d[res_l[cnt]]:
        if res_l.count(t) == 0:
            res_l.append(t)
    cnt += 1
res_l.reverse()
for n in res_l:
    print(d2[n])
'''
#任务链存储为图像
#需要安装graphviz
g = graphviz.Digraph("result")
for k in d:
    g.node(k)
for k in d:
    for v in d[k]:
        g.edge(v, k)
g.view("result")
'''
