class Config:
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///vschool.db'
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:12345678@localhost:5432/postgres1"
    SQLALCHEMY_TRACK_MODIFICATIONS = False