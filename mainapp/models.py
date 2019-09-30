from django.db import models


class Core(models.Model):
    """ Класс ядро - родитель всех классов-моделей """
    class Meta:
        ordering = ('-is_active', 'sort', 'name')
        verbose_name = 'Ядро'
        verbose_name_plural = 'Ядра'

    name = models.CharField(verbose_name='заголовок объекта', max_length=255, null=True)
    description = models.TextField(verbose_name='описание объекта', blank=True, null=True)
    sort = models.IntegerField(verbose_name='номер объекта для сортировки', default=0, blank=True, null=False)
    is_active = models.BooleanField(verbose_name='активен ли объект', default=True, db_index=True)
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='обновлен', auto_now=True)

    def __str__(self):
        return f'{self.name}' if self.name else ''

    def delete(self, **kwargs):  # или может *args
        if 'force' in kwargs:
            super().delete()
        else:
            self.is_active = False
            self.save()


class Picture(Core):
    """ Класс изображений - родитель для других моделей использующих изображения """
    class Meta:
        ordering = ('sort', 'updated')
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    image = models.ImageField(upload_to='images')
    related_obj = models.ForeignKey(Core, verbose_name='изображения', null=True, blank=True, related_name='images', on_delete=models.CASCADE)


class City(Core):
    """ Класс для выбора города приюта / пользователя """


class Shelter(Core):
    """ Класс-модель приюта/питомника """
    shelter_logo = models.ImageField(upload_to='shelter/images', verbose_name='логотип приюта', blank=True)
    shelter_city = models.ForeignKey(City, verbose_name='город', related_name='shelters', null=False, blank=False, on_delete=models.PROTECT)
    shelter_address = models.CharField(verbose_name='адрес', max_length=255, null=False, blank=False, unique=True)
    shelter_phone = models.CharField(verbose_name='телефон', max_length=17, null=False, blank=False, unique=True)
    shelter_email = models.EmailField(verbose_name='эл.почта', null=False, blank=False, unique=True)


class Donate(Core):
    """ Класс для финансовой помощи - Сбер, ЯндексДеньги, PayPal... """
    account = models.ForeignKey(Shelter, verbose_name='реквизиты счетов', blank=True, related_name='accounts', on_delete=models.PROTECT)


class Social(Core):
    """ Класс ссылок на соц.сети и мессенджеры """
    link = models.URLField(verbose_name='ссылка на соц.сеть', null=True, blank=True, unique=True)
    obj = models.ForeignKey(Shelter, related_name='links', on_delete=models.PROTECT)


class Category(Core):
    """Класс описывающий вид животного"""


class Breed(Core):
    """Класс описывающий породу животного"""


class PetGender(Core):
    """Класс описывающий пол животного"""


class PetSize(Core):
    """Класс описывающий размеры животного"""


class PetWool(Core):
    """Класс описывающий длину шерсти животного"""


class PetColor(Core):
    """Класс описывающий цвет животного"""


class PetCharacter(Core):
    """Класс описывающий характер животного"""


class Pet(Core):
    """Класс описывающий животного"""
    HELP = 'SOS'
    SICK = 'SCK'
    READY = 'RDY'
    HOME = 'HME'

    STATUS_CHOICES = (
        (HELP, 'Нужна помощь'),
        (SICK, 'На лечении'),
        (READY, 'Можно забрать'),
        (HOME, 'Уже дома'),
    )

    pet_shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE, related_name='pets', blank=False, null=False)
    pet_status = models.CharField(verbose_name='статус', max_length=3, choices=STATUS_CHOICES, default=SICK)
    pet_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pet_breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    pet_gender = models.ForeignKey(PetGender, on_delete=models.CASCADE)
    pet_size = models.ForeignKey(PetSize, on_delete=models.CASCADE)
    pet_wool_length = models.ForeignKey(PetWool, on_delete=models.CASCADE)
    pet_color = models.ForeignKey(PetColor, on_delete=models.CASCADE)
    pet_character = models.ForeignKey(PetCharacter, on_delete=models.CASCADE)
    age = models.PositiveIntegerField(verbose_name='возраст (лет)', default=0)
    month = models.PositiveIntegerField(verbose_name='возраст (мес)', default=0)

    # Убираем из каталога неактивные объявления
    @staticmethod
    def get_items():
        return Pet.objects.filter(is_active=True).order_by('pet_category', 'name')
