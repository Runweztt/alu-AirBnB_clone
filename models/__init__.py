#!/usr/bin/python3
"""Initialize the models package and shared file storage instance."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
