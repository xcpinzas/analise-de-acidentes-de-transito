# Analise-de-acidentes-de-transito
 analise dados de acidentes de transito no Brasil dos anos 2021 a 2024.

## Features

- Django-based backend

    - [Django](https://www.djangoproject.com/)
    - Separate settings for different environments (local/staging/production)
    - Python 3.5 or later
    - [SPA] Accessible from port `8000` for local development

- Frontend app with JavaScript (ES2015), Jquery and CSS

    - Latest JavaScript features from [ES2015](https://babeljs.io/docs/learn-es2015/)
      [Autoprefixer](https://github.com/postcss/autoprefixer) for more convenient styling
    - [Webpack](https://webpack.github.io/) is used to bundle and minify JavaScript and styles
    - [SPA] Accessible from port `8000` for local development

- Batteries

    - Docker / Docker Compose integration from github actions
    - Linting of Python, JavaScript and Sass code with [Prospector](http://prospector.landscape.io/),
      [ESLint](http://eslint.org/) and [stylelint](https://stylelint.io/)
    - Automated code-formatting using [black](https://black.readthedocs.io) and [prettier](https://prettier.io)
    - [unit.test](https://docs.python.org/3/library/unittest.html) and [coverage](https://coverage.readthedocs.io/) integration


## Usage

To use this project, first ensure that you have
[Virtualenv](https://virtualenv.pypa.io/en/latest/) `2020.0.31` available.

After that, you should:
1. Activate the myenv created by virtualenv:
    ```
    myenv/scripts/activate
    ```
2. Install the requirements of the project template by running
    ```
    pip install -r requirements/requirements.txt
    ```
3. Create superuser
    ```
    python manage.py createsuperuser
    ```
    
4. Run the project
    ```
    python manage.py runserver --insecure
    ```

## Test
To test the system:

1. Unit tests
 ```
 python manage.py test -v apps/
 ```
 
 2. Funcional tests
 ```
 python manage.py test -v UI/
 ```

