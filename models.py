from django.db import models
# from django.forms import TableForm
# Create your models here.


class Table(models.Model):
    id = models.ForeignKey
    month = models.DateField()
    to = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    office = models.IntegerField()
    financial_group = models.CharField(max_length=20)
    financial = models.CharField(max_length=20)
    value = models.IntegerField()

    # def __str__(self):
    #     return self.section_id


#     class Meta:
#         db_table = "Table"

    # Table_id = models.ForeignKey
    # Table_month = models.DateField()
    # Table_to = models.CharField(max_length=20)
    # Table_city = models.CharField(max_length=20)
    # Table_office = models.IntegerField()
    # Table_financial_group = models.CharField(max_length=20)
    # Table_financial = models.CharField(max_length=20)
    # Table_value = models.IntegerField()
