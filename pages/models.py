# -*- coding: utf-8 -*-
from django.db import models
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from urllib.parse import urlparse, urlsplit
import os
import requests

from slugify import slugify_url


class Availability(models.Model):

    def __str__(self):
        return self.availability_title

    availability_title = models.CharField(max_length=50)


class Publish(models.Model):

    def __str__(self):
        return self.publish_title

    publish_title = models.CharField(max_length=50)


class Images(models.Model):

    def __str__(self):
        return self.images_url

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    images_url = models.URLField(null=True, blank=True)
    images_file = models.ImageField(upload_to='images', null=True, blank=True)
    main = models.BooleanField(default=False)
    offer = models.ForeignKey('Offers', related_name='images')

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None, max_width=0, max_height=0):
        self.get_remote_image(max_width, max_height)
        super().save(force_insert=force_insert, force_update=force_update,
                     using=using, update_fields=update_fields)

    def get_remote_image(self, max_width=0, max_height=0):
        print(max_width)
        if self.images_url and not self.images_file:
            r = requests.get(self.images_url)

            if r.status_code == requests.codes.ok:
                img_temp = NamedTemporaryFile(delete=True)
                img_temp.write(r.content)
                img_temp.flush()

                img_filename = urlsplit(self.images_url).path[1:]

                self.images_file.save(img_filename, File(img_temp), save=True)

        if (max_width or max_height) and self.images_file and (self.images_file.width > max_width or self.images_file.width > max_width):
            w = max_width if max_width else self.images_file.width
            h = max_height if max_height else self.images_file.height
            self.create_thumbnail(w, h)

        return False

    def create_thumbnail(self, w, h):
        if not self.images_file:
            return
        from PIL import Image
        from io import BytesIO, StringIO
        from django.core.files.uploadedfile import SimpleUploadedFile
        import os
        THUMBNAIL_SIZE = (w, h)

        if 'jpg' in self.images_file.name or 'jpeg' in self.images_file.name:
            PIL_TYPE = 'jpeg'
            FILE_EXTENSION = 'jpg'
        elif 'png' in self.images_file.name:
            PIL_TYPE = 'png'
            FILE_EXTENSION = 'png'

        image = Image.open(BytesIO(self.images_file.read()))
        image.thumbnail(THUMBNAIL_SIZE, Image.ANTIALIAS)
        temp_handle = BytesIO()
        image.save(temp_handle, PIL_TYPE)
        temp_handle.seek(0)
        self.images_file.save(self.images_file.name, File(temp_handle), save=False)

# Модель категории
class Category(models.Model):

    def __str__(self):
       return self.category_title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


    category_title = models.CharField(max_length=250)


# Модель страници
class Post(models.Model):

    def __str__(self):
        return self.post_title

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страници'

    post_title = models.CharField(max_length=250)            # <h1></h1>
    post_seourl = models.CharField(max_length=250)           # Ссылка на страницу ( мойсайт.ру/(эта ссылка) )
    post_photo = models.ImageField(blank=True)               # Фото на страницу
    post_text = models.TextField()                          # Текст страници
    post_category = models.ForeignKey(Category, blank=True, null=True)
    post_cat_level = models.IntegerField(default=0)
    # post_submenu = models.BooleanField(default=False)
    # post_mainmenu = models.BooleanField(default=False)


# Модель категории товара
class Tags(models.Model):

    def __str__(self):
        return self.tag_title

    class Meta:
        verbose_name = 'Основные теги'
        verbose_name_plural = 'Основные теги'

    tag_url = models.CharField(max_length=250, unique=True)     # Ссылка на категорию
    tag_title = models.CharField(max_length=250)               # Название категории
    tag_publish = models.BooleanField(blank=True)
    tag_priority = models.IntegerField(blank=True)



# Модель категории товара
class Subtags(models.Model):

    def __str__(self):
        return self.tag_title

    class Meta:
        verbose_name = 'Дополнительные теги'
        verbose_name_plural = 'Дополнительные теги'

    tag_url = models.CharField(max_length=250, unique=True)       # Ссылка на категорию
    tag_title = models.CharField(max_length=250)                  # Название категории
    tag_parent_tag = models.ForeignKey(Tags, blank=True)                  # Parents category

    @classmethod
    def create(cls, tag_title):
        tag = cls(tag_title=tag_title, tag_url=slugify_url(tag_title))
        tag.save()
        # do something with the book
        return tag


