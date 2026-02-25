#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Add the project parent directory to the Python path
    # This allows Python to find apps like 'users', 'products', etc.
    # which are in the sibling directories of 'ZyraMart'
    project_parent = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if project_parent not in sys.path:
        sys.path.insert(0, project_parent)
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ZyraMart.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
