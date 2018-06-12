# Zoomin-pictures! 



This is a Django app created that allows users to view pictures by category, tag and country.

The app uses the ```django``` framework to create a set of backend databases that are then templated in the main application.

As a user you can also search by **category type**, **tags** or **title**.



## Building the app

It is best to use the python `virtualenv` tool to build locally:

```
$ virtualenv venv --python-3.6.2
$ source venv/bin/activate
$ pip install -r requirements.txt
$ DEVELOPMENT=1 python manage.py runserver
```

Then visit `http://localhost:8000` to view the app. 



## requirements.txt

The requirements.txt file serves as a placeholder for python dependancies. 
    Contents:
- astroid==1.6.3
- click==6.7
- dj-database-url==0.5.0
- Django==1.11
- django-bootstrap3==10.0.1
- dominate==2.3.1
- Flask==1.0.2
- Flask-Bootstrap==3.3.7.1
- Flask-Script==2.0.6
- Flask-WTF==0.14.2
- gunicorn==19.8.1
- isort==4.3.4
- itsdangerous==0.24
- Jinja2==2.10
- lazy-object-proxy==1.3.1
- MarkupSafe==1.0
- mccabe==0.6.1
- Pillow==5.1.0
- psycopg2==2.7.4
- psycopg2-binary==2.7.4
- pyperclip==1.6.2
- python-decouple==3.1
- pytz==2018.4
- six==1.11.0
- visitor==0.1.3
- Werkzeug==0.14.1
- whitenoise==3.3.1
- wrapt==1.10.11
- WTForms==2.1

**Once you have run the ```pip installation```, verify that you have all the necessary requirements with the following command:**


 ```
 pip3 freeze
 ```

![alt text](./media/thatsall.jpg "Logo Title Text 1")

The app should now run smoothly on your local server.......

__If it doesn't work or you are experiencing errors__, please report to: 

<plucaslambert@gmail.com>



## Functionality breakdown

__Let's get down and dirty & see how this app code works:__

1. Components:

Our app contains standard django templating conponenets that handle __functionalities__, __routing__, __views__ and __templating__.

```Functionalites``` are handled by our __MODELS__ file, that defines __objects__ and their respective functions.

EXAMPLE:

```python
class Image(models.Model):
    title = models.CharField(max_length = 60)
    description = models.TextField()
    editor = models.ForeignKey(Editor)
    category = models.ManyToManyField(Category, related_name='category')
    tag = models.ManyToManyField(Tag, related_name='tag')
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'view_images/')
    location = models.ManyToManyField(Location, related_name='location')
    

    @classmethod
    def search_by_title(cls,search_term):
        title_search = cls.objects.filter(title__icontains = search_term)
        return title_search
```

## Persistent Connections

By default, Django doesn't use persistent connections with memcached. This is a
huge performance problem, especially when using SASL authentication as the
connection setup is even more expensive than normal.

You can fix this by putting the following code in your `wsgi.py` file:

```python
# Fix django closing connection to MemCachier after every request (#11331)
from django.core.cache.backends.memcached import BaseMemcachedCache
BaseMemcachedCache.close = lambda self, **kwargs: None
```

There is a bug file against Django for this issue
([#11331](https://code.djangoproject.com/ticket/11331)).

## Application Code

In your application, use django.core.cache methods to access
MemCachier. A description of the low-level caching API can be found
[here](https://docs.djangoproject.com/en/1.8/topics/cache/#the-low-level-cache-api).
All the built-in Django caching tools will work, too.

Take a look at
[memcachier_algebra/views.py](https://github.com/memcachier/examples-django/blob/master/memcachier_algebra/views.py)
in this repository for an example.

## Get involved!

We are happy to receive bug reports, fixes, documentation enhancements,
and other improvements.

Please report bugs via the
[github issue tracker](http://github.com/memcachier/examples-django/issues).

Master [git repository](http://github.com/memcachier/examples-django):

* `git clone git://github.com/memcachier/examples-django.git`

## Licensing

This library is BSD-licensed.


![alt text](./media/1.jpg "Logo Title Text 1")
