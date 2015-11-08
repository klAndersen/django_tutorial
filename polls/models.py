import datetime

from django.db import models
from django.utils import timezone

# each class is a sub-class of 'django.db.models.Model'

# each field is represented by the Field class (e.g. Character (CharField), DateTime (DateTimeField))
# the field tells Django in what format the data should be stored and what data it contains

# the field name (e.g. question_text, pub_date, etc.) is the name of the field, and
# this is used as column name in the database. This is known as a machine-readable name.
# One could also add the class name in front of the field name (e.g. Question.pub_date)
# to create a human-readable name.


class Question(models.Model):
    # CharField requires the 'max_length' parameter
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # basically Pythons version of toString()
    # prints out the value instead of [<Question: Question object>]
    # when calling 'Question.objects.all()'
    # -------------------------------------
    # In Python2, use __unicode__
    # In Python3, use __str__()
    def __unicode__(self):
        return self.question_text

    # Custom method for printing recently published questions
    # Returns True if less then 1 day old
    def was_published_recently(self):
        # v1.0: Returns True if less then 1 day old (and if created in the future)
        # return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        # v2.0: Returns true only for questions that are created today
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # added attributes (part 2 of tutorial)
    was_published_recently.admin_order_field = 'pub_date'  # sorting by date
    was_published_recently.boolean = True   # default sort is based on the recent ones
    was_published_recently.short_description = 'Published recently?'  # description


class Choice(models.Model):
    # foreign key telling Django that each Choice is related to a single Question
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    # set a default value (here: 0)
    votes = models.IntegerField(default=0)

    # See comment above
    def __unicode__(self):
        return self.choice_text
