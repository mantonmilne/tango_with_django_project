import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django

django.setup()
from rango.models import Category, Page


def populate():
    # Firstly a list of dictionaries containing the pages
    # we want to add into each category is created.
    # After that we then create a dictionary of dictionaries for our categories

    python_pages = [
        {'title': 'Official Python Tutorial',
         'url': 'http://docs.python.org/3/tutorial/',
         'views': 10},
        {'title': 'How to Think like a Computer Scientist',
         'url': 'http://www.greenteapress.com/thinkpython/',
         'views': 14},
        {'title': 'Learn Python in 10 Minutes',
         'url': 'http://www.korokithakis.net/tutorials/python/',
         'views': 20}
    ]

    django_pages = [
        {'title': 'Official Django Tutorial',
         'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
         'views': 50},
        {'title': 'Django Rocks',
         'url': 'http://www.djangorocks.com/',
         'views': 3},
        {'title': 'How to Tango with Django',
         'url': 'http://www.tangowithdjango.com/',
         'views': 18}
    ]

    other_pages = [
        {'title': 'Bottle',
         'url': 'http://bottlepy.org/docs/dev/',
         'views': 4},
        {'title': 'Flask',
         'url': 'http://flask.pocoo.org',
         'views': 33}
    ]

    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
            'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
            'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16} }

    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], views=p['views'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


# below instructions are a useful trick to allow this module to act as both reusable
# module or a standalone Python script. A reusable module is one that can be imported in
# to another module (e.g. through an import statement), which a standalone Python script
# would be executed from the terminal by entering python module.py.
# The below code will therefore only be run if used as a standalone Python script. Importing
# will not run the script, but will allow you access to the classes or functions.
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
