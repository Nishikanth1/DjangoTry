from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request,*args, **kwargs):
    print("request is {0}".format(request.user))
    print('args is {0}'.format(args))
    print('kwargs is {0}'.format(kwargs))
    return render(request, "home.html", {})
    # return HttpResponse("<h1>Hello World</h1>")

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})
    # return HttpResponse("<h1>This is contact view please note down the contact details lel.</h1>")


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text": 'This is a text called my_text',
        "my_number": 125,
        "my_list": ['a', 1, 2, 3, 4],
        "center": "This is the center_var",
        "capfirst_var": "this is the capfirst and upper",
        "html_var": "<h1>This-is the html</h1>"
        }
    return render(request, 'about.html', my_context)