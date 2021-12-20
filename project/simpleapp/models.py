from django.db import models

# Создаём модель новости
class News(models.Model):
    title = models.CharField(
        max_length=50,
        unique=True,
    )
    text = models.TextField()

    dateCreation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title.title()}. Дата публикации: {self.dateCreation.strftime("%d %B, %Y")}. {self.text[:50]}...'
