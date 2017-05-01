from flask import Flask, request, url_for, Response, make_response,json,abort
from flask_sqlalchemy import SQLAlchemy
import ast

config = {}

config["SQL_USER"] = SQL_USER = 'root'
config["SQL_PASSWORD"] = SQL_PASSWORD = 'aichomavao'
config["SQL_HOSTNAME"] = SQL_HOSTNAME = 'localhost'
config["SQL_PORT"] = SQL_PORT = 3306
config["SQL_DATABASE"] = SQL_DATABASE = 'cmpe281'

config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%s:%s@%s:%d/%s' \
                                    %(SQL_USER, SQL_PASSWORD, SQL_HOSTNAME, SQL_PORT, SQL_DATABASE)

from model import TENANT_TABLE as TNTB
def get_tenant_tables(tenant_id=None):
    if tenant_id is None:
        tables = TNTB.query.all()
    else:
        tables = TNTB.query.filter_by(tenant_id=tenant_id)
    return [ast.literal_eval(str(t)) for t in tables]

from model import TENANT_FIELDS as TNFL
def get_tenant_fields(tenant_id=None,table_name=None):
    if tenant_id is None:
        fields = TNFL.query.all()
    elif table_name is None:
        fields = TNFL.query.filter_by(tenant_id=tenant_id)
    else:
        fields = TNFL.query.filter_by(tenant_id=tenant_id, table_name=table_name)
    return [ast.literal_eval(str(f)) for f in fields]

from model import TENANT_DATA as TNDT
def get_tenant_data(tenant_id=None,tenant_table=None):
    if tenant_id is None:
        data = TNDT.query.all()
    elif tenant_table is None:
        data = TNDT.query.filter_by(tenant_id=tenant_id)
    else:
        data = TNDT.query.filter_by(tenant_id=tenant_id,tenant_table=tenant_table)

    return [ast.literal_eval(str(d)) for d in data]

def get_tenant_table_data(tenant_id):
    tables = get_tenant_tables()
    result = {"tenant_id":tenant_id,
              "tables"   :[]}
    for table in tables:
        temp_table = {"table_name":table["table_name"],
                      "table_desc":table["table_desc"],
                      "fields"    :[]}
        fields = get_tenant_fields(tenant_id, temp_table["table_name"])
        data = get_tenant_data(tenant_id, temp_table["table_name"])
        if len(data) == 0:
            continue
        for field in fields:
            field_column = "column_" + str(field["field_column"])
            temp_field = {"field_name":field["field_name"],
                          "field_type":field["field_type"],
                          "field_data":data[0][field_column]}
            temp_table["fields"].append(temp_field)
        result["tables"].append(temp_table)
    return result
