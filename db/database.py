from distutils.debug import DEBUG

class Config:
    SECRET_KEY="a_a_a_"

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER='root'
    MYSQL_PASSWORD=''
    MYSQL_DB='db_Freemoney'

config={'development':DevelopmentConfig}

class Exe():
    
    @classmethod
    def sentencia_all(self,mysql,sent):
        sql=mysql.connection.cursor()
        sql.execute(sent)
        res=sql.fetchall()
        sql.close()
        print(res)
        return res

    @classmethod
    def sentencia_one(self,mysql,sent):
        sql=mysql.connection.cursor()
        sql.execute(sent)
        res=sql.fetchone()
        sql.close()
        print(res)
        return res

    @classmethod
    def sentencia_commit(self,mysql,sent):
        sql=mysql.connection.cursor()
        sql.execute(sent)
        mysql.connection.commit()            