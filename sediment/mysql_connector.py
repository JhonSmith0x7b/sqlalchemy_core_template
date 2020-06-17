
import sqlalchemy
import requests
from sqlalchemy.engine import Engine
import logging
from sqlalchemy.engine.base import Connection
from sediment.mysql_tables.test_table import TestTable


class MysqlConnector(object):

    db_url = None
    _engine = None
    _metadata = None
    _test_table = None
    # add your table args

    def __init__(self, host, port, user, passwd, db):
        db_url = f'mysql+pymysql://{requests.utils.quote(user)}:{requests.utils.quote(passwd)}@{host}:{port}/{db}?charset=UTF8MB4'
        self.db_url = db_url
        self.__init_connect(self.db_url)

    def __init_connect(self, db_url):
        logging.debug("mysql connector db url: %s" % db_url)
        self._engine = sqlalchemy.create_engine(
            db_url
        )
        self._metadata = sqlalchemy.MetaData()
        self._test_table = TestTable().get_table(self._metadata)
        # add your table to link
        self._metadata.create_all(self._engine)

    # you can set a get method.
    def get_test_table(self) -> TestTable:
        return self._test_table

    def get_connect(self) -> Connection:
        try:
            conn = self._engine.connect()
            if not conn.closed:
                return conn
            else:
                raise Exception("conn is closed, will reconnect")
        except Exception as e:
            pass
        self.__init_connect(self.db_url)
        return self._engine.connect()

    def get_engine(self) -> Engine:
        return self._engine

