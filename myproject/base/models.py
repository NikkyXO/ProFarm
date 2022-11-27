from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=20)
    id = models.IntegerField(unique=True)
    supplier_id = models.CharField(max_length=20)
    unit_price = models.floatField(max_length=12)
    isDiscontinued = models.BooleanField(default=True)
    InStock = models.BooleanField(default=False)
    Review = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=255)

    def get_absolute_url(self):
        return reverse()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.id)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        pub_date = ['created_on']

        def __unicode__(self):
            return self.id

class Comment(models.Model):
	name = models.CharField(max_length=42)
	email = models.EmailField(max_length=75)
	website = models.URLField(max_length=200, null=True, blank=True)
	content = models.TextField()
	post = models.ForeignKey(Product, on_delete=models.CASCADE)
	created_on = models.DateTimeField(auto_now_add=True)
  

    
