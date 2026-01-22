# django-async-proj

This is a Django project that demonstrates the use of asynchronous views and HTTP requests.

## Project Structure

```
django-async-proj
├── manage.py
├── django_async_proj
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── asyncviews
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── requirements.txt
└── README.md
```

## Features

- Asynchronous views using Django's async capabilities.
- Example of non-blocking HTTP requests using `httpx`.
- Simple time counter to demonstrate asynchronous execution.

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd django-async-proj
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage

1. Access the asynchronous view at `http://127.0.0.1:8000/async-counter/` to see the non-blocking behavior.
2. Access the synchronous view at `http://127.0.0.1:8000/sync-counter/` to observe the blocking behavior.

**Important**: To run asynchronous views, start the server with ASGI:
```
python manage.py runserver
```

Or use an ASGI server like Daphne or Uvicorn:
```
pip install daphne
daphne django_async_proj.asgi:application
```

## How it works

- **Async View**: The counter runs in the background without blocking the response. The server returns immediately while counting continues in the console.
- **Sync View**: The counter blocks the request, and the response is only sent after all 5 seconds have elapsed.

## License

This project is licensed under the MIT License.