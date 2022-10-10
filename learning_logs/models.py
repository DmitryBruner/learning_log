from django.db import models
class Topic(models.Model):
    """Тема, которую изучает пользователь"""
    text = models.CharField(max_length=200)
    date_added = models.Da
    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.text