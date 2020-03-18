from django.db import models

# Create your models here.


class StudentModel(models.Model):
    """ 
    student name
    student st_id
    student level
    student program
    student program type
     """
    name = models.CharField(max_length=200)
    st_id = models.CharField(max_length=8)
    
    level = models.IntegerField(
        choices=[
            (100, "FR"), (200, "SO"), (300, "JR"), (400, "SR")
        ],
        default=100
    )

    program = models.CharField(
        max_length=200,
        choices=[
            ("None", "Spectator"),
            ("CS", "Computer Science"),
            ("MATH", "Mathematics"),
            ("STAT", "Statistics"),
            ("IT", "Information Technology"),
            ("PHY", "Physics"),
            ("CHEM", "Chemistry"),
        ],
        default="NONE"
    )

    type = models.CharField(
        max_length=10,
        choices=[
            ("Bsc", "Bachelor of Science"),
            ("Ba", "Bachelor of Art"),
            ("Cert", "Certificate"),
            ("Dipl", "Diploma"),
            ("Hnr", "Honours"),
            ("Ms", "Masters of Science"),
            ("Ma", "Masters of Art"),
            ("PhD", "Doctor of Philosophy"),
        ],
        default="Bsc"
    )

    def __str__(self):
        return f"{self.name} {self.type}"
