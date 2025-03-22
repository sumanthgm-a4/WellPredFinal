# Generated by Django 5.1.5 on 2025-02-19 04:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("app1", "0008_remove_diabetesrecord_user_id_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="DepressionRecord",
            fields=[
                ("record_id", models.AutoField(primary_key=True, serialize=False)),
                ("prediction_date", models.DateField(auto_now_add=True)),
                ("gender", models.IntegerField(choices=[(1, "Male"), (0, "Female")])),
                ("academic_pressure", models.IntegerField()),
                ("cgpa", models.FloatField()),
                ("study_satisf", models.IntegerField()),
                (
                    "sleep",
                    models.IntegerField(
                        choices=[
                            (0, "5-6 hours"),
                            (1, "7-8 hours"),
                            (2, "<5 hours"),
                            (3, ">3 hours"),
                        ]
                    ),
                ),
                (
                    "dietary_habits",
                    models.IntegerField(
                        choices=[(0, "Healthy"), (1, "Moderate"), (3, "Unhealthy")]
                    ),
                ),
                (
                    "degree",
                    models.IntegerField(
                        choices=[
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
                    ),
                ),
                ("suicidal", models.BooleanField(default=False)),
                ("study_hours", models.IntegerField()),
                ("financial_stress", models.IntegerField()),
                ("family_mental_illness", models.BooleanField(default=False)),
                (
                    "prediction",
                    models.IntegerField(choices=[(1, "Positive"), (2, "Negative")]),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DiabetesRecord",
            fields=[
                ("record_id", models.AutoField(primary_key=True, serialize=False)),
                ("prediction_date", models.DateField(auto_now_add=True)),
                ("gender", models.IntegerField(choices=[(1, "Male"), (0, "Female")])),
                ("age", models.IntegerField()),
                ("hypertension", models.BooleanField(default=False)),
                ("heart_disease", models.BooleanField(default=False)),
                (
                    "smoking_status",
                    models.IntegerField(
                        choices=[
                            (3, "Former Smoker"),
                            (1, "Current Smoker"),
                            (4, "Never Smoked"),
                        ]
                    ),
                ),
                ("bmi", models.FloatField()),
                ("glucose_level", models.FloatField()),
                (
                    "prediction",
                    models.IntegerField(choices=[(1, "Positive"), (0, "Negative")]),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StrokeRecord",
            fields=[
                ("record_id", models.AutoField(primary_key=True, serialize=False)),
                ("prediction_date", models.DateField(auto_now_add=True)),
                ("gender", models.IntegerField(choices=[(0, "Male"), (1, "Female")])),
                ("age", models.IntegerField()),
                ("hypertension", models.BooleanField(default=False)),
                ("heart_disease", models.BooleanField(default=False)),
                ("ever_married", models.BooleanField(default=False)),
                (
                    "work_type",
                    models.IntegerField(
                        choices=[
                            (0, "Private"),
                            (1, "Self-Employed"),
                            (2, "Looks after children"),
                            (3, "Govt. Job"),
                            (4, "Never Worked"),
                        ]
                    ),
                ),
                (
                    "residence_type",
                    models.IntegerField(choices=[(1, "Urban"), (2, "Rural")]),
                ),
                ("glucose_level", models.FloatField()),
                ("bmi", models.FloatField()),
                (
                    "smoking_status",
                    models.IntegerField(
                        choices=[
                            (1, "Former Smoker"),
                            (2, "Current Smoker"),
                            (0, "Never Smoked"),
                        ]
                    ),
                ),
                (
                    "prediction",
                    models.IntegerField(choices=[(1, "Positive"), (2, "Negative")]),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
