Certainly! Here's a sample `README.md` file that explains how to run your Django project and how to send a request to your API:

```markdown
# Dividend API Project

This project is a Django-based API that allows you to retrieve dividend summaries by symbol and year.

## Prerequisites

Before running the project, make sure you have the following installed:

- Python (3.6 or higher)
- Django
- MySQL (or your preferred database)

## Getting Started

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Adshow/YahooFinanceAPI.git
   cd dividend-api
   ```

2. Install the project's dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your database configuration in `dividend_api/settings.py`. You can use MySQL or any other database supported by Django.

4. Apply migrations to create the database tables:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser to access the Django admin interface (optional):

   ```bash
   python manage.py createsuperuser
   ```

6. Load data from your CSV file or Yahoo Finance API into the database:

   ```bash
   python manage.py shell
   >>> from dividend.services import load_dividends_to_db
   >>> load_dividends_to_db("PETR4.SA")
   ```

## Running the Project

Start the Django development server:

```bash
python manage.py runserver
```

The API will be accessible at `http://localhost:8000/api/dividends-summary/`.

## Sending Requests

You can send GET requests to retrieve dividend summaries. Use the following format:

```
GET http://localhost:8000/api/dividends-summary/?symbol=<SYMBOL>&year=<YEAR>
```

- Replace `<SYMBOL>` with the stock symbol you want to query (e.g., PETR4.SA).
- Replace `<YEAR>` with the year for which you want to retrieve dividend summaries (e.g., 2022).

Example using `curl`:

```bash
curl -X GET "http://localhost:8000/api/dividends-summary/?symbol=PETR4.SA&year=2022"
```

The API will respond with JSON data containing the total dividends for the specified symbol and year.

## Admin Interface

You can access the Django admin interface at `http://localhost:8000/admin/` to manage database records. Log in with the superuser credentials you created earlier.

## Troubleshooting

If you encounter any issues or have questions, please open an issue in this repository.

```

Replace `<SYMBOL>` and `<YEAR>` with actual symbol and year values. This `README.md` file provides clear instructions on setting up the project, running it, and making requests to the API. It also mentions how to access the admin interface for managing data.

Make sure to adapt it to your specific project details as needed.