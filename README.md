# Description

Following: https://www.django-rest-framework.org/tutorial/1-serialization/ 

## Part 1: Serializers

Create project and app:
```
python manage.py startproject tutorial
python manage.py snippets
```
adapt models.py and create serializers.py. Go into `python manage.py shell` to construct test data.

Update views.py, urls.py and create snippets/urls.py and **done**.

In the views.py the important mehtods for request handling are located, e.g.
```
def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
```