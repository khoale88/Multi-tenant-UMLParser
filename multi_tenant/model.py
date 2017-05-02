from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import ast

app = Flask(__name__)


app.config["SQL_USER"] = SQL_USER = 'root'
app.config["SQL_PASSWORD"] = SQL_PASSWORD = 'aichomavao'
app.config["SQL_HOSTNAME"] = SQL_HOSTNAME = 'localhost'
app.config["SQL_PORT"] = SQL_PORT = 3306
app.config["SQL_DATABASE"] = SQL_DATABASE = 'cmpe281'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%s:%s@%s:%d/%s' \
                                    %(SQL_USER, SQL_PASSWORD, SQL_HOSTNAME, SQL_PORT, SQL_DATABASE)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class AS_DICT():
    def as_dict(self):
        return ast.literal_eval(str(self))


class TENANT_TABLE(db.Model, AS_DICT):
    __tablename__ = "TENANT_TABLE"
    __table_args__ = (
        db.PrimaryKeyConstraint('tenant_id', 'table_name'),
    )
    tenant_id = db.Column(db.String(10), nullable=False)
    table_name = db.Column(db.String(45), nullable=False)
    table_desc = db.Column(db.String(80))

    def __init__(self, tenant_id, table_name, table_desc):
        self.tenant_name = tenant_id
        self.table_name = table_name
        self.table_desc = table_desc

    def __repr__(self):
        return '<TENANT %r>' %(self.tenant_id)

    def __str__(self):
        return str({"tenant_id" :self.tenant_id,
                    "table_name":self.table_name,
                    "table_desc":self.table_desc})


class TENANT_FIELDS(db.Model, AS_DICT):
    __tablename__ = "TENANT_FIELDS"
    __table_args__ = (
        db.PrimaryKeyConstraint('index', 'tenant_id', 'table_name'),
    )
    index = db.Column(db.Integer, nullable=False)
    tenant_id = db.Column(db.String(10), db.ForeignKey("TENANT_TABLE.tenant_id"),
                          nullable=False)
    table_name = db.Column(db.String(45), db.ForeignKey("TENANT_TABLE.tenant_table"),
                           nullable=False)
    field_name = db.Column(db.String(45),
                           unique=True, nullable=False)
    field_type = db.Column(db.String(80))
    field_column = db.Column(db.Integer,
                             nullable=False)

    def __init__(self, tenant_id, table_name, field_name, field_type, field_column):
        self.tenant_id = tenant_id
        self.table_name = table_name
        self.field_name = field_name
        self.field_type = field_type
        self.field_column = field_column

    def __repr__(self):
        return {    "index"       : self.index,
                    "tenant_id"   : self.tenant_id,
                    "table_name"  : self.table_name,
                    "field_name"  : self.field_name,
                    "field_type"  : self.field_type,
                    "field_column": self.field_column}

    def __str__(self):
        return str({"index"       : self.index,
                    "tenant_id"   : self.tenant_id,
                    "table_name"  : self.table_name,
                    "field_name"  : self.field_name,
                    "field_type"  : self.field_type,
                    "field_column": self.field_column})


class TENANT_DATA(db.Model, AS_DICT):
    __tablename__ = "TENANT_DATA"
    __table_args__ = (
        db.PrimaryKeyConstraint('record_id', 'tenant_id'),
    )
    record_id = db.Column(db.String(45), 
                          nullable=False)
    tenant_id = db.Column(db.String(10), db.ForeignKey("TENANT_TABLE.tenant_id"),
                          nullable=False)
    tenant_table = db.Column(db.String(45), db.ForeignKey("TENANT_TABLE.tenant_table"),
                             nullable=False)
    column_1 = db.Column(db.String(80))
    column_2 = db.Column(db.String(80))
    column_3 = db.Column(db.String(80))
    column_4 = db.Column(db.String(80))
    column_5 = db.Column(db.String(80))
    column_6 = db.Column(db.String(80))
    column_7 = db.Column(db.String(80))
    column_8 = db.Column(db.String(80))
    column_9 = db.Column(db.String(80))
    column_10 = db.Column(db.String(80))


    def __init__(self, record_id, tenant_id, tenant_table, column_1, 
                    column_2, column_3, column_4, column_5, column_6,
                    column_7, column_8, column_9, column_10):
        self.record_id = record_id
        self.tenant_id = tenant_id
        self.tenant_table = tenant_table
        self.column_1 = column_1
        self.column_2 = column_2
        self.column_3 = column_3
        self.column_4 = column_4
        self.column_5 = column_5
        self.column_6 = column_6
        self.column_7 = column_7
        self.column_8 = column_8
        self.column_9 = column_9
        self.column_10 = column_10

    def __repr__(self):
        return '<TENANT %r>' %(self.tenant_id)

    def __str__(self):
        return str({"record_id"     : self.record_id,
                    "tenant_id"     : self.tenant_id,
                    "tenant_table"  : self.tenant_table,
                    "column_1"      : self.column_1,
                    "column_2"      : self.column_2,
                    "column_3"      : self.column_3,
                    "column_4"      : self.column_4,
                    "column_5"      : self.column_5,
                    "column_6"      : self.column_6,
                    "column_7"      : self.column_7,
                    "column_8"      : self.column_8,
                    "column_9"      : self.column_9,
                    "column_10"     : self.column_10})
