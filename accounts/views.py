# # accounts/views.py
# from django.contrib.auth import get_user_model
# from rest_framework import generics, status
# from rest_framework.response import Response
# from .serializers import (
#     StudentRegisterSerializer, StartupRegisterSerializer, CommercialRegisterSerializer
# )
# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# from django.contrib.auth.tokens import default_token_generator
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes, force_str
# from django.template.loader import render_to_string
# from django.core.mail import send_mail

# from django.conf import settings

# User = get_user_model()

# # JWT login view
# # class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
# #     @classmethod
# #     def get_token(cls, user):
# #         token = super().get_token(user)
# #         token['email'] = user.email
# #         token['user_type'] = user.user_type
# #         return token


# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

#     def validate(self, attrs):
#         data = super().validate(attrs)

#         # Add custom fields to response
#         data = {
#             "status": True,
#             "message": "Login successful",
#             "user": {
#                 "id": self.user.id,
#                 "email": self.user.email,
#                 "user_type": self.user.user_type,
#             },
#             "tokens": {
#                 "refresh": data["refresh"],
#                 "access": data["access"]
#             }
#         }
#         return data

#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         token['email'] = user.email
#         token['user_type'] = user.user_type
#         return token


# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer

# # Student register
# class StudentRegisterView(generics.CreateAPIView):
#     serializer_class = StudentRegisterSerializer
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         # Return JWT tokens after registration
#         token_serializer = CustomTokenObtainPairSerializer(data={'email': user.email, 'password': request.data.get('password')})
#         token_serializer.is_valid(raise_exception=True)
#         return Response(token_serializer.validated_data, status=status.HTTP_201_CREATED)

# # Startup register
# class StartupRegisterView(generics.CreateAPIView):
#     serializer_class = StartupRegisterSerializer
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         token_serializer = CustomTokenObtainPairSerializer(data={'email': user.email, 'password': request.data.get('password')})
#         token_serializer.is_valid(raise_exception=True)
#         return Response(token_serializer.validated_data, status=status.HTTP_201_CREATED)

# # Commercial register
# class CommercialRegisterView(generics.CreateAPIView):
#     serializer_class = CommercialRegisterSerializer
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         token_serializer = CustomTokenObtainPairSerializer(data={'email': user.email, 'password': request.data.get('password')})
#         token_serializer.is_valid(raise_exception=True)
#         return Response(token_serializer.validated_data, status=status.HTTP_201_CREATED)

# # Password reset request view
# from rest_framework.views import APIView
# class PasswordResetRequestView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         if not email:
#             return Response({"detail": "Email is required."}, status=400)
#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             # Security: do not reveal that email doesn't exist. Return 200.
#             return Response({"detail": "If that email exists, a password reset link has been sent."})
#         uid = urlsafe_base64_encode(force_bytes(user.pk))
#         token = default_token_generator.make_token(user)
#         reset_link = f"{request.build_absolute_uri('/')}api/auth/password-reset-confirm/?uid={uid}&token={token}"
#         # Option: use a template; here we send a simple email
#         subject = "Password Reset for Navkalpit"
#         message = f"Use the following link to reset your password:\n\n{reset_link}\n\nIf you did not request this, ignore."
#         send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
#         return Response({"detail": "If that email exists, a password reset link has been sent."})

# # Password reset confirm view
# class PasswordResetConfirmView(APIView):
#     def post(self, request):
#         uid = request.data.get('uid')
#         token = request.data.get('token')
#         new_password = request.data.get('new_password')
#         if not uid or not token or not new_password:
#             return Response({"detail": "uid, token and new_password are required."}, status=400)
#         try:
#             uid_decoded = force_str(urlsafe_base64_decode(uid))
#             user = User.objects.get(pk=uid_decoded)
#         except Exception:
#             return Response({"detail": "Invalid uid."}, status=400)
#         if not default_token_generator.check_token(user, token):
#             return Response({"detail": "Invalid or expired token."}, status=400)
#         try:
#             from django.contrib.auth.password_validation import validate_password
#             validate_password(new_password, user)
#         except Exception as e:
#             return Response({"detail": str(e)}, status=400)
#         user.set_password(new_password)
#         user.save()
#         return Response({"detail": "Password has been reset successfully."})


