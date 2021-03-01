# sql_database_app.py

import sqlite3
import csv



def csv_to_sqldb_migration(p_csv_path, p_connection, p_table_name):

    with open(p_csv_path, "r") as file:
        no_records = 0
        print(file)
        for row in file:
            if row.split(",")[0] == "":
                pass
            else:
                print(row.split(","))
                p_connection.cursor().execute("INSERT INTO BaseTable VALUES (?,?,?,?,?,?)", row.split(","))
                p_connection.commit()
                no_records += 1

    p_connection.close()

    return f'{no_records} Records Transfered'

def create_base_table(p_connection):

    sql = """
    CREATE TABLE BaseTable (
        id INTEGER,
        melyseg REAL,
        csucs_ellenallas REAL,
        palast_surlodas REAL,
        porus_viznyomas REAL,
        surlodasi_aranyszam REAL,
        primary key(id)
        )"""

    p_connection.cursor().execute(sql)

    return"BaseTable has been created"


csv_path = "CPTu_1_base.csv"
connection = sqlite3.connect("CPTU_1.db")
# create_base_table(connection)
csv_to_sqldb_migration(csv_path, connection, "BaseTable")
