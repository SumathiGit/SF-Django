django-salesforce
=================


Quick Start
-----------

Install, configure a Salesforce connection, create a Salesforce model and run.

1. Install django-salesforce: ``pip install django-salesforce``

2. Add a salesforce connection to your ``DATABASES`` setting::

    'salesforce': {
        'ENGINE': 'salesforce.backend',
        'CONSUMER_KEY': '',                # 'client_id'   in OAuth2 terminology
        'CONSUMER_SECRET': '',             # 'client_secret'
        'USER': '',
        'PASSWORD': '',
        'HOST': 'https://test.salesforce.com',
    }

 3.python3 manage.py runserver
