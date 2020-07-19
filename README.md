# SmURL
A URL shortener based on Django.

### Features
- It generates a base62 encoded token and stores the token and url in the database. The short url is represented in the format of - smurl.com/token. 

- It the given url already exist in the database, that token is fetched otherwise a new token is generated from primary key.

- The Home page have buttons to open the URl in new tab and also to copy url in the clipboard.

### Requirement

Python 3.6 or above.

### To Run Locally

1. Create an environment variable

    `python3 -m venv env`

2. Install the Dependencies

    `pip install -r requirements.txt`

    or

    `pip3 install -r requirements.txt`

3. Run the Server

    `python manage.py runserver`

4. Open localhost:8000 to open the homepage and use it.

## Author

[Debajyoti Dutta](https://github.com/DeboDevelop)