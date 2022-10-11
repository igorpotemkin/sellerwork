#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
'''python manage.py runserver 192.168.88.189:8000'''
'''python manage.py runserver ws002.smbg.local:8000'''
'''python manage.py runserver 10.10.40.18:8000'''
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seller_work.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
