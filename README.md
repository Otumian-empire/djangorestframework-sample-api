# someapidrf
This is a sample CRUD API using Django rest framework

## Dajngo version
Django Version: 2.2.5

## DRF version
djangorestframework version: 3.11.0


## student model
The student model consist of the student name as `name`,student id as `st_id`, student program as `program`, the type of program the student is been offered as `type` and their current year as `level`. 

### name
`name` is of type `CharField` of `max_length=200`

### st_id
`st_id` is of type `CharField` of `max_length=8` and is `unique`, 

### level
`level` is of type `IntegerField` with four choices
`(100, FR)`, `(200, Jr)`, `(300, SO)`, `(400, SR)` and the default is `100`

### program
`program` is of type `CharField` of `max_length=200` with seven choices `(None, Spectator)`, `(CS, Computer Science)`, `(MATH, Mathematics)`, `(STAT, Statistics)`, `(IT, Information Technology)`, `(PHY, Physics)`, `(CHEM, Chemistry)` and by default is `None`

### type
`type` of type `CharField` of `max_length=10` with eight choices `(Bsc, Bachelor of Science)`, `(Ba, Bachelor of Art)`, `(Cert, Certificate)`, `(Dipl, Diploma)`, `(Hnr, Honours)`, `(Ms, Masters of Science)`, `(Ma, Masters of Art)`, `(PhD, Doctor of Philosophy)`

## routes
### read all students
GET: `http://127.0.0.1:8000/student/`

### read a student
GET: `http://127.0.0.1:8000/student/<int:st_id>/` where `st_id` is the student ID. Sample route: `http://127.0.0.1:8000/student/10825747/`

### add student
POST: `http://127.0.0.1:8000/student/<int:st_id>/add/` where `st_id` is the student ID. Sample route: `http://127.0.0.1:8000/student/10825747/add/` them you pass, the form-data.

``` JSON
    
    "name": "Odame Michael Akeles",
    "st_id": "10825747",
    "level": 400,
    "program": "PHY",
    "type": "PhD"

```

### update a student's data
PUT: `http://127.0.0.1:8000/student/<int:st_id>/update/` where  `st_id` is the student ID. Sample route: `http://127.0.0.1:8000/student/10825747/update/` then pass the updated data in a form-data.

``` JSON
    
    "name": "Odame Michael",
    "st_id": "10825747",
    "level": 200,
    "program": "MATH",
    "type": "Bsc"

```

### delete a student's data
DELETE: `http://127.0.0.1:8000/student/<int:st_id>/delete/` where  `st_id` is the student ID. Sample route: `http://127.0.0.1:8000/student/10825747/delete/`.

