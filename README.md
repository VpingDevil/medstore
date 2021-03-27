Medstore
===
<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangomade124x25.gif" border="0" alt="Made with Django." title="Made with Django." /></a>
![W3C Validation](https://img.shields.io/w3c-validation/default?targetUrl=https%3A%2F%2Fmedstore.pythonanywhere.com)

Medstore is a Medical store alike website, built as the submission for the Minor project in the college.

## How to run Locally

- Clone this repository
    ```bash
    git clone https://github.com/mukeshgurpude/medstore.git
    ```

- Alternatively you can [download](https://github.com/mukeshgurpude/medstore/archive/master.zip) this repository as `zip`, and extract it.
- Switch to the project directory and create a <span title="To access admin panel">superuser</span>
    ```bash
    cd medstore
    python3 manage.py createsuperuser
    ```
    <div style="border: 1px solid #f44;">
    <strong>Note</strong>: Depending on the system, python3 above should be replaced by <code>python</code> or <code>py</code>(in windows)
    </div>

- Initialize database
    ```bash
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
  
- Run the server
  ```bash
  python3 manage.py runserver
  ```
  This will start a local server on `port 8000`.
- Open http://localhost:8000 or http://127.0.0.1:8000, in the browser to view the website