from sqlalchemy import MetaData, create_engine, text

meta = MetaData()
db_engine = create_engine('postgresql://pythonuser:mypass@localhost:5432/mydb', echo=True)
meta.create_all(db_engine)


def print_params(stmt):
    return str(stmt.compile().params)


def print_result(rt):
    for row in rt:
        print(row)
    pass


def free_stmt(sql):
    stmt = text(sql)
    return execute_stmt(stmt, db_engine)


def execute_stmt(stmt, engine):
    conn = engine.connect()
    rt = conn.execute(stmt)
    return rt
