import logging
import sqlalchemy


class BaseTable(object):
    table_name = None
    columns = []
    table = None

    def __init__(self, table_name):
        self.table_name = table_name
        self._init_columns()

    def get_table(self, metadata):
        self.table = sqlalchemy.Table(
            self.table_name, metadata, *self.columns
        )
        return self

    def _init_columns(self):
        raise Exception("no override init columns")
