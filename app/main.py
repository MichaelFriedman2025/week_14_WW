from fastapi import FastAPI, UploadFile,File
import uvicorn
from models import doing_all
from db import insert_data_to_db,create_table

app = FastAPI()



@app.post("/upload")
def get_file(file:UploadFile = File(...)):
    create_table()
    df  = doing_all(file)
    res = insert_data_to_db(df)
    return res


if __name__=="__main__":
    uvicorn.run("main:app",port=8080,host="localhost",reload=True)