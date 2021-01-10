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
### **Basic API is working here**

## Part 2 & 3: Requests/Responses and Views

**Part 2**: Entirely rewrote views.py with little modificaitons of snippets/urls.py. But other than that no changes. Allowes for webbased API with UI.

**Part 3**: Entirely rewrote views.py twice, with little modificaitons of snippets/urls.py. But other than that no changes.

Result is most generic views with minimal amount of code.

## Part 4: Authentication & Permissions (also Blueprint for extending app/model)

In this part:

* Code snippets are always associated with a creator.
* Only authenticated users may create snippets.
* Only the creator of a snippet may update or delete it.
* Unauthenticated requests should have full read-only access.

The following steps were taken to achieve this:

1. Update models.py and make new db including some superusers.
2. Added `UserSerializer` class in serializers.py
3. Define `UserList` and `UserDetail` in views.py with generic constructors and update snippets/urls.py to include paths to user views.
4. **Key step**: associate snippets with users - add `perform_create` method to `SnippetList` class

   ```
   def perform_create(self, serializer):
       serializer.save(owner=self.request.user)
   ```
5. Update serializer.py with an `owner` field.
6. **Key step**: define permissions as `permission_classes` in the two view-classes `SnippetList` and `SnippetDetail`:

   ```
   permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   ```
7. Update project-level urls.py to be able to login on api UI level.
8. **Key step**: create *permissions.py* and define class to be used to have custom behaviour

## Part 5: Relationships and Hyperlinked APIs

We replace primary keys with hyperlinks for relating fileds/elements.

1. In *views.py* add `api_root` and `SnippetHighlight`.
2. In *urls.py* add root path '' and for snippet highlighting.
3. Hyperlinking API by updating corresponding serializers `SnippetSerializer` and `UserSerializer`.
4. Naming URL patterns and adding pagination in *settings.py*

## Part 6: ViewSets & Routers

This part introduces ViewSets and Routers to reduce the code to be written. One loses flexibilty however.