# accounts/views.py
# from django.contrib.auth import get_user_model
# from rest_framework import generics, status
# from rest_framework.response import Response
# from .serializers import (
#     StudentRegisterSerializer, StartupRegisterSerializer, CommercialRegisterSerializer
# )
# from rest_framework_simplejwt.views import TokenObtainPairView
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# from rest_framework.views import APIView
# from django.contrib.auth.tokens import default_token_generator
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes, force_str
# from django.core.mail import send_mail
# from django.conf import settings
# from django.contrib.auth.password_validation import validate_password

# User = get_user_model()

# # Custom JWT serializer to include email and user_type in token if desired
# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)
#         # add custom claims
#         token["email"] = user.email
#         token["user_type"] = user.user_type
#         return token

# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer


# class StudentRegisterView(generics.CreateAPIView):
#     serializer_class = StudentRegisterSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         # return JWT tokens
#         token_serializer = CustomTokenObtainPairSerializer(data={
#             "email": user.email,
#             "password": request.data.get("password")
#         })
#         token_serializer.is_valid(raise_exception=True)
#         return Response(token_serializer.validated_data, status=status.HTTP_201_CREATED)


# class StartupRegisterView(generics.CreateAPIView):
#     serializer_class = StartupRegisterSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         token_serializer = CustomTokenObtainPairSerializer(data={
#             "email": user.email,
#             "password": request.data.get("password")
#         })
#         token_serializer.is_valid(raise_exception=True)
#         return Response(token_serializer.validated_data, status=status.HTTP_201_CREATED)


# class CommercialRegisterView(generics.CreateAPIView):
#     serializer_class = CommercialRegisterSerializer

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         token_serializer = CustomTokenObtainPairSerializer(data={
#             "email": user.email,
#             "password": request.data.get("password")
#         })
#         token_serializer.is_valid(raise_exception=True)
#         return Response(token_serializer.validated_data, status=status.HTTP_201_CREATED)


# class PasswordResetRequestView(APIView):
#     """
#     POST { "email": "user@example.com" }
#     Sends password reset link to email (console in dev).
#     """
#     def post(self, request):
#         email = request.data.get("email")
#         if not email:
#             return Response({"detail": "Email is required."}, status=status.HTTP_400_BAD_REQUEST)
#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             # security: don't reveal whether email exists
#             return Response({"detail": "If that email exists, a password reset link has been sent."})
#         uid = urlsafe_base64_encode(force_bytes(user.pk))
#         token = default_token_generator.make_token(user)
#         # Build a link appropriate for your front-end to consume:
#         reset_link = f"{request.build_absolute_uri('/')}api/auth/password-reset-confirm/?uid={uid}&token={token}"
#         subject = "Navkalpit - Password Reset"
#         message = f"Use this link to reset your password:\n\n{reset_link}\n\nIf you didn't request this, ignore."
#         send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
#         return Response({"detail": "If that email exists, a password reset link has been sent."})


# class PasswordResetConfirmView(APIView):
#     """
#     POST { "uid": "<uid>", "token": "<token>", "new_password": "..." }
#     """
#     def post(self, request):
#         uid = request.data.get("uid")
#         token = request.data.get("token")
#         new_password = request.data.get("new_password")
#         if not uid or not token or not new_password:
#             return Response({"detail": "uid, token and new_password are required."}, status=status.HTTP_400_BAD_REQUEST)
#         try:
#             uid_decoded = force_str(urlsafe_base64_decode(uid))
#             user = User.objects.get(pk=uid_decoded)
#         except Exception:
#             return Response({"detail": "Invalid uid."}, status=status.HTTP_400_BAD_REQUEST)
#         if not default_token_generator.check_token(user, token):
#             return Response({"detail": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)
#         try:
#             validate_password(new_password, user)
#         except Exception as e:
#             return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
#         user.set_password(new_password)
#         user.save()
#         return Response({"detail": "Password has been reset successfully."})


# from django.contrib.auth import authenticate, get_user_model
# from rest_framework import generics, status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes, force_str


# from .serializers import (
#     StudentRegisterSerializer,
#     StartupRegisterSerializer,
#     CommercialRegisterSerializer
# )



from decimal import Decimal
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import (
    CustomTokenObtainPairSerializer, StudentRegisterSerializer, StartupRegisterSerializer, CommercialRegisterSerializer, TechnologySerializer, TierSerializer, MaterialPriceSerializer, MaterialSerializer
)
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


# REQUIRED imports ↓↓↓
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.contrib.auth.password_validation import validate_password
from django.conf import settings
from django.contrib.auth import authenticate 
from .models import Material, MaterialPrice, Technology, Tier, Color, UploadedSTL
from .serializers import TechnologySerializer, TierSerializer, MaterialPriceSerializer, MaterialSerializer, UploadedSTLSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


User = get_user_model()

# ---------------------------
# Login View (NO TOKEN RETURN)
# ---------------------------
# class LoginView(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')

#         user = authenticate(email=email, password=password)

#         if user is not None:
#             return Response(
#                 {"message": "Login successful"},
#                 status=status.HTTP_200_OK
#             )
#         return Response(
#             {"message": "Invalid email or password"},
#             status=status.HTTP_400_BAD_REQUEST
#         )


class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({"detail": "Email and password are required."},
                            status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, email=email, password=password)

        if user is None:
            return Response({"detail": "Invalid email or password."},
                            status=status.HTTP_401_UNAUTHORIZED)

        token_serializer = CustomTokenObtainPairSerializer(data={
            "email": email,
            "password": password
        })
        token_serializer.is_valid(raise_exception=True)

        return Response(token_serializer.validated_data, status=status.HTTP_200_OK)

# ---------------------------
# Student Register
# ---------------------------
class StudentRegisterView(generics.CreateAPIView):
    serializer_class = StudentRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"message": "Student registered successfully"},
            status=status.HTTP_201_CREATED
        )


