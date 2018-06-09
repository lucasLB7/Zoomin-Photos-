from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image,Category,Tag

def homePageElements(request):
    all_images = Image.view_all_pictures()
    rel_categories = Category.objects.all()
    date = dt.date.today()
    
    return render(request, 'homepage.html', {"date": date, "all_images": all_images, "rel_categories":rel_categories})





def images_by_date(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    # if date == dt.date.today():
    #     return redirect(news_today)
    
    img = Image.pictures_by_date(date)
    return render(request, 'all_images/image.html', {"date": date, "img":img})






def search_results(request):

    if 'article' in request.GET and request.GET["article"]:
        search_term = request.GET.get("article")
        searched_articles = Article.search(search_term)
        message = f"{search_term}"

        return render(request, 'projects/search.html', {"message":message, "articles": searched_articles})
    else:
        message = "Oop, looks like that doesn't exist.."
        return render(request, 'projects/search.html',{"message":message})


def image(request, image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,'all_images/image.html', {"image":image})

# def categories(request):
#     category = Category.objects.all()
#     return render(request,'projects/article.html', {"category":category})
