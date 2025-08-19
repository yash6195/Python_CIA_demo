#!/usr/bin/env python
import os, sys
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
if sys.argv[1] == "runserver":
    import subprocess
    subprocess.run(["python", "manage.py", "migrate"])
if __name__ == '__main__':
    main()
