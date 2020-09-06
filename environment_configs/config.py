__all__ = ['Development', 'Testing', 'Production']


class Base:
    DEBUG = False
    TESTING = False


class Development(Base):
    DEBUG = True
    DATABASE_URI = "mysql+mysqldb://root:root@localhost/demo"


class Testing(Base):
    DEBUG = False
    DATABASE_URI = "mysql+mysqldb://root:root@test_server_host_name/demo_test"


class Production(Base):
    DEBUG = False
    DATABASE_URI = "mysql+mysqldb://root:root@prod_host_name/demo_prod"
