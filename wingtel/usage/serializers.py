from rest_framework import serializers
from wingtel.usage.models import DataUsageRecord, VoiceUsageRecord


class DataUsageRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataUsageRecord
        fields = '__all__'


class VoiceUsageRecord(serializers.ModelSerializer):

    class Meta:
        model = VoiceUsageRecord
        fields = '__all__'


class SubscriptionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    type = serializers.CharField(source='get_type')
    exceeded_by = serializers.DecimalField(max_digits=1000, decimal_places=2)

    def get_type(self, obj):
        if type(obj) == DataUsageRecord:
            return "Data"
        else:
            return "Voice"
