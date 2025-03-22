from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DiabetesRecord(models.Model):
    
    GENDER_CHOICES = [
        (1, "Male"),
        (0, "Female")
    ]
    SMOKING_CHOICES = [
        (3, "Former Smoker"),
        (1, "Current Smoker"),
        (4, "Never Smoked")
    ]
    PREDICTION_CHOICES = [
        (1, "Positive"),
        (0, "Negative")
    ]
    
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    record_id = models.AutoField(primary_key=True)
    prediction_date = models.DateField(auto_now_add=True)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    age = models.IntegerField()
    hypertension = models.BooleanField(default=False)
    heart_disease = models.BooleanField(default=False)
    smoking_status = models.IntegerField(choices=SMOKING_CHOICES)
    bmi = models.FloatField()
    glucose_level = models.FloatField()
    prediction = models.IntegerField(choices=PREDICTION_CHOICES)
    
    def __str__(self):
        return f"Patient {self.user_id} - last prediction on {self.prediction_date} - prediction {self.prediction} "
    
    
class StrokeRecord(models.Model):
    
    GENDER_CHOICES = [
        (0, "Male"),
        (1, "Female")
    ]
    SMOKING_CHOICES = [
        (1, "Former Smoker"),
        (2, "Current Smoker"),
        (0, "Never Smoked")
    ]
    WORK_TYPE_CHOICES = [
        (0, "Private"),
        (1, "Self-Employed"),
        (2, "Looks after children"),
        (3, "Govt. Job"),
        (4, "Never Worked"),
    ]
    RESIDENCE_CHOICES = [
        (1, "Urban"),
        (2, "Rural")
    ]
    PREDICTION_CHOICES = [
        (1, "Positive"),
        (0, "Negative")
    ]
    
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    record_id = models.AutoField(primary_key=True)
    prediction_date = models.DateField(auto_now_add=True)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    age = models.IntegerField()
    hypertension = models.BooleanField(default=False)
    heart_disease = models.BooleanField(default=False)
    ever_married = models.BooleanField(default=False)
    work_type = models.IntegerField(choices=WORK_TYPE_CHOICES)
    residence_type = models.IntegerField(choices=RESIDENCE_CHOICES)
    glucose_level = models.FloatField()
    bmi = models.FloatField()
    smoking_status = models.IntegerField(choices=SMOKING_CHOICES)
    prediction = models.IntegerField(choices=PREDICTION_CHOICES)
    
    def __str__(self):
        return f"Patient {self.user_id} - last prediction on {self.prediction_date} - prediction {self.prediction} "
        
        
class DepressionRecord(models.Model):
    
    GENDER_CHOICES = [
        (1, "Male"),
        (0, "Female")
    ]
    SLEEP_CHOICES = [
        (0, "5-6 hours"),
        (1, "7-8 hours"),
        (2, "<5 hours"),
        (3, ">3 hours")
    ]
    DIETARY_CHOICES = [
        (0, "Healthy"),
        (1, "Moderate"),
        (3, "Unhealthy")
    ]
    DEGREE_CHOICES = [
        (11, "Class 12"),
        (2, "B.Ed"),
        (1, "B.Com"),
        (0, "B.Arch"),
        (7, "BCA"),
        (25, "MSc"),
        (4, "B.Tech"),
        (21, "MCA"),
        (17, "M.Tech"),
        (9, "BHM"),
        (10, "BSc"),
        (15, "M.Ed"),
        (3, "B.Pharm"),
        (14, "M.Com"),
        (6, "BBA"),
        (20, "MBBS"),
        (12, "LLB"),
        (8, "BE"),
        (5, "BA"),
        (16, "M.Pharm"),
        (22, "MD"),
        (19, "MBA"),
        (18, "MA"),
        (27, "PhD"),
        (13, "LLM"),
        (24, "MHM"),
        (23, "ME"),
        (26, "Others"),
    ]
    PREDICTION_CHOICES = [
        (1, "Positive"),
        (2, "Negative")
    ]
    
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    record_id = models.AutoField(primary_key=True)
    prediction_date = models.DateField(auto_now_add=True)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    academic_pressure = models.IntegerField()
    cgpa = models.FloatField()
    study_satisf = models.IntegerField()
    sleep = models.IntegerField(choices=SLEEP_CHOICES)
    dietary_habits = models.IntegerField(choices=DIETARY_CHOICES)
    degree = models.IntegerField(choices=DEGREE_CHOICES)
    suicidal = models.BooleanField(default=False)
    study_hours = models.IntegerField()
    financial_stress = models.IntegerField()
    family_mental_illness = models.BooleanField(default=False)
    prediction = models.IntegerField(choices=PREDICTION_CHOICES)
    
    def __str__(self):
        return f"Patient {self.user_id} - last prediction on {self.prediction_date} - prediction {self.prediction} "
