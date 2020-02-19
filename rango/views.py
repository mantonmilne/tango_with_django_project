from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category
from rango.models import Page

def index(request):

    # This instruction queries the database for a list of all the categories
    # it then has them listed in descending order ('-likes')
    # and then retrieves only the top 5 of these [:5], or all if there are 5 or less
    category_list = Category.objects.order_by('-likes')[:5]

    # added for exercises for chapter 6
    page_list = Page.objects.order_by('-views')[:5]

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!

    # category_list is added to the context_dict as 'categories'

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list



    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict)

def about(request):

    # do we need a context_dict ? Don't think so as one is not referenced in about.html
    # context_dict = {''}
    return render(request, 'rango/about.html')

def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # The .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)

        # Retrieve all of the associated pages.
        # The filter() will return a list of page objects or an empty list.
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages.
        context_dict['pages'] = pages
        # We also add the category object from
        # the database to the context dictionary.
        # We'll use this in the template to verify that the category exists.
        context_dict['category'] = category

    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['pages'] = None

    # Go render the response and return it to the client.
    return render(request, 'rango/category.html', context=context_dict)


# removed in exercise 4.4
#def about(request):
#    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")
