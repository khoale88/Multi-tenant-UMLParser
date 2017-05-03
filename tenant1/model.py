import mysql.connector

def get_tenant_data(config):
    cnx = mysql.connector.connect(user=config["DB_USER"], password=config["DB_PASSWORD"],
                                  host=config["DB_HOST"], port=config["DB_PORT"],
                                  database=config["DB_DATABASE"])
    cursor = cnx.cursor()
    query = ("select * from TENANT_DATA \
             where TENANT_ID = '" + config["TENANT_ID"] +\
             "' order by RECORD_ID desc LIMIT 1")

    cursor.execute(query)
    data = next(cursor)
    cursor.close()
    cnx.close()

    return data

def update_tenant_data(config,data):
    cnx = mysql.connector.connect(user=config["DB_USER"], password=config["DB_PASSWORD"],
                                  host=config["DB_HOST"], port=config["DB_PORT"],
                                  database=config["DB_DATABASE"])

    cursor = cnx.cursor()

    #ignore record_id for auto inc, only modify 3 - len(data)
    tenant_data = list(get_tenant_data(config))
    tenant_data[0] = None
    start = 3
    end = start + len(data)
    tenant_data[start:end] = data

    query = ("""insert into TENANT_DATA \
             values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""")
    cursor.execute(query, tenant_data)

    cnx.commit()
    cursor.close()
    cnx.close()

    return