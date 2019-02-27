# 任务链查询程序

---

## 数据来源

kcwiki 舰娘百科[任务一览](https://zh.kcwiki.org/wiki/%E4%BB%BB%E5%8A%A1)

---

## 使用说明

在目录下使用命令行命令

    python query.py 你想查询的任务编号

若想保存任务链至文本，继续输入save，保存至 **./任务编号.txt**

若希望保存任务链至图片，需要安装 graphviz 包，并且输入save image，保存至 **./任务编号.pdf**
 - (不存在的，韬酱罢工了不写了)

否则请输入quit

---

## 使用环境

python 3.6+