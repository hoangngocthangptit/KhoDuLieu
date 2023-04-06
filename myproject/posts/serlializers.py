from rest_framework import serializers

from django.db.models import fields
from .models import DepositorMst,OfficeMst,PaymentConditionRegistration

class PaymentConditionRegistrationSerializer(serializers.ModelSerializer):  # create class to serializer user model
    depositor_cd = serializers.PrimaryKeyRelatedField(queryset=DepositorMst.objects.all())
    office_cd = serializers.PrimaryKeyRelatedField(queryset=OfficeMst.objects.all())
    class Meta:
        model =PaymentConditionRegistration
        # fields = ('contact_no_show','customer_department_show','mark_showe','created_dt','updated_dt','created_user_id','updated_user_id','is_delete')
        fields ='__all__'

class OfficeMstSerializer(serializers.ModelSerializer):
    # creator =serializers.ReadOnlyField(
    class Meta:
        model =OfficeMst
        fields = ('cd','name','is_delete')
class DepositorMstSerializer(serializers.ModelSerializer):
    class Meta:
        model =OfficeMst
        fields = ('cd','name','is_delete')
