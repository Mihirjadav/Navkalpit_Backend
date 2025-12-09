# # accounts/models.py
# from django.db import models
# from django.contrib.auth.models import AbstractUser
# from django.utils.translation import gettext_lazy as _

# class User(AbstractUser):
#     USER_TYPE_CHOICES = (
#         ('student', 'Student'),
#         ('startup', 'Startup'),
#         ('commercial', 'Commercial'),
#     )
#     username = None
#     email = models.EmailField(_('email address'), unique=True)
#     user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return f"{self.email} ({self.user_type})"

# # StudentProfile (fields exactly from your txt)
# class StudentProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
#     full_name = models.CharField(max_length=255)
#     country = models.CharField(max_length=255, blank=True)
#     state = models.CharField(max_length=255, blank=True)
#     city = models.CharField(max_length=255, blank=True)
#     university_name = models.CharField(max_length=255, blank=True)
#     department = models.CharField(max_length=255, blank=True)
#     course = models.CharField(max_length=255, blank=True)
#     semester = models.CharField(max_length=100, blank=True)
#     end_of_semester = models.CharField(max_length=100, blank=True)
#     aadhar_number = models.CharField(max_length=50, blank=True)
#     address = models.TextField(blank=True)  # Address (Aadhar Card Based)
#     mobile_number = models.CharField(max_length=50, blank=True)
#     enrollment_no = models.CharField(max_length=100, blank=True)
#     collage_idcard = models.CharField(max_length=255, blank=True)

#     def __str__(self):
#         return f"StudentProfile: {self.user.email}"

# # StartupProfile
# class StartupProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='startup_profile')
#     company_name = models.CharField(max_length=255)
#     owner_name = models.CharField(max_length=255, blank=True)
#     company_mobile_number = models.CharField(max_length=50, blank=True)
#     # dp_certificate_no = models.CharField(max_length=255, blank=True)
#     # udyam_certificate_no = models.CharField(max_length=255, blank=True)
#     dp_id_certificate = models.BooleanField(default=False)
#     dp_certificate_no = models.CharField(max_length=255, blank=True)

#     udyam_certificate = models.BooleanField(default=False)
#     udyam_certificate_no = models.CharField(max_length=255, blank=True)

#     company_type = models.CharField(max_length=255, blank=True)        # like private limited, LLP,etc
#     owner_aadhar_card = models.CharField(max_length=255, blank=True)
#     gst_number = models.CharField(max_length=255, blank=True)
#     company_description = models.TextField(blank=True)  # up to 200 words (no hard limit here)

#     def __str__(self):
#         return f"StartupProfile: {self.user.email}"

# # CommercialProfile
# class CommercialProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='commercial_profile')
#     company_name = models.CharField(max_length=255)
#     gst_number = models.CharField(max_length=255, blank=True)
#     company_type = models.CharField(max_length=255, blank=True)
#     business_type = models.CharField(max_length=255, blank=True)  # like scale: small/medium/retail
#     company_mobile_number = models.CharField(max_length=50, blank=True)
#     aadhar_number = models.CharField(max_length=255, blank=True)
#     company_address = models.TextField(blank=True)

#     def __str__(self):
#         return f"CommercialProfile: {self.user.email}"



# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ("student", "Student"),
        ("startup", "Startup"),
        ("commercial", "Commercial"),
    )

    username = None
    email = models.EmailField(_("email address"), unique=True)
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email} ({self.user_type})"


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile")
    full_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    university_name = models.CharField(max_length=255, blank=True)
    department = models.CharField(max_length=255, blank=True)
    course = models.CharField(max_length=255, blank=True)
    semester = models.CharField(max_length=100, blank=True)
    end_of_semester = models.CharField(max_length=100, blank=True)
    aadhar_number = models.CharField(max_length=50, blank=True)
    address = models.TextField(blank=True)  # Address (Aadhar Card Based)
    mobile_number = models.CharField(max_length=50, blank=True)
    enrollment_no = models.CharField(max_length=100, blank=True)
    collage_idcard = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"StudentProfile: {self.user.email}"


class StartupProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="startup_profile")
    company_name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255, blank=True)
    company_mobile_number = models.CharField(max_length=50, blank=True)
    # dp_id_certificate = models.CharField(max_length=255, blank=True)   # Yes/No or id
    # udyam_certificate = models.CharField(max_length=255, blank=True)   # Yes/No or id
    dp_id_certificate = models.BooleanField(default=False)
    dp_certificate_no = models.CharField(max_length=255, blank=True)

    udyam_certificate = models.BooleanField(default=False)
    udyam_certificate_no = models.CharField(max_length=255, blank=True)

    company_type = models.CharField(max_length=255, blank=True)
    owner_aadhar_card = models.CharField(max_length=255, blank=True)
    gst_number = models.CharField(max_length=255, blank=True)
    company_description = models.TextField(blank=True)

    def __str__(self):
        return f"StartupProfile: {self.user.email}"


class CommercialProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="commercial_profile")
    company_name = models.CharField(max_length=255)
    gst_number = models.CharField(max_length=255, blank=True)
    company_type = models.CharField(max_length=255, blank=True)
    business_type = models.CharField(max_length=255, blank=True)
    company_mobile_number = models.CharField(max_length=50, blank=True)
    aadhar_number = models.CharField(max_length=255, blank=True)
    company_address = models.TextField(blank=True)

    def __str__(self):
        return f"CommercialProfile: {self.user.email}"


# pricing and quotations

# class Technology(models.Model):
#     slug = models.SlugField(unique=True)
#     name = models.CharField(max_length=64)

#     def __str__(self):
#         return self.name

# class Tier(models.Model):
#     """
#     Customer tiers: Student, Startup, Industrial
#     """
#     slug = models.SlugField(unique=True)
#     name = models.CharField(max_length=64)

#     def __str__(self):
#         return self.name

# class Material(models.Model):
#     technology = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name="materials")
#     name = models.CharField(max_length=128)
#     # approximate density in g/cm^3 (used to convert volume cm^3 -> grams)
#     density_g_per_cm3 = models.FloatField(null=True, blank=True, help_text="g/cm^3")

#     def __str__(self):
#         return f"{self.name} ({self.technology})"

# class MaterialPrice(models.Model):
#     material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="prices")
#     tier = models.ForeignKey(Tier, on_delete=models.CASCADE)
#     price_per_gram = models.DecimalField(max_digits=8, decimal_places=2)  # ₹/g
#     min_price_per_gram = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
#     max_price_per_gram = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

#     class Meta:
#         unique_together = ("material", "tier")

#     def __str__(self):
#         return f"{self.material.name} - {self.tier.name}: {self.price_per_gram}"



# modify quotations

class Technology(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Tier(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

class Material(models.Model):
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE, related_name="materials")
    name = models.CharField(max_length=128)
    density_g_per_cm3 = models.FloatField(null=True, blank=True, help_text="g/cm^3")

    def __str__(self):
        return f"{self.name} ({self.technology})"

class MaterialPrice(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="prices")
    tier = models.ForeignKey(Tier, on_delete=models.CASCADE)
    price_per_gram = models.DecimalField(max_digits=8, decimal_places=2)  # ₹/g
    min_price_per_gram = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    max_price_per_gram = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)

    class Meta:
        unique_together = ("material", "tier")

    def __str__(self):
        return f"{self.material.name} - {self.tier.name}: {self.price_per_gram}"

# optional: fixed palette colors
class Color(models.Model):
    name = models.CharField(max_length=64)
    hex = models.CharField(max_length=7, help_text="#RRGGBB")

    def __str__(self):
        return f"{self.name} ({self.hex})"

# Uploaded file record
class UploadedSTL(models.Model):
    file = models.FileField(upload_to="uploads/stls/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    # link to choices used for price calculation
    technology = models.ForeignKey(Technology, on_delete=models.SET_NULL, null=True)
    material = models.ForeignKey(Material, on_delete=models.SET_NULL, null=True)
    tier = models.ForeignKey(Tier, on_delete=models.SET_NULL, null=True)
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)

    # computed values
    volume_cm3 = models.FloatField(null=True, blank=True)
    weight_grams = models.FloatField(null=True, blank=True)
    price_per_gram = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    material_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    gst_percent = models.DecimalField(max_digits=5, decimal_places=2, default=18)
    gst_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Upload {self.pk} - {self.file.name}"