# ---------------------------
# Startup Register
# ---------------------------
class StartupRegisterView(generics.CreateAPIView):
    serializer_class = StartupRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"message": "Startup registered successfully"},
            status=status.HTTP_201_CREATED
        )


# ---------------------------
# Commercial Register
# ---------------------------
class CommercialRegisterView(generics.CreateAPIView):
    serializer_class = CommercialRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {"message": "Commercial registered successfully"},
            status=status.HTTP_201_CREATED
        )


# # ---------------------------
# # Password Reset Request
# # ---------------------------
# class PasswordResetRequestView(APIView):
#     def post(self, request):
#         email = request.data.get("email")

#         if not email:
#             return Response({"message": "Email is required"}, status=400)

#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             return Response({"message": "If email exists, reset link sent"})

#         # Create reset link (console email backend)
#         from django.contrib.auth.tokens import default_token_generator
#         from django.utils.http import urlsafe_base64_encode
#         from django.utils.encoding import force_bytes
#         from django.core.mail import send_mail
#         from django.conf import settings

#         uid = urlsafe_base64_encode(force_bytes(user.pk))
#         token = default_token_generator.make_token(user)

#         link = f"{request.build_absolute_uri('/')}api/auth/password-reset-confirm/?uid={uid}&token={token}"

#         send_mail(
#             "Password Reset",
#             f"Use this link to reset your password:\n{link}",
#             settings.DEFAULT_FROM_EMAIL,
#             [email],
#         )

#         return Response({"message": "If email exists, reset link sent"})


# # ---------------------------
# # Password Reset Confirm
# # ---------------------------
# class PasswordResetConfirmView(APIView):
#     def post(self, request):
#         uid = request.data.get("uid")
#         token = request.data.get("token")
#         new_password = request.data.get("new_password")

#         from django.contrib.auth.tokens import default_token_generator
#         from django.utils.http import urlsafe_base64_decode
#         from django.utils.encoding import force_str
#         from django.contrib.auth.password_validation import validate_password

