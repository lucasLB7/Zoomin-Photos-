from django.shortcuts import render
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Image,Category,Tag, Location
from django.db.models import Q

def homePageElements(request):
    all_images = Image.view_all_pictures()
    rel_categories = Category.objects.all()
    rel_tags = Tag.objects.all()
    date = dt.date.today()
    location = Location.objects.all()
    title = "home"
    
    
    return render(request, 'homepage.html', {"date": date, "all_images": all_images, "rel_categories":rel_categories, "rel_tags":rel_tags, "location": location, "title":title})





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
        searched_articles = Image.search_by_title(search_term) or Tag.search_by_tag(search_term)
        message = f"{search_term}"
        date = dt.date.today()

        return render(request, 'all_images/search.html', {"message":message, "articles": searched_articles, "date":date})
    else:
        message = "You havne't searched for any term"
        date = dt.date.today()
        return render(request, 'all_images/search.html',{"message":message, "date":date})

def image(request, image_id):
    date = dt.date.today()

    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,'all_images/image.html', {"image":image, "date":date})

# def categories(request):
#     category = Category.objects.all()
#     return render(request,'projects/article.html', {"category":category})
