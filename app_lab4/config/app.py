import yaml


class Config:
    def __init__(self, config_file='config/app.yml'):
        with open(config_file, 'r') as file:
            config_data = yaml.safe_load(file)

        db = config_data.get('db', {})
        self.DB_HOST = db.get('host')
        self.DB_PORT = int(db.get('port', 3306))
        self.DB_USER = db.get('user')
        self.DB_PASSWORD = db.get('password')
        self.DB_NAME = db.get('database')

    def get_db_uri(self) -> str:
        return (
            f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


config = Config()
