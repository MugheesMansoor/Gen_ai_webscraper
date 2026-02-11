# Gen_ai_webscraper
This project is an intelligent web scraping system that combines traditional scraping techniques with Generative AI to extract structured job listing data from websites.

Instead of manually parsing complex HTML structures, the system leverages a Large Language Model (LLM) to intelligently analyze and convert raw HTML into structured JSON format.

🔥 Key Features

🌐 Web scraping using BeautifulSoup

🤖 Generative AI-based data extraction (LLM-powered)

🗄 MySQL database storage

🌍 Flask web interface

📊 Dynamic filtering by year and month

🧠 Intelligent structured data generation

🏗 System Architecture

Scrape webpage using requests and BeautifulSoup

Send raw HTML to LLM (LLaMA 3.1 via OpenRouter)

AI extracts structured job data in JSON format

Store extracted data into MySQL database

Display results using Flask web application

🧠 How Generative AI is Used

Instead of manually writing complex HTML parsers, this project uses a Large Language Model to:

Understand HTML structure

Extract job title

Extract company name

Identify required skills

Extract posting date

Return structured JSON

This demonstrates how LLMs can automate semi-structured data extraction tasks.

🛠 Technologies Used

Python

Flask

MySQL

BeautifulSoup

Requests

OpenRouter API

LLaMA 3.1 8B Model

Generative AI (LLM)