#         if not uid or not token or not new_password:
#             return Response({"message": "Missing required fields"}, status=400)

#         try:
#             user_id = force_str(urlsafe_base64_decode(uid))
#             user = User.objects.get(pk=user_id)
#         except:
#             return Response({"message": "Invalid UID"}, status=400)

#         if not default_token_generator.check_token(user, token):
#             return Response({"message": "Invalid or expired token"}, status=400)

#         validate_password(new_password)
#         user.set_password(new_password)
#         user.save()

#         return Response({"message": "Password updated successfully"})


# Forgot password: send link with uid and token
class ForgotPasswordView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({"detail": "Email is required."}, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            # don't reveal whether email exists
            return Response({"detail": "If that email exists, a password reset link has been sent."}, status=status.HTTP_200_OK)

        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = default_token_generator.make_token(user)

        # Build reset link. For dev, this points to the API confirm endpoint or a front-end page.
        # Example link to a frontend page: https://yourfrontend/reset-password/?uid=...&token=...
        # For SPA-less dev testing we provide an API-friendly link:
        reset_link = f"{request.build_absolute_uri('/')}api/auth/forgot-password-confirm/?uid={uid}&token={token}"

        subject = "Navkalpit: Password reset"
        message = f"Hello,\n\nUse the link below to reset your password:\n\n{reset_link}\n\nThis link is for one-time use and will expire.\nIf you did not request this, please ignore."
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

        return Response({"detail": "If that email exists, a password reset link has been sent."}, status=status.HTTP_200_OK)

# Forgot password confirm: client POSTs uid, token, new_password
# class ForgotPasswordConfirmView(APIView):
#     def post(self, request):
#         uid = request.data.get('uid')
#         token = request.data.get('token')
#         new_password = request.data.get('new_password')

#         if not uid or not token or not new_password:
#             return Response({"detail": "uid, token and new_password are required."}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             uid_decoded = force_str(urlsafe_base64_decode(uid))
#             user = User.objects.get(pk=uid_decoded)
#         except Exception:
#             return Response({"detail": "Invalid uid."}, status=status.HTTP_400_BAD_REQUEST)

#         if not default_token_generator.check_token(user, token):
#             return Response({"detail": "Invalid or expired token."}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             validate_password(new_password, user)
#         except Exception as e:
#             return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

#         user.set_password(new_password)
#         user.save()
#         return Response({"detail": "Password has been reset successfully."}, status=status.HTTP_200_OK)


# class ForgotPasswordConfirmView(APIView):
#     def post(self, request):
#         uid = request.data.get("uid")
#         token = request.data.get("token")
#         new_password = request.data.get("new_password")

#         if not uid or not token or not new_password:
#             return Response({"detail": "uid, token and new_password are required."}, status=400)

#         # Decode UID
#         try:
#             uid_decoded = force_str(urlsafe_base64_decode(uid))
#             user = User.objects.get(pk=uid_decoded)
#         except Exception:
#             return Response({"detail": "Invalid uid."}, status=400)

#         # Validate token
#         if not default_token_generator.check_token(user, token):
#             return Response({"detail": "Invalid or expired token."}, status=400)

#         # Validate password
#         try:
#             validate_password(new_password, user)
#         except Exception as e:
#             return Response({"detail": str(e)}, status=400)

#         user.set_password(new_password)
#         user.save()

#         return Response({"detail": "Password has been reset successfully."})


class ForgotPasswordConfirmView(APIView):
    def post(self, request):
        uid = request.data.get("uid")
        token = request.data.get("token")
        new_password = request.data.get("new_password")

        if not uid or not token or not new_password:
            return Response({"detail": "uid, token and new_password are required."}, status=400)

        # Decode UID
        try:
            uid_decoded = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=uid_decoded)
        except Exception as e:
            return Response({"detail": "Invalid uid", "error": str(e)}, status=400)

        # DEBUG — print values
        print("DEBUG UID:", uid)
        print("DEBUG decoded UID:", uid_decoded)
        print("DEBUG token:", token)

        # Check token
        is_valid = default_token_generator.check_token(user, token)
        print("DEBUG token valid status:", is_valid)

        if not is_valid:
            return Response({"detail": "Invalid or expired token."}, status=400)

        # Validate password
        try:
            validate_password(new_password, user)
        except Exception as e:
            return Response({"detail": str(e)}, status=400)

        user.set_password(new_password)
        user.save()

        return Response({"detail": "Password has been reset successfully."})


