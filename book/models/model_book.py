from django.db import models

from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField


class Book(models.Model):
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    title = models.CharField(max_length=350)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    cover = FilerImageField(related_name="cover_books", on_delete=models.CASCADE)
    file = FilerFileField(related_name="file_books", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
