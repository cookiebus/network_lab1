network lab1
===================================  
小组成员: 
    高成良 1200012948
    陈敏焕 1200012757
    黄丽明 1200012907
    田堃   1200012845


###
    创建数据库：
    sudo su postgres psql
    create database news;
    create user news with password 'news';
###
    在终端执行：
    network_lab1 目录下执行
    python manage.py syncdb //同步数据库
    python manage.py runserver　//本地运行
    
###
    127.0.0.1:8000/spider 允许爬虫程序
    127.0.0.1 访问爬下来的网页
