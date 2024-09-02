from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User


class File(models.Model):
    file = models.FileField(upload_to='files/', null=False, blank=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.file.name


class Category(models.Model):
    title = models.CharField(max_length=255, null=False, help_text=_("Category title"))
    icon = models.ImageField(upload_to='categories', null=True, blank=True)
    order = models.IntegerField(default=0, null=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['order']


class Tag(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, help_text=_("Tag name"))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Tags"


class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False, help_text=_("Post title"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts", null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", null=False)
    images = models.ManyToManyField(File, default=None, null=True, blank=True)
    description = models.TextField(null=True, blank=True, help_text=_("Additional info"))
    tags = models.ManyToManyField(Tag, default=None, null=True, blank=True)

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"
        ordering = ['-created_at']


class Featured(models.Model):
    """ Partner brands """
    title = models.CharField(max_length=255, null=True, blank=True)
    icon = models.ImageField(upload_to='featured', null=False, blank=False)

    def __str__(self):
        return self.title or f"#{self.pk}"