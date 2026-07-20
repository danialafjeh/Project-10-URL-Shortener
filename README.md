# About Project

# Django URL Shortener

A simple and practical URL Shortener web application built with **Django** and **PostgreSQL**.

The application allows users to submit a long URL and instantly receive a shortened version that redirects to the original website.

---

## Features

- Generate unique short URLs
- Redirect short links to their original destinations
- Store URLs in a PostgreSQL database
- Automatic unique short code generation
- Display the generated short URL after creation
- Track creation date for every shortened URL
- Server-side validation using Django ModelForms
- Clean separation of application logic using utility functions

---

## Technologies Used

- Python
- Django
- Django ModelForms
- PostgreSQL
- HTML
- CSS

---

## Project Structure

The application follows the Django MVT architecture.

### Views

The project is separated into three dedicated views:

- **Home View**
  - Displays the URL submission form
  - Validates user input
  - Generates a unique short code
  - Saves data into PostgreSQL

- **Result View**
  - Displays the generated short URL

- **Redirect View**
  - Receives the short code
  - Finds the corresponding original URL
  - Redirects the user to the destination website

---

## Database Model

The application stores:

- Original URL
- Generated Short Code
- Creation Date

---

## Short Code Generation

Short URLs are generated using a custom utility function located in:

```
utils.py
```

The generator:

- Creates random alphanumeric codes
- Prevents duplicate short codes
- Produces unique URLs before saving to the database

---
