# accounts/admin.py
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import StudentProfile, StartupProfile, CommercialProfile, Technology, Material, MaterialPrice, Tier, Color, UploadedSTL

# User = get_user_model()

# @admin.register(User)
# class UserAdmin(BaseUserAdmin):
#     list_display = ["email", "user_type", "is_staff"]
#     search_fields = ["email"]
#     ordering = ["email"]
#     fieldsets = (
#         (None, {"fields": ["email", "password", "user_type"]}),
#         ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
#     )
#     add_fieldsets = (
#         (None, {"classes": ("wide",), "fields": ["email", "user_type", "password1", "password2"]}),
#     )

#     # pricing an dquotations 

# @admin.register(Technology)
# class TechAdmin(admin.ModelAdmin):
#     list_display = ["name", "slug"]

# @admin.register(Tier)
# class TierAdmin(admin.ModelAdmin):
#     list_display = ["name", "slug"]

# @admin.register(Material)
# class MaterialAdmin(admin.ModelAdmin):
#     list_display = ["name", "technology", "density_g_per_cm3"]

# @admin.register(MaterialPrice)
# class MaterialPriceAdmin(admin.ModelAdmin):
#     list_display = ["material", "tier", "price_per_gram"]

# @admin.register(Color)
# class ColorAdmin(admin.ModelAdmin):
#     list_display = ["name", "slug"]

# @admin.register(UploadedSTL)
# class UploadedSTLAdmin(admin.ModelAdmin):
#     list_display = ["user", "file", "created_at"]

# admin.site.register(StudentProfile)
# admin.site.register(StartupProfile)
# admin.site.register(CommercialProfile)

    



# modify and update 

User = get_user_model()

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ["email", "user_type", "is_staff"]
    search_fields = ["email"]
    ordering = ["email"]

    fieldsets = (
        (None, {"fields": ["email", "password", "user_type"]}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ["email", "user_type", "password1", "password2"]
        }),
    )

# pricing and quotations admin sections

@admin.register(Technology)
class TechAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]

@admin.register(Tier)
class TierAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ["name", "technology", "density_g_per_cm3"]

@admin.register(MaterialPrice)
class MaterialPriceAdmin(admin.ModelAdmin):
    list_display = ["material", "tier", "price_per_gram"]

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ["name", "hex"]

# @admin.register(UploadedSTL)
# class UploadedSTLAdmin(admin.ModelAdmin):
#     list_display = ["user", "file", "created_at"]

@admin.register(UploadedSTL)
class UploadedSTLAdmin(admin.ModelAdmin):
    list_display = ["id", "file", "uploaded_at", "technology", "material", "tier", "color"]


admin.site.register(StudentProfile)
admin.site.register(StartupProfile)
admin.site.register(CommercialProfile)