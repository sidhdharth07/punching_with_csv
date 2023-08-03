from django.db import models

# Create your models here.
class RegisterModel(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateField()
    emp=models.CharField(max_length=10,unique=True)

class timing_model(models.Model):
    emp=models.ForeignKey(RegisterModel, on_delete=models.CASCADE,null=True,blank=True)
    clock_in=models.DateTimeField()
    clock_out=models.DateTimeField(null=True,blank=True)
    durations = models.CharField(null=True)

    def duration(self):
        if self.clock_out is not None:
            self.durations= self.clock_out - self.clock_in
            self.durations=self.durations.total_seconds() / 3600
            return round(self.durations,2)
        return None
    