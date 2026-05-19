
from typing import List

class Course:
    
    def __init__(self, name: str, duration: float, link: str):
        self.name = name
        self.duration = duration
        self.link = link
        
    def __str__(self):
        return f'{{ name: {self.name}, duration: {self.duration} horas, link: {self.link}}}'
    
    def __repr__(self):
        return f'{self.name} [{self.duration} horas] (self.link)'


courses: List[Course] = [
        Course('Introduccion a Linux', 15.2, 'https://hack4u.io/curso/introduccion-a-linux'),
		Course('Python Ofensivo', 11.3, 'https://hack4u.io/curso/python-ofensivo'),
		Course('Personalizacion de Linux', 3.7, 'https://hack4u.io/curso/personalizacion-de-entorno-en-linux'),
		Course('Introduccion al Hacking', 53, 'https://hack4u.io/curso/introduccion-al-hacking')
	]

def list_courses()->None:
        for course in courses:
            print(course)

def search_course_by_name(name: str)->Course:
    for course in courses:
        if course.name == name:
            return course
    return None


     

