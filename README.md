# 📚 API REST de Biblioteca

API RESTful para gestión de biblioteca desarrollada con Django REST Framework.

## Características
✅ CRUD de libros, autores y categorías
✅ Autenticación con tokens
✅ Documentación con Swagger
✅ Permisos por roles

## Stack
- Django REST Framework
- PostgreSQL
- JWT Authentication

## Instalación
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Endpoints
```
GET /api/libros/ - Listar libros
POST /api/libros/ - Crear libro
```

Proyecto desarrollado para aprender APIs REST y buenas prácticas.
