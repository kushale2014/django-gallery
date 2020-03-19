from django.db import models

class Album(models.Model):
    objects = models.Manager()
    title = models.CharField('название альбома', max_length=100)
    description = models.CharField("описание альбома", max_length=200)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'

class Image(models.Model):
    objects = models.Manager()
    album = models.ForeignKey(Album, verbose_name="альбом", on_delete=models.PROTECT)
    image_name = models.ImageField(upload_to='gallery')
    description = models.CharField("описаните картинки", max_length=200)
    
    def __str__(self):
        return self.image_name.name
    
    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'