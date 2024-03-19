from django.db import models

# Create your models here.
class InfoUser(models.Model):
    name = models.CharField(
        max_length = 255,
        verbose_name = "Имя пользователя"
    )
    image = models.ImageField(
        upload_to= "info_user/",
        verbose_name= "Фотография пользователя"
    )
    
    work = models.CharField(
        max_length = 255,
        verbose_name = "Профессия"
    )
    
    age = models.IntegerField(
        
        verbose_name = "Возраст"
    )
    
    froms = models.CharField(
        max_length = 255,
        verbose_name = "Откуда"
    )
    
    email = models.EmailField(
        max_length = 255,
        verbose_name = "Почта"
    )
    
    locate = models.CharField(
        max_length = 255,
        verbose_name = "Адрес"
    )
    
    phone = models.CharField(
        max_length = 255,
        verbose_name = "Телофонный номер"
    )
    
    instagram = models.URLField(
        max_length = 255,
        verbose_name = "Instagram",
        blank = True, null = True
    )
    
    facebook = models.URLField(
        max_length = 255,
        verbose_name = "Facebook",
        blank = True, null = True
    )
    
    youtube = models.URLField(
        max_length = 255,
        verbose_name = "Youtube",
        blank = True, null = True
    )
    
    
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        verbose_name = "Данные пользователя"
        verbose_name_plural = "Данные пользователей"
        
        
        
class Secondary(models.Model):
    image = models.ImageField(
        upload_to= "secondary/",
        verbose_name = "Фото пользователя"
    )
    
    tittle = models.CharField(
        max_length = 255,
        verbose_name = "Коротко о себе"
    )   
    
    description = models.TextField(
        max_length = 255,
        verbose_name = "О Себе"
    )
    
    
    def __str__(self):
        return self.tittle
    
    class Meta:
        verbose_name = "О пользователе"
        verbose_name_plural = "О пользователей"
    
    