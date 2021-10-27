from django.db import models
from django.utils.html import mark_safe

# Banner for hero images slides
class Banner(models.Model):
    img = models.ImageField(upload_to="banner_imgs/")
    label = models.CharField(max_length=500, null=True, blank=True)
    tag = models.CharField(max_length=500, null=True, blank=True)
    url = models.URLField(max_length=500, null=True, blank=True)
    alt_text = models.CharField(max_length=300)

    def image_tag(self):
        return mark_safe('<img src="%s" width="100" />' % (self.img.url))

    def __str__(self):
        return self.alt_text


# Contact form details
class Contact(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.first_name