# pricing and quotations 

# List techs
# class TechnologyList(generics.ListAPIView):
#     queryset = Technology.objects.all()
#     serializer_class = TechnologySerializer

# # List materials for a technology (with prices)
# class MaterialList(APIView):
#     def get(self, request):
#         tech_slug = request.query_params.get("technology")
#         tier_slug = request.query_params.get("tier")  # optional: filter to a tier
#         if not tech_slug:
#             return Response({"detail": "technology query param required (e.g. FDM or STL)"}, status=400)
#         tech = get_object_or_404(Technology, slug=tech_slug)
#         materials = Material.objects.filter(technology=tech).prefetch_related("prices__tier")
#         data = []
#         for m in materials:
#             # if tier provided, return single price for that tier
#             if tier_slug:
#                 try:
#                     mp = m.prices.get(tier__slug=tier_slug)
#                     price_obj = {
#                         "tier": {"slug": mp.tier.slug, "name": mp.tier.name},
#                         "price_per_gram": mp.price_per_gram
#                     }
#                     mdata = {
#                         "id": m.id,
#                         "name": m.name,
#                         "density_g_per_cm3": m.density_g_per_cm3,
#                         "price": price_obj
#                     }
#                 except MaterialPrice.DoesNotExist:
#                     mdata = {
#                         "id": m.id,
#                         "name": m.name,
#                         "density_g_per_cm3": m.density_g_per_cm3,
#                         "price": None
#                     }
#             else:
#                 # return all prices
#                 prices = []
#                 for mp in m.prices.all():
#                     prices.append({
#                         "tier": {"slug": mp.tier.slug, "name": mp.tier.name},
#                         "price_per_gram": mp.price_per_gram
#                     })
#                 mdata = {
#                     "id": m.id,
#                     "name": m.name,
#                     "density_g_per_cm3": m.density_g_per_cm3,
#                     "prices": prices
#                 }
#             data.append(mdata)
#         return Response(data)

# # Calculate price endpoint
# class CalculatePriceView(APIView):
#     """
#     POST body:
#     {
#       "material_id": 1,
#       "tier": "student",
#       "weight_grams": 25.3,   # OR volume_cm3: 10.2
#       "gst_percent": 18   # optional, default 18
#     }
#     """
#     def post(self, request):
#         material_id = request.data.get("material_id")
#         tier_slug = request.data.get("tier")
#         weight = request.data.get("weight_grams")
#         volume_cm3 = request.data.get("volume_cm3")
#         gst_percent = Decimal(request.data.get("gst_percent", 18))

#         if not material_id or not tier_slug:
#             return Response({"detail":"material_id and tier are required"}, status=400)
#         material = get_object_or_404(Material, pk=material_id)
#         tier = get_object_or_404(Tier, slug=tier_slug)
#         try:
#             mp = MaterialPrice.objects.get(material=material, tier=tier)
#         except MaterialPrice.DoesNotExist:
#             return Response({"detail":"No price defined for this material & tier"}, status=400)

#         price_per_gram = Decimal(mp.price_per_gram)
#         # calculate weight either from given weight or from volume & density
#         if weight is None:
#             if volume_cm3 is None:
#                 return Response({"detail":"Either weight_grams or volume_cm3 required"}, status=400)
#             if not material.density_g_per_cm3:
#                 return Response({"detail":"Material density not set, cannot compute weight from volume"}, status=400)
#             weight = Decimal(volume_cm3) * Decimal(material.density_g_per_cm3)
#         else:
#             weight = Decimal(str(weight))

