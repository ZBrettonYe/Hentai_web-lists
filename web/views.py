from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Site, Category, SmallCategory


def index(request):
    outer_categorys = Category.objects.filter(guonei=0).all()
    inner_categorys = Category.objects.filter(guonei=1).all()
    return render(request, 'web/index.html', locals())


@csrf_exempt
@require_POST
def sitelist(request):
    classId = request.POST['classId']
    category = Category.objects.filter(id=classId).first()
    sites_result = {"dataResult": []}
    small_categorys = SmallCategory.objects.filter(category=category).all().values("id", "name")
    for small_category in small_categorys:
        sites = Site.objects.filter(smallcategory=small_category.get('id')).all().values()
        c = {"id": small_category.get('id'), "className": small_category.get('name'), "description": small_category.get('name'), "siteVos": []}
        for site in sites:
            if site.get('id') and small_category.get('id'):
                a = {"id": site.get('id'), "siteName": site.get('name'), "siteUrl": site.get('true_url'), "logoResourceId": site.get('image_url')}
                c["siteVos"].append(a)
        sites_result['dataResult'].append(c)
    response = JsonResponse(sites_result, safe=False)
    return response


