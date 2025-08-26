from flask import g as global_variables
from .config import SessionLocal

def get_db():
    if 'db' not in global_variables:
        global_variables.db = SessionLocal()
    return global_variables.db

def close_db(e=None):
    SessionLocal.remove()
