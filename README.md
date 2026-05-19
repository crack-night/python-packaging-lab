# Hack4u Academy Courses Library

> Renombrado: cracknight

Una biblioteca Python para consultar cursos de academia Hack4u.

## Cursos Disponibles
- Introduccion a Linux
- Python Ofensivo
- Personalizacion de Linux
- Introduccion al Hacking
## Instalacion

```python3
pip3 install cracknight
```

## Uso basico

### Listar todos los cursos

```python3
from cracknight import list_courses

for course in list_courses():
    print(course)

```

### Obtener un curso por su nombre

```python3
from cracknight import get_course_by_name

course = search_course_by_name('Introduccion a Linux')

print(course)

```

### Calcular duracion total de los cursos

```python3
from cracknight.utils import total_duration

print(f'Duracion total: { total_duration() } horas!')

```

