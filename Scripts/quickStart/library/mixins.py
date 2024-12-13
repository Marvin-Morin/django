from django.http import HttpRequest, HttpResponse, HttpResponseForbidden

class PostPermissionMixin:
    def post(self, request: HttpRequest, *args, **kwargs)->HttpResponse:
        
        if request.method == "POST" and '_method' in request.POST:
            return super().delete(request, *args, **kwargs)
        
        if request.method == "POST" and not request.user.is_authenticated:
            return HttpResponseForbidden('Not allowed')
        return super().dispatch(request, *args, **kwargs)