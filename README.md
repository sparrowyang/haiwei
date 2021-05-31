# 海味开发文档

## 项目结构说说明

```
haiwei/
    home.py		#自己添加的文件，未用
    __init__.py
    settings.py	# 项目配置文件
    urls.py	    # 定义网站子链接文件
    views.py	# 视图渲染文件，将模板渲染成显示的网页页面
    wsgi.py		
static/			# 存放静态文件，样式、字体等
    css/
        custom.css #自定义样式表
    js/
    icon/
    font/
templates/		# 存放用于给views.py渲染的模板 
manage.py 		# 不需要修改
```

## 依赖环境
- python3
- django

### 使用pip解决依赖包

项目根目录：
```
pip install -r requirements.txt
```

## 运行
项目根目录：
```bash
python manage.py runserver
```

## 查看
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)


## 前端框架
[MDUI](https://www.mdui.org/)

## 开发

### 前端 
于templates文件夹编写html模板页面。

### 后端
于haiwei文件夹编写python,调用数据库等。

### 后记
1. 季节性选择
2. 


