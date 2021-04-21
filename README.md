# 海味开发文档

## 项目结构说说明

```
djangoProject1/
    home.py		#自己添加的文件，未用
    __init__.py
    settings.py	# 项目配置文件
    urls.py	    # 定义网站子链接文件
    views.py		# 视图渲染文件，将模板渲染成显示的网页页面
    wsgi.py		
static/			# 存放静态文件，样式、字体等
    css/
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
python3 manage.py runserver 0.0.0.0:8000
```

## 查看
[http://127.0.0.1:8000/index/](http://127.0.0.1:8000/index/)


