from django.db import models
from private_storage.fields import PrivateFileField


class Category(models.Model):
    symbol = models.CharField(max_length=64,
                              unique=True)
    class Meta:
        ordering = ["symbol",]
        verbose_name = "kategoria"
        verbose_name_plural = "kategorie"
    
    def __str__(self):
        return self.symbol


class Notice(models.Model):
    number = models.CharField(max_length=16,
                              unique=True,
                              verbose_name="Numer",
                              help_text="max 16 znaków")
    description = models.TextField(default="",
                                   blank=True,
                                   verbose_name="opis")
    date = models.DateTimeField(verbose_name="data")
    comment = models.TextField(default="",
                               blank=True,
                               verbose_name="komentarz")
    NEW = "n"
    ACCEPTED = "a"
    DONE = "d"
    REJECTED = "r"
    STATUSES = [(NEW, "nowy"),
                (ACCEPTED, "przyjęty"),
                (DONE, "wykonany"),
                (REJECTED, "odrzucony")]
    status = models.CharField(max_length=1,
                              choices=STATUSES,
                              default=NEW)
    category = models.ForeignKey(Category,
                                 null=True,
                                 blank=True,
                                 on_delete=models.PROTECT,
                                 verbose_name="kategoria",
                                 related_name="notices")
    image = models.ImageField(upload_to="notice/",
                              null=True,
                              blank=True,
                              default="",
                              verbose_name="obraz")
    
    file = PrivateFileField(upload_to= 'notice/',
                            null=True,
                            blank=True,
                            default="",
                            content_types =['application/pdf'],
                            max_file_size = 2*1024*1024,
                            verbose_name = 'plik')
    
    class Meta:
        ordering = ["-date",
                    "number"]
        verbose_name = "zgłoszenie"
        verbose_name_plural = "zgłoszenia"

    def __str__(self):
        return self.number
    
    def status_name(self):
        for name in self.STATUSES:
            if self.status == name[0]:
                return name[1]
        return "?"
    
    def status_color(self):
        if self.status == self.NEW:
            return "text-danger"
        elif self.status == self.ACCEPTED:
            return "text-primary"
        elif self.status == self.DONE:
            return "text-success"
        elif self.status == self.REJECTED:
            return "text-secondary"
        return ""
