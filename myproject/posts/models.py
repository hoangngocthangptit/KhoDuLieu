from __future__ import unicode_literals

from django.db import models
from django.urls import reverse


class Post(models.Model):
  name = models.CharField(max_length=224, null=False, blank=False)
  content = models.TextField(max_length=254, null=False, blank=False)
  timestamp = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

class DepositorMst(models.Model):
  class Meta:
    db_table = 'depositor_mst'
  cd = models.CharField(max_length=10, primary_key=True)
  name = models.CharField(max_length=100, null=True)
  is_delete = models.BooleanField(default=False)

class OfficeMst(models.Model):
  class Meta:
    db_table = 'office_mst'
  cd = models.CharField(max_length=10, primary_key=True)
  name = models.CharField(max_length=100, null=True)
  is_delete = models.BooleanField(default=False)

class PaymentConditionRegistration(models.Model):
  class Meta:
    db_table = 'payment_condition_registration'
  depositor_cd = models.ForeignKey(DepositorMst, on_delete=models.DO_NOTHING)
  office_cd = models.ForeignKey(OfficeMst, on_delete=models.DO_NOTHING)
  contact_no_show = models.BooleanField(null=True)
  customer_department_show = models.BooleanField(null=True)
  mark_show = models.BooleanField(null=True)
  created_dt = models.DateTimeField(null=True)
  updated_dt = models.DateTimeField(null=True)
  created_user_id = models.IntegerField(null=True)
  updated_user_id = models.IntegerField(null=True)
  is_delete = models.BooleanField(default=False)



  def __unicode__(self):
    return self.content