from django.db import models

class Editor(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    nick_name = models.CharField(max_length = 20, blank = True)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10, blank = True)
    editor_photo = models.ImageField(upload_to = 'editors/')
    
    def __str__(self):
        return self.first_name
    
    def save_editor(self):
        self.save()

    def delete_editor(self):
        self.delete()

    class Meta:
        ordering = ['first_name']



class Category(models.Model):

    category_type = models.CharField(max_length = 100)

    def __str__(self):
        return self.category_type


class Tag(models.Model):

    tags = models.CharField(max_length = 30)

    def __str__(self):
        return self.tags


class Image(models.Model):
    title = models.CharField(max_length = 60)
    description = models.TextField()
    editor = models.ForeignKey(Editor)
    category = models.ManyToManyField(Category, related_name='category')
    tag = models.ManyToManyField(Tag, related_name='tag')
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'view_images/')


    @classmethod
    def search_pictures(cls, search_term):
        result = cls.objects.filter(title__icontains = search_term , category__icontains = search_term , pub_date__date = search_term, tag__icontains = search_term)
        return results
    # @classmethod
    # def search_by_category(cls, search_term):
    #     result = cls.objects.filter(category__icontains = search_term)
    #     return results
    # @classmethod
    # def search_by_date(cls, search_term):
    #     result = cls.objects.filter(pub_date__date = search_term)
    #     return results


    @classmethod
    def view_all_pictures(cls):
        results = cls.objects.filter()
        return results
    
    @classmethod
    def pictures_by_date(cls,date):
        results = cls.objects.filter(pub_date__date = date)
        return results




