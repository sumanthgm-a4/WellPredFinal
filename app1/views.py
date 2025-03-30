import joblib
from random import randint
import numpy as np
from pathlib import Path
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.utils import IntegrityError
from .models import *


# Get the base directory
BASE_DIR = Path(__file__).resolve().parent.parent


# Create your views here.
def render_home(request):
    
    return render(request, "index.html")


def render_register(request):
    
    if request.method == "POST":
        firstname = request.POST.get("fname")
        lastname = request.POST.get("lname")
        emailid = request.POST.get("email")
        pword = request.POST.get("pword")
        cpword = request.POST.get("cpword")
        print(firstname, lastname, emailid, pword, cpword)
        if User.objects.filter(email=emailid):
            messages.warning(request, "User with the given email already exists.")
            return redirect("registerpage")
        if len(pword) < 8:
            messages.error(request, "Password must be 8 characters long")
            return redirect("registerpage")
        if cpword != pword:
            messages.error(request, "Passwords don't match")
            return redirect("registerpage")
        send_otp(request=request, email=emailid, user_details={
            'fname': firstname,
            'lname': lastname,
            'email': emailid,
            'passw': pword,
        })
        return redirect("verify_otp")
    
    return render(request, "register.html")


def render_login(request):
    
    if request.method == "POST":
        emailid = request.POST.get("email")
        password = request.POST.get("pword")
        
        user = authenticate(request, username=emailid, password=password)
        if user is not None:
            login(request, user)
            # messages.success(request, "Login successful!")
            return redirect('homepage')
        else:
            messages.error(request, "Invalid email or password.")
    
    return render(request, "login.html")


def render_logout(request):
    
    logout(request)
    # messages.success(request, "Successfully logged out")
    return redirect("homepage")


def render_models_page(request):
    
    return render(request, "models.html")


def render_stroke(request):
    
    return render(request, "stroke.html")


@login_required(login_url="loginuser")
def render_stroke_predict(request):
    
    if request.method == "POST":
        age = int(request.POST.get("age"))
        height = float(request.POST.get("height"))
        weight = float(request.POST.get("weight"))
        avg_glucose_level = float(request.POST.get("avg_glucose_level"))
        smoking_status = int(request.POST.get("smoking_status"))
        x = request.POST.get("gender")
        if x is None:
            messages.error(request, "Please select a gender")
            return redirect("strokepredict")
        else:
            gender = int(x)
        hypertension = int(request.POST.get("hypertension"))
        marriage_status = int(request.POST.get("marriage_status"))
        heart_disease = int(request.POST.get("heart_disease"))
        work_type = int(request.POST.get("work_type"))
        residence_type = int(request.POST.get("residence_type"))
        
        bmi = weight / (height ** 2)
        
        values = [gender, age, hypertension, heart_disease, marriage_status, 
                  work_type, residence_type, avg_glucose_level, bmi, smoking_status]
        values_dict = {"gender": gender, "age": age, "hypertension": hypertension,
                       "heart_disease": heart_disease, "marriage_status": marriage_status,
                       "work_type": work_type, "residence_type": residence_type,
                       "avg_glucose_level": avg_glucose_level, "bmi": bmi,
                       "smoking_status": smoking_status}
        print(values_dict)
        
        # Construct paths
        model_path = "app1/Models/stroke_lgbm_model.joblib"
        scaler_path = "app1/Models/stroke_std_scaler.joblib"
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        
        user_input = np.array(values).reshape(1, -1)
        user_input_scaled = scaler.transform(user_input)
        
        prediction = model.predict(user_input_scaled)
        pred_prob = model.predict_proba(user_input_scaled)
        print(f"Prediction: {prediction}")
        print(f"Prediction Prob.: {pred_prob[0][prediction]}")
        
        stroke_record = StrokeRecord.objects.create(
            user_id=request.user,          # Assuming `user` is an instance of User
            gender=gender,        # 1 for Male, 0 for Female
            age=age,              # Integer value
            hypertension=hypertension,  # Boolean (True/False)
            heart_disease=heart_disease,  # Boolean (True/False)
            ever_married=marriage_status,  # Boolean (True/False)
            work_type=work_type,  # Integer based on WORK_TYPE_CHOICES
            residence_type=residence_type,  # Integer based on RESIDENCE_CHOICES
            glucose_level=avg_glucose_level,  # Float value
            bmi=bmi,              # Float value
            smoking_status=smoking_status,  # Integer based on SMOKING_CHOICES
            prediction=prediction  # 1 for Positive, 0 for Negative
        )
        stroke_record.save()
        
        prob = f"{pred_prob[0][prediction][0] * 100: .2f}"
        
        return render(request, "stroke_result.html", context={"prediction": prediction, "prob": prob})
    
    return render(request, "stroke_pred.html")


