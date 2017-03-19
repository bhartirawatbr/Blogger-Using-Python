bharti

1.install celery= pip install celery

2.In installed app add= 'djcelery'

3.Then install it = pip install django-celery

4.Then migrate it= python manage.py migrate

5.debbug task.pyfile of celery= 

from celery.contrib import rdb
    rdb.set_trace()

6. Then open a tab in a terminal: 
run celery= celery -A myblogger worker -l info or  celery -A myblogger worker --loglevel=info

7.Then get the port from the celery tab eg: 127.0.0.1 6901

8.Then open another tab and type : telnet 127.0.0.1 6901

now finally tasks.py can be debug


