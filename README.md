# Chinese-solution-to-obsidian-kindle-plugin

## 前情提要   
[Obsidian](https://obsidian.md/)是一款非常有意思的笔记软件，可以结合多种插件管理笔记。  
[Kindle Highlights](https://github.com/hadynz/obsidian-kindle-plugin)是一款Obsidian的插件，可以将Kindle中的书摘导入到Obsidian中，方便使用Obsidian管理并形成可视化知识图谱。  
然而，在使用该插件的`My Clippings.txt`导入方式时，似乎不支持解析中文的引用和时间信息，即类似于`- 您在第 574 页（位置 #8918-8918）的标注 | 添加于 2023年10月6日星期五 下午11:20:54`这样的语句。具体issue可点击[这里](https://github.com/hadynz/obsidian-kindle-plugin/issues/263)查看。  
因此，笔者写了这个小片段，将所有类似于上述格式的字符串全部转为英文格式再进行导入，发现插件能够正常应用。  
请注意，笔者此处只是提出了一个最简单的解决措施，并未结合该插件原有逻辑以及解析方法，也许这并不是报错的根本原因（但是可以导进去就是了呃呃呃我很急）  

## 使用方法
1. 将`Convert.py`下载到`My Clippings.txt`所在的文件夹。
2. 运行`Convert.py`。
3. 将产生的`output_file.txt`上传到原插件里进行导入。

## Background
[Obsidian](https://obsidian.md/) is an interesting writing app to keep notes with all kinds of plugins.  
[Kindle Highlights](https://github.com/hadynz/obsidian-kindle-plugin) is one of the plugins to sync your Kindle notes and highlights directly into your Obsidian vault.  
However, while using `My Clippings.txt` to upload the highlights, it seems that Chinese strings cannot be parsed. See [here](https://github.com/hadynz/obsidian-kindle-plugin/issues/263) for more.  
So I wrote this Python snippet which can be used to process the original `My Clippings.txt`. What it actually does is to convert all the location and datetime information to English.  
Please note that this is only a brute-force solution with no reference to the plugin's original logic.  
But it works :P

## Usage
1. Download `Convert.py` under the same directory with `My Clippings.txt`.
2. Run `Convert.py`.
3. Upload the generated `output_file.txt` to the plugin.
