Esta Api esta orientada a una consulta de libros de una base de datos

Para correr la Api instalar las librerias mediante pip install requirements.txt, luego iniciarlo con pyhon manage.py runserver

Utilice DRF para crear Api

Utilice pandas para leer el csv de los libros he importarlos mediante management con la funcion import_books

Cree los views para el crud y todo esta listo para ser consumido por postman
http://127.0.0.1:8000/books/ la url para listar todos los libros


la base de datos que utilice fue la que trae por defecto Django, sqlite

en data se encuentra el csv por si necesitan importar mas libros con el comando python manage.py import_books, hay en total unos 650000, pero para la prueba solo utilice menos de 100 registros