import os
import sys
import json
import math
import sqlite3
from datetime import datetime, timedelta

def main():
    con = sqlite3.connect(os.path.join(sys.path[0], 'bookstore.db'))
    con.execute(
        '''CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isbn TEXT NOT NULL,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            pages INTEGER NOT NULL,
            year TEXT NOT NULL,
            status TEXT DEFAULT "AVAILABLE",
            return_date DATE DEFAULT NULL
        );'''
    )


if __name__ == "__main__":
    main()