# Модель товара
class Offers(models.Model):

    def __str__(self):
        return self.offer_title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    offer_title = models.CharField(max_length=250, verbose_name='Название')                       # Название товара
    offer_price = models.FloatField(default=0, verbose_name='Цена')                           # Price
    offer_price_discount = models.FloatField(blank=True, default=0, verbose_name='Цена со скидкой', null=True)
    offer_discount_term = models.DateTimeField(blank=True, null=True, verbose_name='Срок действия скидки')
    offer_price_from = models.FloatField(blank=True, default=0, verbose_name='Цена от')
    offer_price_to = models.FloatField(blank=True, default=0, verbose_name='Цена до')
    offer_valuta = models.CharField(max_length=40, verbose_name='Валюта')                       # Валюта
    offer_value = models.CharField(max_length=50, blank=True, verbose_name='Единица измерения')            # Еденица измерения товара
    offer_minorder = models.IntegerField(default=1, verbose_name='Минимальный размер заказа')
    offer_minorder_value = models.CharField(max_length=50, blank=True, verbose_name='Единица измерения минимального заказа')   # Еденица измерения товара
    offer_pre_text = models.TextField(blank=True, null=True, verbose_name='Краткое описание')                                  # Текст описания товара
    offer_text = models.TextField(verbose_name='Полное описание')                                      # Текст описания товара
    offer_photo_alt = models.CharField(max_length=250, blank=True, verbose_name='Комментарий к изображению')
    offer_priority = models.BooleanField(default=False, verbose_name='Приоритетный товар')
    offer_urt_to_rubric = models.URLField(blank=True, verbose_name='Ссылка на рубрику')
    offer_characteristics = models.TextField(blank=True, verbose_name='Характеристики')
    offer_availability = models.ForeignKey(Availability, verbose_name='Наличие')
    offer_article = models.CharField(max_length=50, blank=True, verbose_name='Артикул')
    offer_id_on_site = models.IntegerField(blank=True, verbose_name='ID товара на сайте www.pulscen.ru')
    offer_code = models.CharField(max_length=50, blank=True, verbose_name='Код товара в вашем каталоге')
    offer_publish = models.ForeignKey(Publish, verbose_name='Публикуемость')
    offer_url = models.CharField(max_length=250, verbose_name='Ссылка на товар на нашем сайте')                         # Ссылка на товар на нашем сайте
    offer_photo = models.ImageField(blank=True, null=True, verbose_name='Фото на страницу')                          # Фото на страницу ( если нету ссылки на фото)
    offer_tag = models.ForeignKey(Tags, blank=True, verbose_name='Группа 1 уровня')                      # Ссылка на категорию
    offer_subtags = models.ManyToManyField(Subtags, blank=True, verbose_name='Группа 2 уровня')          # Ссылка на категорию

    @property
    def get_main_image(self):
        if self.images.filter(main=True):
            return self.images.filter(main=True).first()
        elif self.images.all():
            return self.images.first()
        elif self.offer_photo:
            return self.offer_photo

        return False

    @models.permalink
    def get_admin_url(self):
        return "admin:%s_%s_change" % (self._meta.app_label, self._meta.model_name), (self.id, )

# Банер на главной
class MainBaner(models.Model):

    def __str__(self):
        return self.baner_text

    class Meta:
        verbose_name = 'Банер на главной'
        verbose_name_plural = 'Банер на главной'

    baner_text = models.CharField(max_length=80)   # Текст на банере
    baner_img = models.ImageField(blank=True)      # Картинка банера
    baner_url = models.CharField(max_length=250)


class FBlocks(models.Model):
    def __str__(self):
        return self.fb_title

    class Meta:
        verbose_name = 'Блоки под слайдером'
        verbose_name_plural = 'Блоки под слайдером'

    fb_title = models.CharField(max_length=80)  # Текст на банере
    fb_text = models.TextField()                # Текст на банере
    fb_url = models.CharField(max_length=250)


class LBlocks(models.Model):
    def __str__(self):
        return self.lb_title

    class Meta:
        verbose_name = 'Список под 4 блоками'
        verbose_name_plural = 'Список под 4 блоками'

    lb_title = models.CharField(max_length=80)  # Текст на банере
    lb_text = models.TextField()                # Текст на банере
    lb_icon = models.CharField(max_length=80)
    lb_link = models.CharField(max_length=250, blank=True)


class AboutCompany(models.Model):
    def __str__(self):
        return self.ac_title

    class Meta:
        verbose_name = 'Про компанию на главной'
        verbose_name_plural = 'Про компанию на главной'

    ac_title = models.CharField(max_length=80)  # Текст на банере
    ac_text = models.TextField()  # Текст на банере


class TopOffers(models.Model):
    def __str__(self):
        return self.to_title

    class Meta:
        verbose_name = 'Самые продаваемые товары'
        verbose_name_plural = 'Самые продаваемые товары'

    to_title = models.CharField(max_length=80)  # Текст на банере
    to_link = models.CharField(max_length=250)


class Support(models.Model):
    def __str__(self):
        return self.sup_title

    class Meta:
        verbose_name = 'Служба поддержки на главной'
        verbose_name_plural = 'Служба поддержки на главной'

    sup_title = models.CharField(max_length=80)
    sup_time = models.CharField(max_length=80)
    sup_slogan = models.CharField(max_length=80)
    sup_phone = models.CharField(max_length=80)


class Personal(models.Model):
    def __str__(self):
        return self.p_name

    class Meta:
        verbose_name = 'Персонал на главной'
        verbose_name_plural = 'Персонал на главной'

    p_name = models.CharField(max_length=80)
    p_doljnost = models.CharField(max_length=80)
    p_photo = models.ImageField()


class HeaderPhoto(models.Model):
    def __str__(self):
        return self.hp_name

    class Meta:
        verbose_name = 'Картинка в шапку на главной'
        verbose_name_plural = 'Картинка в шапку на главной'

    hp_name= models.CharField(max_length=80)
    hp_photo = models.ImageField()


class Footer(models.Model):
    def __str__(self):
        return self.f_adres

    class Meta:
        verbose_name = 'Элементы подвала'
        verbose_name_plural = 'Элементы подвала'

    f_adres = models.CharField(max_length=80)
    f_skype = models.CharField(max_length=80)
    f_mob_phone = models.CharField(max_length=80)
    f_rob_phone = models.CharField(max_length=80)
    f_facebook_link = models.CharField(max_length=80)
    f_twitter_link = models.CharField(max_length=80)


class Reviews(models.Model):

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    name = models.CharField(blank=True, null=True, max_length=150)
    email = models.CharField(blank=True,null=True, max_length=100)
    text = models.TextField()
    publish = models.BooleanField(default=False, blank=True)
    date = models.DateTimeField(auto_now_add=True)