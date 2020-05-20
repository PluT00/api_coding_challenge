from django.test import TestCase

from wingtel.att_subscriptions.models import ATTSubscription
from wingtel.sprint_subscriptions.models import SprintSubscription
from wingtel.usage.models import DataUsageRecord, VoiceUsageRecord


class DataUsageRecordTestCase(TestCase):

    def setUp(self):
        self.data_usage_record = DataUsageRecord.objects.create(
            kilobytes_used=10
        )

# Test att_subscription_id field.
    def test_att_subsctiption_id_related_model(self):
        related_model = self.data_usage_record._meta.get_field(
            'att_subscription_id'
        ).related_model
        self.assertEqual(related_model, ATTSubscription)

    def test_att_subsctiption_id_null(self):
        null = self.data_usage_record._meta.get_field(
            'att_subscription_id'
        ).null
        self.assertEqual(null, True)

# Test sprint_subscription_id field.
    def test_sprint_subscription_id_related_model(self):
        related_model = self.data_usage_record._meta.get_field(
            'sprint_subscription_id'
        ).related_model
        self.assertEqual(related_model, SprintSubscription)

    def test_sprint_subscription_id_null(self):
        null = self.data_usage_record._meta.get_field(
            'sprint_subscription_id'
        ).null
        self.assertEqual(null, True)

# Test price field.
    def test_price_decimal_places(self):
        decimal_places = self.data_usage_record._meta.get_field(
            'price'
        ).decimal_places
        self.assertEqual(decimal_places, 2)

    def test_price_max_digits(self):
        max_digits = self.data_usage_record._meta.get_field(
            'price'
        ).max_digits
        self.assertEqual(max_digits, 5)

    def test_price_default(self):
        default = self.data_usage_record._meta.get_field(
            'price'
        ).default
        self.assertEqual(default, 0)

# Test usage_date field.
    def test_usage_date_null(self):
        null = self.data_usage_record._meta.get_field(
            'usage_date'
        ).null
        self.assertEqual(null, True)

# Test kilobytes_used field.
    def test_kilobytes_used_null(self):
        null = self.data_usage_record._meta.get_field(
            'kilobytes_used'
        ).null
        self.assertEqual(null, False)

# Test get_type method.
    def test_get_type(self):
        type = self.data_usage_record.get_type()
        self.assertEqual(type, "Data")


class VoiceUsageRecordTestCase(TestCase):

    def setUp(self):
        self.voice_usage_record = VoiceUsageRecord.objects.create(
            seconds_used = 10
        )

# Test att_subscription_id field.
    def test_att_subsctiption_id_related_model(self):
        related_model = self.voice_usage_record._meta.get_field(
            'att_subscription_id'
        ).related_model
        self.assertEqual(related_model, ATTSubscription)

    def test_att_subsctiption_id_null(self):
        null = self.voice_usage_record._meta.get_field(
            'att_subscription_id'
        ).null
        self.assertEqual(null, True)

# Test sprint_subscriptions_id field.
    def test_sprint_subscription_id_related_model(self):
        related_model = self.voice_usage_record._meta.get_field(
            'sprint_subscription_id'
        ).related_model
        self.assertEqual(related_model, SprintSubscription)

    def test_sprint_subscription_id_null(self):
        null = self.voice_usage_record._meta.get_field(
            'sprint_subscription_id'
        ).null
        self.assertEqual(null, True)

# Test price field.
    def test_price_decimal_places(self):
        decimal_places = self.voice_usage_record._meta.get_field(
            'price'
        ).decimal_places
        self.assertEqual(decimal_places, 2)

    def test_price_max_digits(self):
        max_digits = self.voice_usage_record._meta.get_field(
            'price'
        ).max_digits
        self.assertEqual(max_digits, 5)

    def test_price_default(self):
        default = self.voice_usage_record._meta.get_field(
            'price'
        ).default
        self.assertEqual(default, 0)

# Test usage_date field.
    def test_usage_date_null(self):
        null = self.voice_usage_record._meta.get_field(
            'usage_date'
        ).null
        self.assertEqual(null, True)

# Test seconds_used field.
    def test_seconds_used_null(self):
        null = self.voice_usage_record._meta.get_field(
            'seconds_used'
        ).null
        self.assertEqual(null, False)

# Test get_type method.
    def test_get_type(self):
        type = self.voice_usage_record.get_type()
        self.assertEqual(type, "Voice")
