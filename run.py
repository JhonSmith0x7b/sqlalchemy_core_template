
from sediment import mysql_connector


def main():
    mc = mysql_connector.MysqlConnector(
        '127.0.0.1',
        3306,
        'root',
        '123456',
        'test'
    )
    test_table = mc.get_test_table()
    test_table.replace_into(mc.get_connect(), 1, 'JohnSmith')
    test_record = test_table.select_via_id(mc.get_connect(), 1)
    assert test_record.name == 'JohnSmith'


if __name__ == '__main__':
    main()
