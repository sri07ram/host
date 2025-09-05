from rest_framework import serializers
from .models import Hospital

class HospitalSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    patient_name = serializers.CharField(max_length=100)
    patient_sick = serializers.CharField(max_length=100)
    a_time = serializers.CharField(max_length=100)
    doctor_name = serializers.CharField(max_length=100)
    patient_loc = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Hospital.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.patient_name = validated_data.get('patient name', instance.patient_name)
        instance.a_time = validated_data.get('Appoinment ', instance.a_time)
        instance.save()
        return instance
