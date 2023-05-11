from django.db import models



# This is class model
class students(models.Model):
    Student_Name=models.CharField(max_length=30)



class board(models.Model):
    Board= models.CharField(max_length=20)
    StudentB=models.ForeignKey(students, on_delete=models.CASCADE)

# Medium model
class medium(models.Model):
    Medium= models.CharField(max_length=30)
    StudentM=models.ForeignKey(students, on_delete=models.CASCADE)


# Standard Model
class standard(models.Model):
    Standard=models.IntegerField(default=0)
    StudentS=models.ForeignKey(students, on_delete=models.CASCADE)
    
