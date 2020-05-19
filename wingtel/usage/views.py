from itertools import chain

from rest_framework import generics, viewsets
from wingtel.usage.serializers import (SubscriptionSerializer,
                                       DataUsageRecordSerializer,
                                       VoiceUsageRecordSerializer)
from wingtel.usage.models import DataUsageRecord, VoiceUsageRecord


class DataUsageRecordViewSet(viewsets.ModelViewSet):
    queryset = DataUsageRecord.objects.all()
    serializer_class = DataUsageRecordSerializer


class VoiceUsageRecordViewSet(viewsets.ModelViewSet):
    queryset = VoiceUsageRecord.objects.all()
    serializer_class = VoiceUsageRecordSerializer


class ExceededSubsListAPIView(generics.ListAPIView):

    def get_queryset(self):
        exceeding = self.request.query_params.get('exceeding')

        if exceeding != None:
            data = DataUsageRecord.objects.filter(price__gt=exceeding)
            voice = VoiceUsageRecord.objects.filter(price__gt=exceeding)

            queryset = list(chain(data, voice))

            return queryset
        return list(chain(
            DataUsageRecord.objects.all(), VoiceUsageRecord.objects.all()
            ))

    def get_serializer_context(self):
        return {'exceeding': self.request.query_params.get('exceeding')}

    serializer_class = SubscriptionSerializer
