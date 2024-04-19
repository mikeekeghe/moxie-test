# Moxie API

## Description

Moxie API is a RESTful API built using the Django framework. It provides endpoints for managing a variety of activities related to a hypothetical business.

## Activities

- Install Django and necessary dependencies:
pipenv install django
pipenv shell
pipenv install djangorestframework
pipenv install markdown # Markdown support for the browsable API.
pipenv install django-filter # Filtering support


- Create Django project and apps:
django-admin startproject moxieapi .
python manage.py startapp medspa
python manage.py startapp services
python manage.py startapp appointments


- Update model, view, and URL files as per your requirements.

## Steps to Run the Application

1. Update the `.env` file to include the PostgreSQL database connection credentials.
2. Run the Django development server:
python manage.py runserver

3. Access the API endpoints through your preferred API client.

## API Endpoints

- `/medspa/`: Endpoint for managing medspa-related data.
- `/services/`: Endpoint for managing services offered.
- `/appointments/`: Endpoint for managing appointments.

## Technologies Used

- **Django**: Python-based web framework for building web applications quickly and efficiently.
- **Django REST Framework**: Toolkit for building Web APIs in Django.
- **PostgreSQL**: Open-source relational database management system for storing data.

## Contributors

- [Your Name or Organization](https://github.com/yourusername)

## License

This project is licensed under the [MIT License](LICENSE).

