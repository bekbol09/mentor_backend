from django.db import models




class Announcement(models.Model):
    LEARN = "Хочу научиться"
    TEACH = "Могу научить"
    TYPE_OF_ADS = [
            (LEARN,"Хочу научиться"),
            (TEACH,"Могу научить"),
    ]


    subcategory = models.ForeignKey('Subcategory', on_delete=models.CASCADE, related_name="announcements", null=True, blank=True)
    type = models.CharField(max_length=100,choices=TYPE_OF_ADS, default=LEARN)
    title = models.CharField(max_length=155)
    description = models.TextField(verbose_name="description")
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    main_image = models.ImageField(upload_to="image/announcement/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.title
    
class Category(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.title

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)

    def __str__(self):
        return self.title
