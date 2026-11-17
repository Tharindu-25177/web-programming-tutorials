from datetime import datetime
from django.core.management.base import BaseCommand
from django.utils import timezone
from myApp.models import Student, Module

class Command(BaseCommand):
    help = 'Add example students and modules'

    def handle(self, *args, **options):
        module_data = [
            ('MOD002619','Web Programming'),
            ('MOD002643','Image Processing'),
            ('MOD002691','Final Project'),
            ('MOD003212','Introduction to Programming'),
            ('MOD003484','Software Principles'),
        ]
        module_objects = {}
        for code, name in module_data:
            module, created = Module.objects.get_or_create(code=code, defaults={'name':name})
            module_objects[code] = module

        if Student.objects.exists():
            self.stdout.write(self.style.WARNING('Students already exist; no sample students added.'))
            return

        sample_students = [
            ('Connie','James',20,'connie@example.com','MOD002619|MOD003212'),
            ('Joshua','Brown',21,'joshua@example.com','MOD002643|MOD003484'),
            ('Amara','Perera',19,'amara@example.com','MOD002691|MOD003212'),
        ]
        for first, last, age, email, codes in sample_students:
            student = Student.objects.create(
                firstName=first, lastName=last, age=age, email=email,
                enrolmentDate=timezone.make_aware(datetime(2026,1,15))
            )
            for code in codes.split('|'):
                student.modules.add(module_objects[code])
        self.stdout.write(self.style.SUCCESS('Example students and modules added.'))
