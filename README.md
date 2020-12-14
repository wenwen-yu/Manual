# Manuals

@( Manuals for ) [Mech-Viz | Mech-Vision | Mech-Eye]


## Requirements:

1. install [python3.6](https://www.python.org/downloads/windows/)(suggest Environment configuation with Anaconda), As for the editor, VS Code in Anaconda is suggested;
2. ```pip install sphinx```;
3. ```pip install sphinx_rtd_theme```;
4. ```git clone https://github.com/MechMindRobotics/Manuals.git```
5. run ```./make html``` and then you will find the html files in *../Manuals_build* directory
   >  or run```sphinx-build.exe -b html ./source/ ./[BUILD_FILE]```is all right with Windows

## 文档编写时的注意事项：

#### Rules:
1. 统一软件命名: 文档中出现软件名称的时候，要写成 **Mech-Viz、Mech-Vision、Mech-Eye Viewer、Mech-Hub**的形式。
2. 文档中添加注意事项时，统一使用note、tip、attention；
   按照程度划分：说明用**note**，提示用**tip**，注意用**attention**
3. 文档中涉及公司名称的，要用公司全称：**梅卡曼德(北京)机器人科技有限公司**


>**Tips：**
>1. 注意使用空格和空行
>2. 编辑表格时，需要使用等宽字体(中文字符 = 2*英文字符)


### 文档组织结构：
+ 文档文件夹
    + 文档组织列表.rst
    + 章节1文件夹
        + 本章内容.rst
        + image文件夹
    + 章节2文件夹  
        + ..
    + ...


## FAQ:
### 1、如果编写环境是：sublime text
推荐几个工具：
1.rst预览工具：```OmniMarkupPreviewer``` 
2.rst格式化工具：```Restructured Text (RST) Snippets``` 