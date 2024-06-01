from django.db import models

class Student(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    address = models.TextField()
    fathersName = models.TextField()
    # my_field = models.BigAutoField(primary_key=True)
    # my_field = models.BinaryField(blank=True, null=True)
    # my_field = models.BooleanField(default=True)
    # my_field = models.CharField(max_length=255, default='default val')

    # my_field = models.DateField()
    # my_field = models.DateTimeField()
    # my_field = models.DecimalField(max_digits=5, decimal_places=2)
    # my_field = models.DurationField()
    # my_field = models.FilePathField(path='/path/to/files/')
    # my_field = models.FloatField()
    # my_field = models.ForeignKey(OtherModel, on_delete=models.CASCADE)
    # my_field = models.GenericIPAddressField()
    # my_field = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'Roll: {self.roll} - {self.name}'
