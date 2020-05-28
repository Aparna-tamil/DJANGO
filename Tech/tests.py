from django.test import TestCase
import datetime
from django.utils import timezone
from .models import all

class allModelTests(TestCase):
    def test_was_published_recently_with_future_course(self):
        time=timezone.now()+datetime.timedelta(days=30)
        future_question=all(startedfrom=time)
        self.assertIs(future_question.was_published_recently(), False)
    def test_was_published_recently_with_old_course(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_course=all(startedfrom=time)
        self.assertIs((old_course.was_publised_recently(), False))
    def test_was_published_recently_with_recent_course(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        old_course = all(startedfrom=time)
        self.assertIs((old_course.was_publised_recently(), True))