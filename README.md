# Django_Wishlists
This is a small Django project with the purpose of creating a backend that allows users to register, signup and create wishlists. Each whishlist can have multiple items, which the user can choose himself.
Requirements to this project were: 

- User registration validation
- Creating Models and configuring Serializers
- ViewSets with correct permissions
- Logging via logfile

To test it out:
- create your own `.env`-File according to `.env.example`
- run `pip install - r requirements.txt`
- run `python manage.py migrate`
- run `py .\manage.py runserver`
