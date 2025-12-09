# # accounts/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('register/student/', views.StudentRegisterView.as_view(), name='register-student'),
#     path('register/startup/', views.StartupRegisterView.as_view(), name='register-startup'),
#     path('register/commercial/', views.CommercialRegisterView.as_view(), name='register-commercial'),
#     path('login/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('password-reset/', views.PasswordResetRequestView.as_view(), name='password_reset'),
#     path('password-reset-confirm/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
# ]


# accounts/urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path("register/student/", views.StudentRegisterView.as_view(), name="register-student"),
#     path("register/startup/", views.StartupRegisterView.as_view(), name="register-startup"),
#     path("register/commercial/", views.CommercialRegisterView.as_view(), name="register-commercial"),
#     path("login/", views.CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
#     path("password-reset/", views.PasswordResetRequestView.as_view(), name="password_reset"),
#     path("password-reset-confirm/", views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
# ]


from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("register/student/", views.StudentRegisterView.as_view()),
    path("register/startup/", views.StartupRegisterView.as_view()),
    path("register/commercial/", views.CommercialRegisterView.as_view()),

    # NEW LOGIN VIEW (No JWT)
    path("login/", TokenObtainPairView.as_view()),

    # path("password-reset/", views.PasswordResetRequestView.as_view()),
    # path("password-reset-confirm/", views.PasswordResetConfirmView.as_view()),

    path('forgot-password/', views.ForgotPasswordView.as_view(), name='forgot-password'),
    path('forgot-password-confirm/', views.ForgotPasswordConfirmView.as_view(), name='forgot-password-confirm'),

    # path('technology-list/', views.TechnologyList.as_view(), name='technology-list'),
    # path('material-list/', views.MaterialList.as_view(), name='material-list'),
    # path('calculate-price/', views.CalculatePriceView.as_view(), name='calculate-price'),
    # path('stl-upload/', views.STLUploaderView.as_view(), name='stl-upload'),

    # modify 

    path('technology-list/', views.TechnologyList.as_view(), name='technology-list'),
    path('material-list/', views.MaterialList.as_view(), name='material-list'),
    path('stl-upload/', views.STLUploaderView.as_view(), name='stl-upload'),
    path('uploads/', views.UploadedSTLList.as_view(), name='uploaded-list'),
]
