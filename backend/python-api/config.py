from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'user_db'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 8889
app.config['MYSQL_DATABASE_CONNECT_TIMEOUT'] = 1000
app.config['MYSQL_DATABASE_WAIT_TIMEOUT'] = 28800
app.config['MYSQL_DATABASE_INTERACTIVE_TIMEOUT'] = 28800
mysql.init_app(app)