# Hack4u Academy Courses Library

Una biblioteca Python para consultar cursos de academia Hack4u.

## Cursos Disponibles
- Introduccion a Linux
- Python Ofensivo
- Personalizacion de Linux
- Introduccion al Hacking
## Instalacion

```python3
pip3 install hack4u
```

## Uso basico

### Listar todos los cursos

```python3
from hack4u import list_courses

for course in list_courses():
    print(course)

```

### Obtener un curso por su nombre

```python3
from hack4u import get_course_by_name

course = get_course_by_name('Introduccion a Linux')

print(course)

```

### Calcular duracion total de los cursos

```python3
from hack4u.utils import total_duration

print(f'Duracion total: { total_duration() } horas!')

```

