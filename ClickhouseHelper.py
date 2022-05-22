from clickhouse_driver import Client
from Config import config


class ClickhouseHelper:
    def __init__(self):
        self.client = Client(**config['CK']['connect'])

    def create_table(self):
        sql = "CREATE TABLE retention_test(uid Int32, action String, date Date) ENGINE = Memory;"
        self.client.execute(sql)

    def delete_table(self):
        sql = "drop table retention_test"
        self.client.execute(sql)

    def window_funnel(self, column_name, actions):
        sql_template = """
        with tmp as (
          select
            level,
            count(uid) as res
          from
            (
              select
                uid,
                windowFunnel(60000000000, 'strict_order')(date place_holder)
                 as level
              from
                retention_test
              group by
                uid
              order by
                uid
            ) as t
          group by
            t.level
        )
        select
          tmp.level,
          SUM(tmp.res) OVER(
            ORDER BY
              tmp.level ROWS BETWEEN CURRENT ROW
              AND UNBOUNDED FOLLOWING
          ) AS retention
        from
          tmp
        order by
          tmp.level;
        """
        params = ''
        for action in actions:
            params += f", {column_name} = '{action}'"
        print(self.client.execute(sql_template.replace('place_holder', params)))





