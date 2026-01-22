import mysql.connector
import os
from pandas import DataFrame


def get_connection():
    connection = mysql.connector.connect(
        host= os.getenv("DB_HOST","localhost"),
        user= os.getenv("DB_USER","root"),
        password=os.getenv("DB_PASSWORD",""),
        database=os.getenv("DB_NAME","mydatabase")
    )
    return connection

def create_table():
    connection = get_connection()
    cursor = connection.cursor()
    sql = """
            CREATE TABLE IF NOT EXISTS weapons
            (id INT AUTO_INCREMENT PRIMARY KEY,
            weapon_id VARCHAR(255),
            weapon_name VARCHAR(255),
            weapon_type VARCHAR(255),
            range_km INT,
            weight_kg FLOAT,
            manufacturer VARCHAR(255),
            origin_country VARCHAR(255),
            storage_location VARCHAR(255),
            year_estimated INT,
            risk_level VARCHAR(20))
        """
    cursor.execute(sql)

def insert_data_to_db(df:DataFrame):
    connection = get_connection()
    cursor = connection.cursor()
    sql = """
    INSERT INTO weapons (
    weapon_id,weapon_name,weapon_type,range_km,weight_kg,manufacturer,origin_country,storage_location,year_estimated,risk_level
    ) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)
    """
    for row in range(len(df)):
        val = (
            df.iloc[row]["weapon_id"],
            df.iloc[row]["weapon_name"],
            df.iloc[row]["weapon_type"],
            int(df.iloc[row]["range_km"]),
            float(df.iloc[row]["weight_kg"]),
            df.iloc[row]["manufacturer"],
            df.iloc[row]["origin_country"],
            df.iloc[row]["storage_location"],
            int(df.iloc[row]["year_estimated"]),
            df.iloc[row]["risk_level"])
        cursor.execute(sql,val)
    connection.commit()
    connection.close()
    return {"status": "success","inserted_records": len(df)}