# -*- coding: utf-8 -*-

import re
from datetime import datetime

# 读取文本文件
with open('My Clippings.txt', 'r', encoding='utf-8') as file:
    text = file.read()

#format examples:
#- 您在第 (\d+) 页（位置 #(\d+)-(\d+)）的标注 \| 添加于 (\d+)年(\d+)月(\d+)日星期五 下午(\d+):(\d+):(\d+)
#- Your Highlight on page 607 | location 9399-9399 | Added on Wednesday, 11 October 2023 12:09:00
#- 您在位置 #395-396的标注 | 添加于 2019年1月28日星期一 下午4:34:42
#- Your Highlight at location 829-830 | Added on Tuesday, 10 October 2023 21:09:36
#- 您在位置 #209 的书签 | 添加于 2017年12月9日星期六 下午10:09:32
#- 您在第 19 页的书签 | 添加于 2017年12月9日星期六 下午10:09:32
#- 您在第 78 页（位置 #1558）的书签 |
#- Your Bookmark on page 607 | location 9399 | Added on Wednesday, 11 October 2023 14:38:07


#Convert timestamp
pattern = r'添加于 (\d+)年(\d+)月(\d+)日星期([^\x00-\xff]) ([^\x00-\xff])午(\d+):(\d+):(\d+)'
matches = re.findall(pattern, text)
for match in matches:
    year, month, day, week, halfday, hour, minute, second = match
    if int(hour)==12:
        hour=0
    if halfday=="下":
        hour=int(hour)+12
            
    date_time = datetime(int(year), int(month), int(day), int(hour) , int(minute), int(second))  # 转换为24小时制的时间
    new_statement = f'Added on {date_time.strftime("%A, %d %B %Y %H:%M:%S")}'
    text = text.replace('添加于 {}年{}月{}日星期{} {}午{}:{}:{}'.format(*match), new_statement)

#Convert loc info
pattern = r'- 您在第 (\d+) 页（位置 #(\d+)-(\d+)）的标注'
matches = re.findall(pattern, text)
for match in matches:
    page, start, end = match
    new_statement = 'Your Highlight on page {} | location {}-{}'.format(page,start,end)
    text = text.replace('您在第 {} 页（位置 #{}-{}）的标注'.format(*match), new_statement)
pattern = r'- 您在第 (\d+) 页（位置 #(\d+)）的标注'
matches = re.findall(pattern, text)
for match in matches:
    page, loc = match
    new_statement = 'Your Highlight on page {} | location {}'.format(page,loc)
    text = text.replace('您在第 {} 页（位置 #{}）的标注'.format(*match), new_statement)
pattern = r'- 您在位置 #(\d+)-(\d+)的标注'
matches = re.findall(pattern, text)
for match in matches:
    start, end = match
    new_statement = 'Your Highlight at location {}-{}'.format(start,end)
    text = text.replace('您在位置 #{}-{}的标注'.format(*match), new_statement)
pattern = r'- 您在第 (\d+)-(\d+) 页的标注'
matches = re.findall(pattern, text)
for match in matches:
    start, end = match
    new_statement = '- Your Highlight on page {}-{}'.format(start,end)
    text = text.replace('- 您在第 {}-{} 页的标注'.format(*match), new_statement)
pattern = r'- 您在第 (\d+) 页的标注'
matches = re.findall(pattern, text)
for match in matches:
    page = int(match)
    new_statement = '- Your Highlight on page {}'.format(page)
    text = text.replace('- 您在第 {} 页的标注'.format(match), new_statement)
pattern = r'- 您在位置 #(\d+)的标注'
matches = re.findall(pattern, text)
for match in matches:
    loc = int(match)
    new_statement = '- Your Highlight on page {}'.format(loc)
    text = text.replace('- 您在位置 #{}的标注'.format(match), new_statement)
pattern = r'- 您在第 (\d+) 页（位置 #(\d+)）的书签'
matches = re.findall(pattern, text)
for match in matches:
    page, loc = match
    new_statement = 'Your Bookmark on page {} | location {}'.format(page,loc)
    text = text.replace('您在第 {} 页（位置 #{}）的书签'.format(*match), new_statement)
pattern = r'- 您在第 (\d+) 页的书签'
matches = re.findall(pattern, text)
for match in matches:
    page = int(match)
    new_statement = '- Your Bookmark on page {}'.format(page)
    text = text.replace('- 您在第 {} 页的书签'.format(match), new_statement)
pattern = r'- 您在位置 #(\d+) 的书签'
matches = re.findall(pattern, text)
for match in matches:
    loc = int(match)
    new_statement = 'Your Bookmark at location {}'.format(loc)
    text = text.replace('您在位置 #{} 的书签'.format(match), new_statement)


#generate the converted file
with open('output_file.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(text)

