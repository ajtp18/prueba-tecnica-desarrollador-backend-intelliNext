Esta Api esta orientada a una consulta de libros de una base de datos

Para correr la Api instalar las librerias mediante pip install requirements.txt, luego iniciarlo con pyhon manage.py runserver

Utilice DRF para crear Api

Utilice pandas para leer el csv de los libros he importarlos mediante management con la funcion import_books

Cree los views para el crud y todo esta listo para ser consumido por postman
http://127.0.0.1:8000/books/ la url para listar todos los libros
http://127.0.0.1:8000/books/ para crear
http://127.0.0.1:8000/books/{id}/ para actualizar
http://127.0.0.1:8000/books/{id}/ para borrar

Cabe recalcar que en las solicitudes de POST para crear y actualizar un book mediante postman nos pide un body en el cual debe tener lo siguiente:
{
    "title": "This field is required.",
    "author": "This field is required.",
    "yearOfPublication": "This field is required."
    "publisher": "This field is required."
}
En caso tal no colocar nada en el body, el servidor nos dara la respuesta de que estas son requeridas.

la base de datos que utilice fue la que trae por defecto Django, sqlite

en data se encuentra el csv por si necesitan importar mas libros con el comando python manage.py import_books, hay en total unos 650000, pero para la prueba solo utilice menos de 100 registros
