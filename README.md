# COVID-19-Database-Challenge

Implement database structure to deal with covid-19 to save the world!

- Use Django-1.11 and Python 2.7
- Requirements:
    * [ ] Hospital including name and city
    * [ ] Department in hospital including name
    * [ ] Hospital worker that is part of one or more department and can be in 
    position of Doctor or Nurse. Also have name, age and gender (Male, Female, Other)
    * [ ] Patient in specific department. Also have name, age and gender (Male, Female, Other)
    * [ ] Medical examination result of specific patient with examine time,
    the hospital worker that performed the examination and the result (Healthy, Corona, Botism, Dead)

---

# Guided Solution

1. Add `.gitignore` file.   
   `db.sqlite3`, `.pyc`
2. Use Django default `id` field and don't set it yourself.   
❌ Don't do:
    ```python
    class Hospital(models.Model):
        id = models.AutoField(primary_key=True)
    ```
3. Model fields shouldn't start with class name as prefix   
    ✔ Do:
    ```python
        class Hospital(models.Model):
             name = models.CharField(max_length=200, null=False, blank=False)
    ```    
    ❌ Don't do:    
    ```python    
    class Hospital(models.Model):
        hospital_name = models.CharField(max_length=200, null=False, blank=False)
    ```
4. Model names that is not special for our app should start with the app name as prefix.   
    *This will prevent problems in case of project with multiple apps that might share the same model names.   
    ✔ Do:
    ```python
        class HospitalWorker(models.Model):
            ...
   
        class ProjectConfigurations(modelsModel):
            ...
    ```    
    ❌ Don't do:    
    ```python
        class Worker(models.Model):
            ...
   
        class Configurations(modelsModel):
            ...
    ```
   *In case of multiple apps project, models like `Person` should be set in different app named `common`.     
5. Explicitly set important arguments as keyword-args and avoid relying on default values.   
This will make the model definition easier to understand.   
   `null`, `blank`, `to`, `related_name`, `auto_now`, `auto_now_add`, `on_delete`   
   ✔ Do:
     ```python
    class HospitalWorker(models.Model):
        person = models.ForeignKey(
            to=Person,
            related_name='hospital_jobs',
            null=False,
            blank=False,
            on_delete=models.CASCADE,
        )
        position = models.CharField(max_length=255, blank=False, null=False, )
        position_start_datetime = models.DateTimeField(auto_now=False, auto_now_add=False, )
     ```
6. `CharField` choices:
   1. Create constants attributes for every choice.   
        This way it will be possible to use them in other purposes.
   2. Don't use shorten values to reduce the memory (e.g "F" instead of "Female")   
      It doesn't save a lot of memory and make it difficult for debugging.
   
   ✔ Do:
   ```python
         class MedicalExaminationResult(models.Model):
             RESULT_HEALTHY = 'Healthy'
             RESULT_CORONA = 'Corona'
             RESULT_BOT = 'Botism'
             RESULT_DEAD = 'Dead'
             
             result = models.CharField(max_length=7, blank=False, null=True, choices=(
                 (RESULT_HEALTHY, RESULT_HEALTHY),
                 (RESULT_CORONA, RESULT_CORONA),
                 (RESULT_BOT, RESULT_BOT),
                 (RESULT_DEAD, RESULT_DEAD),             
             ))         
   ```
    Then the usage will look like this:
    ```python 
   MedicalExaminationResult.objects.filter(result=MedicalExaminationResult.RESULT_BOT)
   ```
   ❌ Don't do:    
   ```python
         class MedicalExaminationResult(models.Model):
             RESULTS = (
                 ('H', 'Healthy'),
                 ('C', 'Corona'),
                 ('B', 'Botism'),
                 ('D', 'Dead'),             
             )
             
             result = models.CharField(max_length=7, blank=False, null=True, choices=RESULTS)         
   ```   
