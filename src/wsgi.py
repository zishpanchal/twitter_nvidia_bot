# filepath: wsgi.py
import os
import sys

# Add your project directory to the sys.path
path = os.path.expanduser('~/home/zishpanchal/')  # Replace with your actual project path
if path not in sys.path:
    sys.path.append(path)

# You don't need to import your app here for a scheduled task.
# This file is just needed for PythonAnywhere to recognize your project.