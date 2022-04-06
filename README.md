# personalDataManagerPythonDjango
This is a simple application using Python as the language and the Django framework in which the data is stored in a local database in postgresql-pgAdmin 4.


Requirements to run the project:
1. Install the dependencies by executing the command in the terminal: pip install -r requirements.txt
2. Create a local database with postgresql named "sap_db"
3. We create a table with the name "persona"
4. We set the columns "id" Data type: integer, Not Null? True, Primary key?: True, 
   "nombre" Data type: character varying, Length/Precision: 250, Not Null? False, Primary key?: False,
   "apellido" Data type: character varying, Length/Precision: 250, Not Null? False, Primary key?: False, 
   "email" Data type: character varying, Length/Precision: 250, Not Null? False, Primary key?: False
5. In the terminal we locate ourselves in the "sap" folder which is where our project is and we execute the application:  python manage.py runserver
6. Open a browser and type: 127.0.0.1:8000