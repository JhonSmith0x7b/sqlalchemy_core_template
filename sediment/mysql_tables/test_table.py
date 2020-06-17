import sqlalchemy
from sediment.mysql_tables.base_table import BaseTable
from models.test_model import TestModel
from sqlalchemy.engine.base import Connection


class TestTable(BaseTable):

    def __init__(self):
        super().__init__("sa_test")

    def _init_columns(self):
        self.columns = [
            sqlalchemy.Column('id', sqlalchemy.Integer, primary_key=True, autoincrement=True),
            sqlalchemy.Column('name', sqlalchemy.String(255))
        ]

    def replace_into(self, __conn: Connection, id: int, name: str):
        sql = f"""
        replace into {self.table_name} (id, name)
        values (:id, :name)
        """
        stat = sqlalchemy.text(sql)
        __conn.execute(stat, locals())

    def select_via_id(self, __conn: Connection, id: int) -> TestModel:
        sql = f"""
        select * from {self.table_name}
        where id = :id
        """
        stat = sqlalchemy.text(sql)
        result = __conn.execute(stat, locals()).fetchone()
        if result is None:
            return None
        return TestModel(
            id=result[0],
            name=result[1]
        )