#         material_cost = (price_per_gram * weight).quantize(Decimal("0.01"))
#         gst_value = (material_cost * gst_percent / Decimal(100)).quantize(Decimal("0.01"))
#         total = (material_cost + gst_value).quantize(Decimal("0.01"))

#         return Response({
#             "material_id": material.id,
#             "material_name": material.name,
#             "tier": tier.slug,
#             "weight_grams": float(weight),
#             "price_per_gram": float(price_per_gram),
#             "material_cost": float(material_cost),
#             "gst_percent": float(gst_percent),
#             "gst_value": float(gst_value),
#             "total_price": float(total)
#         })

# # STL upload & calculate (requires trimesh)
# import tempfile
# import os

# class STLUploaderView(APIView):
#     """
#     multipart-form:
#     file: STL file
#     material_id, tier, gst_percent(optional)
#     """
#     def post(self, request):
#         f = request.FILES.get("file")
#         material_id = request.POST.get("material_id")
#         tier_slug = request.POST.get("tier")
#         gst_percent = Decimal(request.POST.get("gst_percent", 18))

#         if not f or not material_id or not tier_slug:
#             return Response({"detail":"file, material_id and tier required"}, status=400)

#         material = get_object_or_404(Material, pk=material_id)
#         tier = get_object_or_404(Tier, slug=tier_slug)
#         try:
#             mp = MaterialPrice.objects.get(material=material, tier=tier)
#         except MaterialPrice.DoesNotExist:
#             return Response({"detail":"No price defined for this material & tier"}, status=400)

#         # save to temp file
#         tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".stl")
#         try:
#             for chunk in f.chunks():
#                 tmp.write(chunk)
#             tmp.flush()
#             tmp.close()
#             # compute volume using trimesh
#             try:
#                 import trimesh
#                 mesh = trimesh.load(tmp.name, force='mesh')
#                 # volume in cubic units; assume STL units are mm -> convert to cm^3
#                 # common case: many STLs are in mm units; trimesh volume will be in mm^3 -> convert
#                 volume_mm3 = mesh.volume
#                 if volume_mm3 is None:
#                     return Response({"detail":"Could not compute volume from STL"}, status=400)
#                 # mm^3 to cm^3: divide by 1000
#                 volume_cm3 = volume_mm3 / 1000.0
#             except Exception as e:
#                 return Response({"detail": f"Error processing STL: {str(e)}"}, status=400)

#             if not material.density_g_per_cm3:
#                 return Response({"detail":"Material density not set, cannot compute weight"}, status=400)

#             weight_grams = Decimal(volume_cm3) * Decimal(material.density_g_per_cm3)
#             price_per_gram = Decimal(mp.price_per_gram)
#             material_cost = (price_per_gram * weight_grams).quantize(Decimal("0.01"))
#             gst_value = (material_cost * gst_percent / Decimal(100)).quantize(Decimal("0.01"))
#             total = (material_cost + gst_value).quantize(Decimal("0.01"))

#             return Response({
#                 "weight_grams": float(weight_grams),
#                 "volume_cm3": float(volume_cm3),
#                 "material_cost": float(material_cost),
#                 "gst_value": float(gst_value),
#                 "total_price": float(total),
#                 "material_name": material.name,
#                 "tier": tier.slug
#             })
#         finally:
#             try:
#                 os.unlink(tmp.name)
#             except Exception:
#                 pass


# modify quotations 


# # Technology list (existing)
# class TechnologyList(generics.ListAPIView):
#     queryset = Technology.objects.all()
#     serializer_class = TechnologySerializer

