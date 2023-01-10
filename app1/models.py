from django.db import models
class Profession(models.Model):
    title = models.CharField('Title', max_length=50)
    description = models.TextField('description')
    habilities = models.TextField('habilities', default='SOMESTRING')
    Company = models.TextField('company', default='SOMESTRING')
    Salary = models.TextField('salary', default='SOMESTRING')
    region = models.TextField('regions', default='SOMESTRING')
    data = models.TextField('data', default='SOMESTRING')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Profession Info'
        verbose_name_plural = 'Profession'