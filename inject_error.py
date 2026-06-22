# Run this script to simulate a live Django crash for testing.
# It replaces the standard home view parameter to raise a NameError on load.

import os

views_path = '/var/www/hamrahvision/core/views.py'

if not os.path.exists(views_path):
    print(f"Error: {views_path} not found. Please edit the path in this script.")
    exit(1)

with open(views_path, 'r') as f:
    content = f.read()

old_def = "def home(request):\n    return render(request, 'core/home.html')"
new_def = "def home(reqst):\n    return render(request, 'core/home.html')"

if old_def in content:
    content = content.replace(old_def, new_def)
    with open(views_path, 'w') as f:
        f.write(content)
    print("NameError successfully injected in views.py!")
else:
    print("Typo is already injected or views.py was customized.")
