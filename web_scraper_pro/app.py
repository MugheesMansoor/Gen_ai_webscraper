from flask import Flask, render_template, request
from db import get_connection

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    year = request.args.get("year", "").strip()
    month = request.args.get("month", "").strip()

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query_sql = "SELECT * FROM fake_jobs WHERE 1=1"
    params = []

    if year:
        query_sql += " AND posted_on LIKE %s"
        params.append(f"%{year}%")

    if month:
        query_sql += " AND posted_on LIKE %s"
        params.append(f"%{month}%")

    cursor.execute(query_sql, params)
    jobs = cursor.fetchall()
    conn.close()

    return render_template("index.html", products=jobs)

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)