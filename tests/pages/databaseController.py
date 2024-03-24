import pymysql
from pages.settings import SettingKeys, Settings

def connect():
    return pymysql.connect(host=SettingKeys.DB_HOST,
                           user=SettingKeys.DB_USER,
                           password=SettingKeys.DB_PASSWORD,
                           database=SettingKeys.DB_DATABASE)
 
class Database:
    def __init__(self):
        self.setting = Settings()   
        
        
class DataBaseController(Database):
    def __init__(self):
        Database.__init__()
        
        
    @staticmethod
    def insert_data(data=""):
        db = connect()
        cursor = db.cursor()
        query = "INSERT INTO bootcamp.case_reports (case_status) VALUES ('{}')".format(data)
        cursor.execute(query)
        db.commit()
        db.close()