# # Material list (existing, updated)
# class MaterialList(APIView):
#     def get(self, request):
#         tech_slug = request.query_params.get("technology")
#         tier_slug = request.query_params.get("tier")
#         if not tech_slug:
#             return Response({"detail":"technology query param required"}, status=400)
#         tech = get_object_or_404(Technology, slug=tech_slug)
#         materials = Material.objects.filter(technology=tech).prefetch_related("prices__tier")
#         data = []
#         for m in materials:
#             if tier_slug:
#                 try:
#                     mp = m.prices.get(tier__slug=tier_slug)
#                     price_obj = {"tier":{"slug":mp.tier.slug,"name":mp.tier.name},"price_per_gram":mp.price_per_gram}
#                     mdata = {"id":m.id,"name":m.name,"density_g_per_cm3":m.density_g_per_cm3,"price":price_obj}
#                 except MaterialPrice.DoesNotExist:
#                     mdata = {"id":m.id,"name":m.name,"density_g_per_cm3":m.density_g_per_cm3,"price":None}
#             else:
#                 prices = []
#                 for mp in m.prices.all():
#                     prices.append({"tier":{"slug":mp.tier.slug,"name":mp.tier.name},"price_per_gram":mp.price_per_gram})
#                 mdata = {"id":m.id,"name":m.name,"density_g_per_cm3":m.density_g_per_cm3,"prices":prices}
#             data.append(mdata)
#         return Response(data)

# # Upload endpoint — saves file to UploadedSTL model and returns result
# class STLUploaderView(views.APIView):
#     """
#     POST multipart/form-data:
#     - file: file
#     - technology (slug)
#     - material_id
#     - tier (slug)
#     - color_id (optional)
#     - gst_percent (optional)
#     """
#     def post(self, request):
#         f = request.FILES.get("file")
#         tech_slug = request.POST.get("technology")
#         material_id = request.POST.get("material_id")
#         tier_slug = request.POST.get("tier")
#         color_id = request.POST.get("color_id", None)
#         gst_percent = Decimal(request.POST.get("gst_percent", 18))

#         if not f or not tech_slug or not material_id or not tier_slug:
#             return Response({"detail":"file, technology, material_id and tier required"}, status=400)

#         tech = get_object_or_404(Technology, slug=tech_slug)
#         material = get_object_or_404(Material, pk=material_id)
#         tier = get_object_or_404(Tier, slug=tier_slug)
#         color = None
#         if color_id:
#             color = get_object_or_404(Color, pk=color_id)

#         # create record first to save file via FileField
#         upload = UploadedSTL.objects.create(
#             file=f,
#             technology=tech,
#             material=material,
#             tier=tier,
#             color=color,
#             gst_percent=gst_percent
#         )

#         # compute volume using trimesh from saved file path
#         try:
#             import trimesh
#             # path of saved file
#             file_path = upload.file.path
#             mesh = trimesh.load(file_path, force='mesh')
#             volume = mesh.volume  # units^3 (depends on STL units)
#             if volume is None:
#                 raise ValueError("Could not compute volume from file")
#             # assume STL units are mm -> convert mm^3 to cm^3 by /1000
#             volume_cm3 = volume / 1000.0
#         except Exception as e:
#             # cleanup upload if you like or keep file for debugging
#             upload.delete()
#             return Response({"detail":f"Error processing file: {str(e)}"}, status=400)

#         if not material.density_g_per_cm3:
#             upload.delete()
#             return Response({"detail":"Material density not set (density_g_per_cm3)."}, status=400)

#         weight_grams = Decimal(volume_cm3) * Decimal(material.density_g_per_cm3)
#         try:
#             mp = MaterialPrice.objects.get(material=material, tier=tier)
#         except MaterialPrice.DoesNotExist:
#             upload.delete()
#             return Response({"detail":"No price defined for this material & tier"}, status=400)

#         price_per_gram = Decimal(mp.price_per_gram)
#         material_cost = (price_per_gram * weight_grams).quantize(Decimal("0.01"))
#         gst_value = (material_cost * gst_percent / Decimal(100)).quantize(Decimal("0.01"))
#         total = (material_cost + gst_value).quantize(Decimal("0.01"))

#         # update upload record
#         upload.volume_cm3 = float(volume_cm3)
#         upload.weight_grams = float(weight_grams)
#         upload.price_per_gram = price_per_gram
#         upload.material_cost = material_cost
#         upload.gst_value = gst_value
#         upload.total_price = total
#         upload.save()

