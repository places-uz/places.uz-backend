### [MondayLabs](https://mondaylabs.tech)
![]()

###### Set
* _Clone repository_ `https://github.com/mondaylabs/todo.git`
* _Go to_ `backend/config` _and copy_ `example.settings_dev.py` as `settings_dev.py`
* _Create new postgres database_
* _Open_ `backend/config/settings_dev.py` _file ans set up your database and email credentials_
* _Got to_ [Google Admin](https://myaccount.google.com/lesssecureapps) _and allow less secure app to connect to your account_ 
* _Create new virtual environment_ `mkvirtualenv todo`
* _Go to_ `backend` _and install dependencies_ `pip install -r requirements.txt`
* _Go to_ `frontend` _and install dependencies_ `yarn`


###### Run
* _Go to_ `backend` _folder_
* _Select virtual environment_ `workon todo`
* _Run server_ `python manage.py runserver`
* _Open new Terminal and go to_ `frontend` 
* _Run frontend_ `yarn start`

###### Dev
* [Python 3.7](https://www.python.org/) _or higher_
* [PostgreSQL 9.3](https://www.postgresql.org/) _or higher_
* [Virtualenv Wrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) _for Mac OS or_ [Virtualenv Wrapper Win](https://pypi.org/project/virtualenvwrapper-win/) _for Windows_
* [Node.js 11](https://nodejs.org/) _or higher_
* [Yarn 1.13](https://yarnpkg.com/en/) _or higher_
* [VSCode](https://code.visualstudio.com/) _optional_

