from peewee import *

from init import conf

sqlite_db = SqliteDatabase(conf.sprint_db_file_path)


class BaseModel(Model):
    """A base model that will use our Sqlite database."""
    # id 非空 自增 主键
    id = BigAutoField(primary_key=True)

    class Meta:
        database = sqlite_db


class Sprint(BaseModel):
    """
    创建迭代实体类
    """
    sprint_id = TextField()
    name = TextField()
    projectId = TextField()
    status = TextField()
    description = TextField()

    class Meta:
        table_name = 'sprint'



