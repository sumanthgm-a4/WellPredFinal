from django.urls import path, include
from .views import *

urlpatterns = [
    path(route="", view=render_home, name="homepage"),
    path(route="signup", view=render_register, name="registerpage"),
    path(route="signout", view=render_logout, name="logoutuser"),
    path(route="signin", view=render_login, name="loginuser"),
    path(route="models", view=render_models_page, name="modelspage"),
    
    path(route="stroke/", view=render_stroke, name="strokepage"),
    path(route="stroke/predict", view=render_stroke_predict, name="strokepredict"),
    path(route="stroke/result", view=render_stroke_result, name="strokeresult"),
    path(route="stroke/blog", view=render_stroke_blog, name="strokeblog"),
    path(route="stroke/records", view=render_stroke_records, name="strokerecords"),
    
    path(route="diabetes/", view=render_diabetes, name="diabetespage"),
    path(route="diabetes/predict", view=render_diabetes_predict, name="diabetespredict"),
    path(route="diabetes/result", view=render_diabetes_result, name="diabetesresult"),
    path(route="diabetes/blog", view=render_diabetes_blog, name="diabetesblog"),
    path(route="diabetes/records", view=render_diabetes_records, name="diabetesrecords"),
    
    path(route="depression/", view=render_depression, name="depressionpage"),
    path(route="depression/predict", view=render_depression_predict, name="depressionpredict"),
    path(route="depression/result", view=render_depression_result, name="depressionresult"),
    path(route="depression/blog", view=render_depression_blog, name="depressionblog"),
    path(route="depression/records", view=render_depression_records, name="depressionrecords"),
    
    path(route="contact", view=render_contact, name="contact"),
    path(route="otp", view=render_otp, name="verify_otp"),
]