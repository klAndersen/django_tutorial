#!/usr/bin/env python

# This project is based on tutorial found at: https://docs.djangoproject.com/en/1.8/intro/tutorial01/#

# A command-line utility that lets you interact with this Django project in various ways.
# See: https://docs.djangoproject.com/en/1.8/ref/django-admin/
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
