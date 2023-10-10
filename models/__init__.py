#!/usr/bin/python3
"""Create a unique FileStorage instance for our application"""
from models.engine.file_storage import FileStorage


# Create a unique FileStorage instance
storage = FileStorage()

# Call the reload method on the storage instance
storage.reload()
