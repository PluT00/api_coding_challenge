from itertools import chain

from rest_framework import generics
from wingtel.usage.serializers import SubscriptionSerializer
from wingtel.usage.models import DataUsageRecord, VoiceUsageRecord


class ExceededSubsListAPIView(generics.ListAPIView):

    def get_queryset(self):
        exceeding = self.request.query_params.get('exceeding')

        if exceeding != None:
            data = DataUsageRecord.objects.filter(price__gt=price)
            voice = VoiceUsageRecord.objects.filter(price__gt=price)

            queryset = list(chain(data, voice))

            return queryset
        return list(chain(
            DataUsageRecord.objects.all(), VoiceUsageRecord.objects.all()
            ))

    serializer_class = SubscriptionSerializer
