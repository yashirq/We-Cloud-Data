import json
import pathlib

import auth
import sql_string


class Postgres_Database:

    def __init__(self):
        self.new_empty_surveys_path = '%s/output/04new_empty_surveys.json' % pathlib.Path(
            __file__).parent.resolve()

    def create_table(self, table_name):
        # Drop table if already exists.
        auth.cursor.execute(
            f'DROP TABLE IF EXISTS {table_name} CASCADE;')
        # Creating table as per requirement
        auth.cursor.execute(sql_string.create_table_syntax[table_name])
        # Need to create unique index for the responses tables
        for i in range(len(sql_string.tables2)):
            if i+1 > 6 and sql_string.tables2[i] == table_name:
                unique_index_columns = sql_string.primary_keys[table_name]
                auth.cursor.execute(
                    f'''CREATE UNIQUE INDEX ui_{table_name} on {table_name} ({unique_index_columns});''')
        print(f'{table_name} table created successfully........')

    def insert_to_table(self, file_path, table_name):
        
        with open(file_path) as f:
            data = f.read()
            if not data:
                print(f'No new data for inserting to {table_name}')
                return
            else: 
                print(f'Inserting data into {table_name}')
            for line in f:
                record = json.loads(line)
                columns = list(record.keys())
                values = list(record.values())
                values = [None if v == '' else v for v in values]
                # Change single quote to double quote to
                # fit the postgresqlsyntax
                primary_key = sql_string.primary_keys[table_name].replace(
                    '\'', '\"')
                insert_string = f'''INSERT INTO {table_name}\n\t({','.join(columns)})\nVALUES\n\t({','.join(['%s'] * len(values))})\nON CONFLICT ({primary_key})\nDO NOTHING'''
                auth.cursor.execute(insert_string, values)
        print(f'Finish inserting data into {table_name}')

    def create_tables(self):
        for index in sql_string.tables2:
            table_name = sql_string.tables2[index]
            self.create_table(table_name)

    def insert_to_tables(self):
        for item in sql_string.insert_syntax:
            self.insert_to_table(item[0], item[1])
