#!/usr/bin/python
#-*-coding:utf-8 -*-

import re

file_path = raw_input("�������ļ�·����")		#����Ҫ������ļ�

with open(file_path,"r") as f:					#���ļ�
	file=f.read()
	words_list = re.findall(r"[a-zA-Z]+",file)		#��ȡ����
	
words_dict={}									#����һ���յ��ֵ�

for i in words_list:							#ͳ�Ƶ��ʵ�Ƶ��
	if words_list.count(i)>0:					#��������ΪKey,����Ƶ����Ϊvalue����һ���ֵ�
		words_dict[i] = words_list.count(i)
		
words_list_2 = sorted(words_dict.items(),key = lambda x:x[1],reverse = True)

my_file = open(file_path,"a+")
print >> my_file,""
for word in words_list_2:
	print >> my_file,word
my_file.close()
