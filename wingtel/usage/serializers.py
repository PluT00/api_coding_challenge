from rest_framework import serializers
from wingtel.usage.models import DataUsageRecord, VoiceUsageRecord


class DataUsageRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataUsageRecord
        fields = '__all__'


class VoiceUsageRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = VoiceUsageRecord
        fields = '__all__'


class SubscriptionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    type = serializers.CharField(source="get_type")
    exceeded_by = serializers.SerializerMethodField()

    def get_exceeded_by(self, obj):
        exceeding = self.context.get('exceeding')
        if exceeding != None:
            return float(obj.price) - float(exceeding)
        return None
