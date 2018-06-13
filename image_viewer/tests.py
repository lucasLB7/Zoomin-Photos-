from django.test import TestCase
from .models import Editor, Image, Tag, Category
import datetime as dt




class EditorTestClass(TestCase):
    def setUp(self):
        self.lucas = Editor(first_name = "Lucas", last_name = "Lambert", email = "plucaslambert@gmial.com")

    def test_instance(self):
        self.assertTrue(isinstance(self.lucas,Editor))
    
    def test_save_method(self):
        self.lucas.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)


class ImageTestClass(TestCase):
    def setUp(self):
        # Creating a new editor and saving it
        self.james = Editor(first_name = 'Lucas', last_name ='Lambert', email ='plucaslambert@gmial.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = Tag(name = 'testing')
        self.new_category = Category(name = 'testing')
        self.new_tag.save()

        self.new_image = Image(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_image.save()

        self.new_image.tag.add(self.new_tag)



