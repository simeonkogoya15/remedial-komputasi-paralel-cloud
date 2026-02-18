from flask import Flask, jsonify
import dask.dataframe as dd
import pandas as pd
from sqlalchemy import create_engine
import os

app = Flask(__name__)

DATABASE_URL = os.getenv("DATABASE_URL")

@app.route('/list')
def list_data():
    engine = create_engine(DATABASE_URL)

    df = pd.read_sql("SELECT * FROM test", engine)

    ddf = dd.from_pandas(df, npartitions=1)

    result = ddf.compute().to_dict(orient="records")

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8123)
