import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from db import create_tables, get_connection
from ai_extraction_model import extract_jobs

URL = "https://realpython.github.io/fake-jobs/"


def main():
    create_tables()

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = soup.find_all("div", class_="card-content")

    conn = get_connection()
    cursor = conn.cursor()

    for job in jobs:
        title = job.find("h2", class_="title").get_text(strip=True)
        company = job.find("h3", class_="subtitle").get_text(strip=True)
        location = job.find("p", class_="location").get_text(strip=True)

        link = job.find_next("a")["href"]

        cursor.execute(
            """
            INSERT INTO fake_jobs (title, company, location, link, description)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (title, company, location, link, "jobs_description")
        )

    conn.commit()
    conn.close()

    print("✅ Jobs inserted successfully")

if __name__ == "__main__":
    main()