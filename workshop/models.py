from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Workshop(models.Model):
    category_name = models.ForeignKey('Category', null=True, blank=True, 
                                      on_delete=models.SET_NULL)
    workshop_name = models.CharField(max_length=254)
    title = models.CharField(max_length=254)
    description = models.TextField()
    hosted_by = models.CharField(max_length=254)
    from_date = models.DateTimeField()
    to_date = models.DateTimeField()
    venue = models.CharField(max_length=254, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.workshop_name


