#!/usr/bin/python
#-*-coding:utf-8 -*-

import re

file_one = raw_input("请输入文件路径：")		#导入要处理的文件

with open(file_one,"r") as f:					#打开文件
	file=f.read()
	words_list = re.findall(r"[a-zA-Z]+",file)		#提取单词
	
words_dict={}									#建立一个空的字典

for i in words_list:							#统计单词的频率
	if words_list.count(i)>0:					#将单词作为Key,出现频率作为value建立一个字典
		words_dict[i] = words_list.count(i)
		
words_list_2 = sorted(words_dict.items(),key = lambda x:x[1],reverse = True)

file_two = open(file_one,"a+")
print >> file_two,""
for word in words_list_2:
	print >> file_two,word
my_file.close()
