from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import Engine

databaseName = "gestionbd"

userName = "root"

userPassword = ""
port = "3306"
serverConnection = "localhost"

connectionToDataBase = f'mysql+mysqlconnector://{userName}:{userPassword}@{serverConnection}:{port}/{databaseName}'

# connectionToDataBase = "mssql+pyodbc://adrian-admin@adrian-123456:Duhast2379497@adrian-123456.database.windows.net:1433/ControlGastos?driver=ODBC+Driver+17+for+SQL+Server&Encrypt=yes&TrustServerCertificate=no"

engine = create_engine(connectionToDataBase)

sessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)