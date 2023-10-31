from django.db import models
from django.contrib.auth.models import User


class BaseModel(models.Model):
    created_on = models.DateTimeField(
        auto_now_add=True,
        help_text='Oluşturulma'
    )
    created_by = models.ForeignKey(
        User,
        null=True,
        help_text='Oluşturan',
        on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_cby',
        editable=False
    )

    modified_on = models.DateTimeField(
        auto_now=True,
        help_text='Güncelleme'
    )
    modified_by = models.ForeignKey(
        User,
        null=True,
        help_text='Güncelleyen',
        on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_mby',
        editable=False
    )
    is_active = models.BooleanField(null=False, blank=False, default=True)

    class Meta:
        abstract = True
        
