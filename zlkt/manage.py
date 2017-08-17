# encoding:utf-8
# 用来写命令/数据迁移

from flask_script import Manager
from flask_migrate import MigrateCommand,Migrate
from zlkt import app
from exts import db
from models import User

# 创建命令的对象
manager = Manager(app)
# 创建迁移的对象，绑定app和db
migrate = Migrate(app,db)
# 添加迁移命令到manager中
manager.add_command('db',MigrateCommand)

# 作为主文件来运行
if __name__ == "__main__":
    manager.run()
