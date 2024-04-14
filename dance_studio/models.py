import json
import logging

from django.conf import settings
from django.db import models
from django.db.models import JSONField

from transliterate.utils import _
from django.db.models import signals

logger = logging.getLogger(__name__)


class Company(models.Model):
    name = models.CharField(unique=True, max_length=1024, verbose_name=_('Name'))
    address = models.CharField(unique=True, max_length=1024, verbose_name=_('Address'))
    created_at = models.DateTimeField(verbose_name=_('Created date'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Changed date'), auto_now=True)
    description = models.CharField(max_length=1024, verbose_name=_('Description'), blank=True, null=True)


class Courses(models.Model):
    name = models.CharField(unique=True, max_length=1024, verbose_name=_('Name'))
    created_at = models.DateTimeField(verbose_name=_('Created date'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Changed date'), auto_now=True)
    description = models.CharField(max_length=1024, verbose_name=_('Description'), blank=True, null=True)
    fk_company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name='Company', blank=True, null=True
    )


class Costs(models.Model):
    name = models.CharField(unique=True, max_length=1024, verbose_name=_('Name'))
    created_at = models.DateTimeField(verbose_name=_('Created date'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Changed date'), auto_now=True)
    cost_date = models.DateTimeField(verbose_name=_('Changed date'), auto_now=True)
    cost = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=1024, verbose_name=_('Description'), blank=True, null=True)
    fk_company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name='Company', blank=True, null=True
    )