#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Add the backend directory to the Python path
    backend_dir = os.path.dirname(os.path.abspath(__file__))
    if backend_dir not in sys.path:
        sys.path.insert(0, backend_dir)
    
    # Also add ZyraMart directory so apps can use short names like "users", "products"
    zyramart_dir = os.path.join(backend_dir, "ZyraMart")
    if zyramart_dir not in sys.path:
        sys.path.insert(0, zyramart_dir)
    
    # Use "ZyraMart.settings" because ZyraMart dir is in sys.path
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