def render_stroke_result(request):
    
    return render(request=request, template_name="stroke_result.html")


def render_stroke_blog(request):
    
    return render(request, "stroke_blog.html")


@login_required(login_url="loginuser")
def render_stroke_records(request):
    
    if request.user.is_authenticated:
        print("YASSS")
        records = StrokeRecord.objects.filter(user_id=request.user)
    else:
        print("NAURR")
        records = None
    
    return render(request, "stroke_records.html", {"records":records})


def render_diabetes(request):
    
    return render(request, "diabetes.html")


@login_required(login_url="loginuser")
def render_diabetes_predict(request):
        
    if request.method == "POST":
        age = int(request.POST.get("age"))
        height = float(request.POST.get("height"))
        weight = float(request.POST.get("weight"))
        glucose_level = float(request.POST.get("blood_glucose_level"))
        smoking_status = int(request.POST.get("smoking_history"))
        x = request.POST.get("gender")
        if x is None:
            messages.error(request, "Please select a gender")
            return redirect("diabetespredict")
        else:
            gender = int(x)
        hypertension = int(request.POST.get("hypertension"))
        heart_disease = int(request.POST.get("heart_disease"))
        
        bmi = weight / (height ** 2)
        
        values = [gender, age, hypertension, heart_disease, smoking_status, bmi, 
                  glucose_level]
        values_dict = {"gender": gender, "age": age, "hypertension": hypertension,
                       "heart_disease": heart_disease, "smoking_status": smoking_status,
                       "bmi": bmi, "glucose_level": glucose_level}
        print(values_dict)
        
        model_path = "app1/Models/new_diabetes_rf_model.joblib"
        scaler_path = "app1/Models/new_diabetes_scaler.joblib"
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        
        user_input = np.array(values).reshape(1, -1)
        user_input_scaled = scaler.transform(user_input)
        
        pred_prob = model.predict_proba(user_input_scaled)
        # Set a lower threshold for classifying as '1'
        threshold = 0.2  # Experiment with values like 0.4, 0.35, etc.
        prediction = int(pred_prob[0][1] >= threshold)
        print(f"Prediction: {prediction}")
        print(f"Prediction Prob.: {pred_prob[0][prediction]}")
        
        diabetes_record = DiabetesRecord.objects.create(
            user_id=request.user,          # Assuming `user` is an instance of User
            gender=gender,        # 1 for Male, 0 for Female
            age=age,              # Integer value
            hypertension=hypertension,  # Boolean (True/False)
            heart_disease=heart_disease,  # Boolean (True/False)
            smoking_status=smoking_status,  # 1, 3, or 4 based on SMOKING_CHOICES
            bmi=bmi,              # Float value
            glucose_level=glucose_level,  # Float value
            prediction=prediction        # Example: 0 for Negative, 1 for Positive
        )
        diabetes_record.save()

        
        prob = f"{pred_prob[0][prediction] * 100: .2f}"
        
        return render(request, "diabetes_result.html", context={"prediction": prediction, "prob": prob})
    
    return render(request, "diab_pred.html")


def render_diabetes_result(request):
    
    return render(request=request, template_name="diabetes_result.html")


def render_diabetes_blog(request):
    
    return render(request=request, template_name="diab_blog.html")


@login_required(login_url="loginuser")
def render_diabetes_records(request):
    
    if request.user.is_authenticated:
        print("YASSS")
        records = DiabetesRecord.objects.filter(user_id=request.user)
    else:
        print("NAURR")
        records = None
    
    return render(request, "diabetes_records.html", {"records":records})


def render_depression(request):
    
    return render(request, "depression.html")


