# Run this script to manually recover the views.py file back to normal.

import os

views_path = '/var/www/hamrahvision/core/views.py'

if not os.path.exists(views_path):
    print(f"Error: {views_path} not found. Please edit the path in this script.")
    exit(1)

with open(views_path, 'r') as f:
    content = f.read()

old_def = "def home(request):\n    return render(request, 'core/home.html')"
new_def = "def home(reqst):\n    return render(request, 'core/home.html')"

if new_def in content:
    content = content.replace(new_def, old_def)
    with open(views_path, 'w') as f:
        f.write(content)
    print("Views.py code successfully restored!")
else:
    print("Code is already normal.")
