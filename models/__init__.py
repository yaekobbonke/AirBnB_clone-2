#!/usr/bin/python3

if HBNB_TYPE_STORAGE == db:
    """This module instantiates an object of class DBStorage"""
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    """This module instantiates an object of class FileStorage"""
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