#         serializer = UploadedSTLSerializer(upload, context={"request": request})
#         return Response(serializer.data, status=201)

# # Download / List uploaded files
# class UploadedSTLList(generics.ListAPIView):
#     queryset = UploadedSTL.objects.all().order_by("-uploaded_at")
#     serializer_class = UploadedSTLSerializer



# Create + list technologies
class TechnologyList(generics.ListCreateAPIView):
    queryset = Technology.objects.all()
    serializer_class = TechnologySerializer

# List materials (optionally filter by technology) and create material
class MaterialList(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        tech_slug = self.request.query_params.get("technology")
        if tech_slug:
            return qs.filter(technology__slug=tech_slug)
        return qs

# STL upload endpoint - improved: infers technology if not provided, accepts tier_id or tier slug
class STLUploaderView(APIView):
    def post(self, request):
        f = request.FILES.get("file")
        material_id = request.POST.get("material_id")
        tier_id = request.POST.get("tier_id")      # accepts numeric id
        tier_slug = request.POST.get("tier")       # or slug
        gst_percent = Decimal(request.POST.get("gst_percent", 18))
        color_id = request.POST.get("color_id", None)

        # Basic checks
        if not f or not material_id or (not tier_id and not tier_slug):
            return Response({"detail":"file, material_id and tier required"}, status=400)

        # Validate file extension - require .stl
        filename = f.name.lower()
        if not filename.endswith(".stl"):
            return Response({"detail":"Uploaded file must be a .stl file"}, status=400)

        # lookup material
        material = get_object_or_404(Material, pk=material_id)

        # lookup tier by id or slug
        if tier_id:
            tier = get_object_or_404(Tier, pk=tier_id)
        else:
            tier = get_object_or_404(Tier, slug=tier_slug)

        color = None
        if color_id:
            color = get_object_or_404(Color, pk=color_id)

        # create UploadedSTL record (FileField will save file to MEDIA_ROOT)
        upload = UploadedSTL.objects.create(
            file=f,
            technology=material.technology,  # infer technology from material
            material=material,
            tier=tier,
            color=color,
            gst_percent=gst_percent
        )

        # compute volume using trimesh
        try:
            import trimesh
            file_path = upload.file.path
            mesh = trimesh.load(file_path, force='mesh')
            volume = mesh.volume
            if volume is None:
                upload.delete()
                return Response({"detail":"Could not compute volume from STL"}, status=400)
            # assume STL units are mm -> convert mm^3 to cm^3
            volume_cm3 = volume / 1000.0
        except Exception as e:
            upload.delete()
            return Response({"detail":f"Error processing STL: {str(e)}"}, status=400)

        # density required to compute weight
        if not material.density_g_per_cm3:
            upload.delete()
            return Response({"detail":"Material density not set (density_g_per_cm3)."}, status=400)

        weight_grams = Decimal(volume_cm3) * Decimal(material.density_g_per_cm3)

        # get material price for this tier
        try:
            mp = MaterialPrice.objects.get(material=material, tier=tier)
        except MaterialPrice.DoesNotExist:
            upload.delete()
            return Response({"detail":"No price defined for this material & tier"}, status=400)

        price_per_gram = Decimal(mp.price_per_gram)
        material_cost = (price_per_gram * weight_grams).quantize(Decimal("0.01"))
        gst_value = (material_cost * gst_percent / Decimal(100)).quantize(Decimal("0.01"))
        total = (material_cost + gst_value).quantize(Decimal("0.01"))

        # update
        upload.volume_cm3 = float(volume_cm3)
        upload.weight_grams = float(weight_grams)
        upload.price_per_gram = float(price_per_gram)
        upload.material_cost = float(material_cost)
        upload.gst_value = float(gst_value)
        upload.total_price = float(total)
        upload.save()

        serializer = UploadedSTLSerializer(upload, context={"request": request})
        return Response(serializer.data, status=201)

# list uploads
class UploadedSTLList(generics.ListAPIView):
    queryset = UploadedSTL.objects.all().order_by("-uploaded_at")
    serializer_class = UploadedSTLSerializer
