"""
See part 2 of Tutorial 1: https://docs.djangoproject.com/en/1.8/intro/tutorial02/
The v1.0-x.y is self-commentary notes describing larger changes made to the
original concept from the start to the end of the tutorial to have something to
look back at.
"""


from django.contrib import admin

from .models import Choice, Question

# ChoiceInLine class changes
# v1.0: 'admin.StackedInline'
# v2.0: Because 'admin.StackedInLine' takes a lot of screen space,
# make it into 'admin.TabularInline' to get tabular format


class ChoiceInline(admin.TabularInline):
    # This tells Django:
    # "Choice objects are edited on the Question admin page.
    # By default, provide enough fields for 3 choices."
    model = Choice  # related/connected model
    extra = 3   # number of extra fields to add for the given model


class QuestionAdmin(admin.ModelAdmin):
    # anytime you want to alter a field/model,
    # create a model object of what you want
    # to alter/change

    # v1.0: fields (see below)
    # sets the publication date field before the question field
    # fields = ['pub_date', 'question_text']

    # v2.0: fieldsets (see below)
    # the first element is the title
    # the second is the fields
    # v2.1: Added <html> 'collapse' class to pub_date
    # fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]

    # v3.0: added <inlines> for the class 'ChoiceInline'
    # inlines = [ChoiceInline]

    # v4.0:
    # changed to 'list_display' to display individual fields
    # added 'list_filter' to filter based on published date
    # added 'search_fields' to search on question text
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

# tell the admin site that the Question objects have an admin interface
admin.site.register(Question, QuestionAdmin)

# removed upon adding v3.0
# admin.site.register(Choice)
