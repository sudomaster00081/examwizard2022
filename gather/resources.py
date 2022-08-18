from importlib import resources
from import_export import resources
from .models import Papers, Student

class PapersResource(resources.ModelResource):
    class meta:
        model = Papers

class StudentResource(resources.ModelResource):
    class meta:
        model = Student