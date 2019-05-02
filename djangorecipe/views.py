from django.shortcuts import render
from djangorecipe.models import Recipes, Author


def list_view(request):
    html = 'list_view.html'
    items = Recipes.objects.all().order_by('title')
    return render(request, html, {'list': items})


def recipe_info(request, id):
    html = 'recipe_info.html'
    items = Recipes.objects.all().filter(id=id)
    instructions = items[0].instructions.split('\n')
    return render(request, html,
                  {'recipes': items, 'instructions': instructions})


def author_info(request, id):
    html = 'author_info.html'
    authors = Author.objects.all().filter(id=id)
    items = Recipes.objects.all().filter(author_id=id)
    return render(request, html, {'authors': authors, 'recipes': items})
