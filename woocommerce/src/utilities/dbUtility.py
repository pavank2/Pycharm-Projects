import pymysql
from src.utilities.credentialsUtility import CredentialsUtility

class DBUtility(object):

    def __init__(self):
        #credsHelper = CredentialsUtility()
        # self.creds = creds_helper.get_db_credentials()
        pass

    def create_connection(self):
        connection = pymysql.connect(host='localhost',user='root',password='root',port=8889)

        return connection

    def execute_select(self,sql):
        conn = self.create_connection()
        try:
            cur = conn.cursor(pymysql.cursors.DictCursor) # Parameter to get cursor as a dictionary
            cur.execute(sql)
            rs_dict = cur.fetchall()
            cur.close()
        except Exception as e:
            raise Exception(f"Failed running {sql}")
        finally:
            conn.close()
        return rs_dict
