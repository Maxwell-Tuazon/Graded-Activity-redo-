# Django Mini Twitter Clone

This is a Django app that allows users to post tweets with optional images. Tweets containing the prohibited words **shit**, **fuck**, and **bobo** are not allowed.

## Features

- Post tweets with text (max 280 chars)
- Upload an image with your tweet
- Prohibited word filtering (case-insensitive)
- View and manage tweets via Django Admin

## Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (optional, for admin access)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

### 7. Usage

- Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- Fill in your tweet and (optionally) upload an image. Forbidden words will block submission.
- Visit [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) to manage tweets.

---

## Notes

- Do **not** commit your `db.sqlite3`, `media/`, or the `venv/` folder.
- The project uses `Pillow` for image handling.