@login_required(login_url="loginuser")
def render_depression_predict(request):
    
    if request.method == "POST":
        age = int(request.POST.get("age"))
        cgpa = float(request.POST.get("cgpa"))
        sleep = int(request.POST.get("sleep_duration"))
        dietary = int(request.POST.get("dietary_habits"))
        study = int(request.POST.get("study_hours"))
        gender = int(request.POST.get("gender"))
        academic = int(request.POST.get("academic_pressure"))
        stud_sat = int(request.POST.get("study_satisfaction"))
        suicidal = int(request.POST.get("suicidal_thoughts"))
        financial = int(request.POST.get("financial_stress"))
        academic = int(request.POST.get("academic_pressure"))
        family_illness = int(request.POST.get("family_illness"))
        degree = int(request.POST.get("degree"))
        
        values = [gender, age, academic, cgpa, stud_sat, sleep, dietary,
                  degree, suicidal, study, financial, family_illness]
        values_dict = {"Gender": gender, "Age": age, "Academic Pressure": academic,
                       "CGPA": cgpa, "Study Satisfaction": stud_sat, "Sleep": sleep,
                       "Dietary Habits": dietary, "Degree": degree,
                       "Suicidal Thoughts": suicidal,
                       "Study Hours": study, "Financial Stress": financial, 
                       "Family History of Mental Illness": family_illness}
        print(values_dict)
        
        model_path = "app1/Models/depression_lda_model.joblib"
        scaler_path = "app1/Models/depression_std_scaler.joblib"
        model = joblib.load(model_path)
        scaler = joblib.load(scaler_path)
        
        user_input = np.array(values).reshape(1, -1)
        user_input_scaled = scaler.transform(user_input)
        
        prediction = model.predict(user_input_scaled)
        pred_prob = model.predict_proba(user_input_scaled)
        print(f"Prediction: {prediction}")
        print(f"Prediction Prob.: {pred_prob[0][prediction]}")
        
        student_record = DepressionRecord.objects.create(
                            user_id = request.user,
                            gender=gender,
                            academic_pressure=academic,
                            cgpa=cgpa,
                            study_satisf=stud_sat,
                            sleep=sleep,
                            dietary_habits=dietary,
                            degree=degree,
                            suicidal=suicidal,
                            study_hours=study,
                            financial_stress=financial,
                            family_mental_illness=family_illness,
                            prediction=prediction 
                        )
        student_record.save()
        
        prob = f"{pred_prob[0][prediction][0] * 100: .2f}"
        
        return render(request, "depress_result.html", context={"prediction": prediction, "prob": prob})
    
    return render(request=request, template_name="depress_pred.html")


def render_depression_result(request):
    
    return render(request, "depress_result.html")


def render_depression_blog(request):
    
    return render(request, "depress_blog.html")


@login_required(login_url="loginuser")
def render_depression_records(request):
    
    if request.user.is_authenticated:
        print("YASSS")
        records = DepressionRecord.objects.filter(user_id=request.user)
    else:
        print("NAURR")
        records = None
    
    return render(request, "depress_records.html", {"records":records})


def render_contact(request):
    
    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "Please sign in to continue")
            return redirect("loginuser")
        message = request.POST.get("message")
        print(message)
        email = request.user.email
        print(email)
        name = request.user.first_name + " " + request.user.last_name
        send_mail(
            subject=f"Mail from {name}",
            message=message+f"\n\nMail sent by <{email}>",
            from_email=email,
            recipient_list=["214g1a32a4@srit.ac.in"],
            fail_silently=False
        )
        # mail = EmailMessage(subject=f"Message from {name} - {email}",
        #                     body=message, from_email=email,
        #                     to=["gmsumanth93917@gmail.com"])
        # mail.send()
        messages.success(request, "Message sent successfully")
    
    return render(request=request, template_name="contact.html")


def send_otp(request, email, user_details):
    
    otp = str(randint(100000, 999999))
    request.session['otp'] = otp
    request.session['user_details'] = user_details
    send_mail(from_email='sumanthgm12345@gmail.com', 
        subject=f"OTP for {email}", 
        message=otp, 
        recipient_list=[email], 
        fail_silently=False)
    
    return


def render_otp(request):
    
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        if entered_otp is None:
            messages.error(request, 'OTP is required')
            return render(request, "otp.html", {'error': 'OTP is required'})

        if entered_otp == request.session.get('otp'):
            user_details = request.session.get('user_details')
            try:
                user = User.objects.create_user(
                    username=user_details['email'],
                    password=user_details['passw'],
                    email=user_details['email'],
                    first_name=user_details['fname'],
                    last_name=user_details['lname'],
                )
                user.save()
                messages.success(request, 'User registered successfully')
                request.session.clear()
                return redirect("loginuser")
            except IntegrityError:
                return render(request, "otp.html", {'error': 'An error occurred while creating the user'})
        else:
            messages.error(request, 'Invalid OTP')
            return render(request, "otp.html", {'error': 'Invalid OTP'})
    else:
        return render(request, "otp.html")