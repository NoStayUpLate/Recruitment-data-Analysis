from pymysql import *

class HandleDatabases():
    def __init__(self):
        # 链接数据库
        self.conn = connect(host = 'localhost',
                       port = 3306,
                       user = 'root',
                       password = '123456',
                       database = 'lagou',
                       charset = 'utf8')
     # 单条件查询
    def SingleConditionQuery(self,Condition,Label):
        cursors = self.conn.cursor()
        Cond = Label + " = " + Condition
        cursors.execute("select * from lagou where" + Cond)
        result = cursors.fetchall()
        cursors.close()
        return result

    # 多条件查询
    def MultipleConditionQuery(self,Condition,Label):
        cursors = self.conn.cursor()
        sql = self.PassSql(Condition,Label)
        cursors.execute(sql)
        result = cursors.fetchall()
        cursors.close()
        return result

    # 传递多查询语句
    def PassSql(self,Condition,Label):
        """
        1.传递 cond 字典，用来组成sql语句
        :returns sql
        """
        item = []
        SQL = "select * from lagou"
        Flag =True
        for i,j in zip(Label,Condition):
            Sql = i + " = " + j
            item.append(Sql)
        for i in item:
            if Flag == True:
                sql = " where " + i
                Flag = False
            else:
                sql = sql + " and " + i
        sql = SQL + sql
        return sql


if __name__ == '__main__':
    Database = HandleDatabases()