7. Implement both `__repr__` and `__str__` (https://www.geeksforgeeks.org/str-vs-repr-in-python/).
    1. It's ok to use `__repr__` implementation in `__str__`.
    2. Add the class name as prefix   .
    3. Wrap the text "<....text....>".
    4. Use unicode prefix `u` in Python2.7 to avoid exceptions in case of unicode characters.
    5. In case you use Python2.7 - implement `__unicode__`.
   
   ✔ Do:
     ```python
    class Hospital(models.Model):
        name = models.CharField(db_index=True, max_length=255, blank=False, null=False, )
        city = models.CharField(max_length=255, blank=False, null=False, )
        
        def __repr__(self):
            return '<Hospital {name}>'.format(name=self.name, )    
               
        def __str__(self):    
            return repr(self)
     ```
   Python2.7
   ```python
    class Hospital(models.Model):
        name = models.CharField(db_index=True, max_length=255, blank=False, null=False, )
        city = models.CharField(max_length=255, blank=False, null=False, )
        
        def __repr__(self):
            return u'<Hospital {name}>'.format(name=self.name, )    
        
        def __unicode__(self):
            return repr(self)
               
        def __str__(self):    
            return repr(self)
     ```
   To handle unicode characters in python 2.7 it is recommended to set coding to utf-8 and import `unicode_literals`
    This way you won't need to use `u` prefix for strings.
    ```python
    # -*- coding: utf-8 -*-
    from __future__ import unicode_literals
    ```
8. `related_name` argument
   1. Starts with the class name in plural.
   2. Model can have two fields with the same related name.
   
    ✔ Do:
    ```python
        class HospitalPatient(models.Model):
            person = models.ForeignKey(
                to=Person,
                related_name='patients_details',
                null=False,
                blank=False,
                on_delete=models.CASCADE,
            )
            department = models.ForeignKey(
                to=HospitalDepartment,
                related_name='patients_details',
                null=False,
                blank=False,
                on_delete=models.CASCADE,
            )
    ```
   Then the usage will look like this:
    ```python
   hospital_department = HospitalDepartment.object.get(hospital=3, name='Nursing')
   patients_details = hospital_department.patients_details
   ```
    ❌ Don't do (!!):    
    ```python
        class HospitalPatient(models.Model):
            person = models.ForeignKey(
                to=Person,
                related_name='persons',
                null=False,
                blank=False,
                on_delete=models.CASCADE,
            )
            department = models.ForeignKey(
                to=HospitalDepartment,
                related_name='departments',
                null=False,
                blank=False,
                on_delete=models.CASCADE,
            )
    ```    
   Setting `related_name` like in the example above, will lead to the following code which makes no sense
   ```python
   hospital_department = HospitalDepartment.object.get(hospital=3, name='Nursing')
   patients_details = hospital_department.departments
   ```
9. Add database index to relevant fields.    
     Database index can have significant performance improvement if used wisely.    
     1. Recommended video https://www.youtube.com/watch?v=fsG1XaZEa78&ab_channel=Socratica
     2. Don't set `db_index` to `enum` fields since it won't improve the performance and the memory cost is not worth it.
     3. Database index is automatically created on the `ForeignKey` in Django (https://docs.djangoproject.com/en/3.2/ref/models/fields/#foreignkey)
     4. Don't create db index for fields that won't be in frequent use for queries.
   
     ✔ Do:
     ```python
    class Person(models.Model):
        name = models.CharField(db_index=True, max_length=255, blank=False, null=False, )
        middle_name = models.CharField(max_length=255, blank=False, null=False, )
     ```    
     ❌ Don't do:    
     ```python
    class Person(models.Model):
        GENDER_MALE = 'Male'
        GENDER_FEMALE = 'Female'
        GENDER_UNDEFINED = 'Other'
    
        gender = models.CharField(db_index=True, max_length=6, blank=False, null=False, choices=(
            (GENDER_MALE, GENDER_MALE),
            (GENDER_FEMALE, GENDER_FEMALE),
            (GENDER_UNDEFINED, GENDER_UNDEFINED),
        ))   
     ```    
10. Use `PositiveInteger` and `PositiveSmallIntegerField` if possible.   
    ✔ Do:
    ```python
        class Person(models.Model):
             age = models.PositiveSmallIntegerField(null=False)
    ```    
11. Person-HospitalWorker-HospitalPatient inheritance VS composition
    1. Inheritance in Django justifies itself just in cases where the parent type doesn't have a use of it's own.   
    For example in case of items models, we could create parent model named Item which will hold common fields such as `name`, `supplier`, `price` etc...
    ```Python
        class Item(models.Model):
            ...
    
        class Book(Creature):
            ...
    
        class Computer(Creature):
            ...
    ```
    2. In case of inheritance, consider setting the parent class to be abstract if it used to hold common fields and isn't in use by it's own.
    ```python
        class ContactInfo(models.Model):
            ...
    
            class Meta:
                abstract = True
    
        class Customer(ContactInfo):
            ...
    
        class Staff(ContactInfo):
            ...
    ``` 
    3. One of the significant disadvantage of inheritance that it might cause duplication of data.
    In our exercise, having `HospitalWorker` and `HospitalPartient` inherit from `Person` will cause data duplication if we have a person that is both `HospitalWorker` and `HospitalPatient`.   
    For this reason, the right implementation is `HospitalWorker` and `HospitalPatient` with a `ForeignKey` to `Person`.
       
