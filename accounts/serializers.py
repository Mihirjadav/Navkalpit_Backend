# # accounts/serializers.py
# from django.contrib.auth import get_user_model
# from rest_framework import serializers
# from django.contrib.auth.password_validation import validate_password
# from .models import StudentProfile, StartupProfile, CommercialProfile

# User = get_user_model()

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'email', 'user_type')

# # Student registration serializer
# class StudentRegisterSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)
#     confirm_password = serializers.CharField(write_only=True)

#     # student fields
#     full_name = serializers.CharField()
#     country = serializers.CharField(required=False, allow_blank=True)
#     state = serializers.CharField(required=False, allow_blank=True)
#     city = serializers.CharField(required=False, allow_blank=True)
#     university_name = serializers.CharField(required=False, allow_blank=True)
#     department = serializers.CharField(required=False, allow_blank=True)
#     course = serializers.CharField(required=False, allow_blank=True)
#     semester = serializers.CharField(required=False, allow_blank=True)
#     end_of_semester = serializers.CharField(required=False, allow_blank=True)
#     aadhar_number = serializers.CharField(required=False, allow_blank=True)
#     address = serializers.CharField(required=False, allow_blank=True)
#     mobile_number = serializers.CharField(required=False, allow_blank=True)
#     enrollment_no = serializers.CharField(required=False, allow_blank=True)
#     collage_idcard = serializers.CharField(required=False, allow_blank=True)

#     def validate(self, data):
#         if data['password'] != data['confirm_password']:
#             raise serializers.ValidationError("Password and Confirm Password do not match.")
#         validate_password(data['password'])
#         if User.objects.filter(email=data['email']).exists():
#             raise serializers.ValidationError("A user with that email already exists.")
#         return data

#     def create(self, validated_data):
#         password = validated_data.pop('password')
#         validated_data.pop('confirm_password', None)
#         email = validated_data.pop('email')
#         # create user
#         user = User.objects.create(email=email, user_type='student')
#         user.set_password(password)
#         user.save()
#         # create profile
#         StudentProfile.objects.create(user=user, **{k: validated_data.get(k, '') for k in [
#             'full_name','country','state','city','university_name','department','course','semester',
#             'end_of_semester','aadhar_number','address','mobile_number','enrollment_no','collage_idcard']})
#         return user

# # Startup registration serializer
# class StartupRegisterSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)
#     confirm_password = serializers.CharField(write_only=True)

#     company_name = serializers.CharField()
#     owner_name = serializers.CharField(required=False, allow_blank=True)
#     company_mobile_number = serializers.CharField(required=False, allow_blank=True)
#     # dp_certificate_no = serializers.CharField(required=False, allow_blank=True) # store number or 'No'
#     # udyam_certificate_no = serializers.CharField(required=False, allow_blank=True)

#     dp_id_certificate = serializers.BooleanField(required=False)
#     dp_certificate_no = serializers.CharField(required=False, allow_blank=True)

#     udyam_certificate = serializers.BooleanField(required=False)
#     udyam_certificate_no = serializers.CharField(required=False, allow_blank=True)

#     company_type = serializers.CharField(required=False, allow_blank=True)
#     owner_aadhar_card = serializers.CharField(required=False, allow_blank=True)
#     gst_number = serializers.CharField(required=False, allow_blank=True)
#     company_description = serializers.CharField(required=False, allow_blank=True)

#     def validate(self, data):
#         if data['password'] != data['confirm_password']:
#             raise serializers.ValidationError("Password and Confirm Password do not match.")
#         validate_password(data['password'])
#         if User.objects.filter(email=data['email']).exists():
#             raise serializers.ValidationError("A user with that email already exists.")
#         return data

#     def create(self, validated_data):
#         password = validated_data.pop('password')
#         validated_data.pop('confirm_password', None)
#         email = validated_data.pop('email')
#         user = User.objects.create(email=email, user_type='startup')
#         user.set_password(password)
#         user.save()
#         StartupProfile.objects.create(user=user, **{k: validated_data.get(k, '') for k in [
#             'company_name','owner_name','company_mobile_number','dp_id_certificate','udyam_certificate',
#             'company_type','owner_aadhar_card','gst_number','company_description']})
#         return user

# # Commercial registration serializer
# class CommercialRegisterSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     password = serializers.CharField(write_only=True)
#     confirm_password = serializers.CharField(write_only=True)

#     company_name = serializers.CharField()
#     gst_number = serializers.CharField(required=False, allow_blank=True)
#     company_type = serializers.CharField(required=False, allow_blank=True)
#     business_type = serializers.CharField(required=False, allow_blank=True)
#     company_mobile_number = serializers.CharField(required=False, allow_blank=True)
#     aadhar_number = serializers.CharField(required=False, allow_blank=True)
#     company_address = serializers.CharField(required=False, allow_blank=True)

#     def validate(self, data):
#         if data['password'] != data['confirm_password']:
#             raise serializers.ValidationError("Password and Confirm Password do not match.")
#         validate_password(data['password'])
#         if User.objects.filter(email=data['email']).exists():
#             raise serializers.ValidationError("A user with that email already exists.")
#         return data

#     def create(self, validated_data):
#         password = validated_data.pop('password')
#         validated_data.pop('confirm_password', None)
#         email = validated_data.pop('email')
#         user = User.objects.create(email=email, user_type='commercial')
#         user.set_password(password)
#         user.save()
#         CommercialProfile.objects.create(user=user, **{k: validated_data.get(k, '') for k in [
#             'company_name','gst_number','company_type','business_type','company_mobile_number','aadhar_number','company_address']})
#         return user



# accounts/serializers.py
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import StudentProfile, StartupProfile, CommercialProfile, Technology, Tier, Material, MaterialPrice, Color, UploadedSTL
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "user_type")


class StudentRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    full_name = serializers.CharField()
    country = serializers.CharField(required=False, allow_blank=True)
    state = serializers.CharField(required=False, allow_blank=True)
    city = serializers.CharField(required=False, allow_blank=True)
    university_name = serializers.CharField(required=False, allow_blank=True)
    department = serializers.CharField(required=False, allow_blank=True)
    course = serializers.CharField(required=False, allow_blank=True)
    semester = serializers.CharField(required=False, allow_blank=True)
    end_of_semester = serializers.CharField(required=False, allow_blank=True)
    aadhar_number = serializers.CharField(required=False, allow_blank=True)
    address = serializers.CharField(required=False, allow_blank=True)
    mobile_number = serializers.CharField(required=False, allow_blank=True)
    enrollment_no = serializers.CharField(required=False, allow_blank=True)
    collage_idcard = serializers.CharField(required=False, allow_blank=True)

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Password and Confirm Password do not match.")
        validate_password(data["password"])
        if User.objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError("A user with that email already exists.")
        return data

    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data.pop("confirm_password", None)
        email = validated_data.pop("email")
        user = User.objects.create(email=email, user_type="student")
        user.set_password(password)
        user.save()
        StudentProfile.objects.create(user=user, **{k: validated_data.get(k, "") for k in [
            "full_name","country","state","city","university_name","department","course","semester",
            "end_of_semester","aadhar_number","address","mobile_number","enrollment_no","collage_idcard"]})
        return user


class StartupRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    company_name = serializers.CharField()
    owner_name = serializers.CharField(required=False, allow_blank=True)
    company_mobile_number = serializers.CharField(required=False, allow_blank=True)
    # dp_id_certificate = serializers.CharField(required=False, allow_blank=True)
    # udyam_certificate = serializers.CharField(required=False, allow_blank=True)
    dp_id_certificate = serializers.BooleanField(required=False)
    dp_certificate_no = serializers.CharField(required=False, allow_blank=True)

    udyam_certificate = serializers.BooleanField(required=False)
    udyam_certificate_no = serializers.CharField(required=False, allow_blank=True)

    company_type = serializers.CharField(required=False, allow_blank=True)
    owner_aadhar_card = serializers.CharField(required=False, allow_blank=True)
    gst_number = serializers.CharField(required=False, allow_blank=True)
    company_description = serializers.CharField(required=False, allow_blank=True)

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Password and Confirm Password do not match.")
        validate_password(data["password"])
        if User.objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError("A user with that email already exists.")
        return data

    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data.pop("confirm_password", None)
        email = validated_data.pop("email")
        user = User.objects.create(email=email, user_type="startup")
        user.set_password(password)
        user.save()

        # Make sure Booleans are always True/False
        dp = validated_data.get("dp_id_certificate", False)
        dp_no = validated_data.get("dp_certificate_no") if dp else ""
        udyam = validated_data.get("udyam_certificate", False)
        udyam_no = validated_data.get("udyam_certificate_no") if udyam else ""

        StartupProfile.objects.create(user=user, **{k: validated_data.get(k, "") for k in [
            "company_name","owner_name","company_mobile_number","dp_id_certificate","udyam_certificate",
            "company_type","owner_aadhar_card","gst_number","company_description","dp_certificate_no",
            "udyam_certificate_no"]})
        return user


class CommercialRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    company_name = serializers.CharField()
    gst_number = serializers.CharField(required=False, allow_blank=True)
    company_type = serializers.CharField(required=False, allow_blank=True)
    business_type = serializers.CharField(required=False, allow_blank=True)
    company_mobile_number = serializers.CharField(required=False, allow_blank=True)
    aadhar_number = serializers.CharField(required=False, allow_blank=True)
    company_address = serializers.CharField(required=False, allow_blank=True)

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Password and Confirm Password do not match.")
        validate_password(data["password"])
        if User.objects.filter(email=data["email"]).exists():
            raise serializers.ValidationError("A user with that email already exists.")
        return data

    def create(self, validated_data):
        password = validated_data.pop("password")
        validated_data.pop("confirm_password", None)
        email = validated_data.pop("email")
        user = User.objects.create(email=email, user_type="commercial")
        user.set_password(password)
        user.save()
        CommercialProfile.objects.create(user=user, **{k: validated_data.get(k, "") for k in [
            "company_name","gst_number","company_type","business_type","company_mobile_number","aadhar_number","company_address"]})
        return user
    
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = "email"

    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")

        # Authenticate using email only
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid email or password")

        data = super().validate(attrs)

        # return user_type inside JWT payload
        data["user_type"] = user.user_type
        data["email"] = user.email

        return data


# pricing and quotation

# class TechnologySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Technology
#         fields = ("id", "slug", "name")

# class TierSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tier
#         fields = ("id", "slug", "name")

# class MaterialPriceSerializer(serializers.ModelSerializer):
#     tier = TierSerializer()
#     class Meta:
#         model = MaterialPrice
#         fields = ("id", "tier", "price_per_gram", "min_price_per_gram", "max_price_per_gram")

# class MaterialSerializer(serializers.ModelSerializer):
#     prices = MaterialPriceSerializer(many=True)
#     class Meta:
#         model = Material
#         fields = ("id", "name", "density_g_per_cm3", "prices")


# modify quotations 

# class TechnologySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Technology
#         fields = ("id","slug","name")

# class TierSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tier
#         fields = ("id","slug","name")

# class MaterialPriceSerializer(serializers.ModelSerializer):
#     tier = TierSerializer()
#     class Meta:
#         model = MaterialPrice
#         fields = ("id","tier","price_per_gram","min_price_per_gram","max_price_per_gram")

# class MaterialSerializer(serializers.ModelSerializer):
#     prices = MaterialPriceSerializer(many=True, read_only=True)
#     class Meta:
#         model = Material
#         fields = ("id","name","density_g_per_cm3","prices")

# class ColorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Color
#         fields = ("id","name","hex")

# class UploadedSTLSerializer(serializers.ModelSerializer):
#     file_url = serializers.SerializerMethodField()
#     material = MaterialSerializer()
#     tier = TierSerializer()
#     color = ColorSerializer()

#     class Meta:
#         model = UploadedSTL
#         fields = ("id","file","file_url","uploaded_at","technology","material","tier","color",
#                   "volume_cm3","weight_grams","price_per_gram","material_cost","gst_percent","gst_value","total_price")

#     def get_file_url(self, obj):
#         request = self.context.get("request")
#         if request is None:
#             return obj.file.url
#         return request.build_absolute_uri(obj.file.url)


class TechnologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Technology
        fields = ("id", "slug", "name")

class TierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tier
        fields = ("id", "slug", "name")

class MaterialPriceSerializer(serializers.ModelSerializer):
    tier = TierSerializer(read_only=True)
    tier_id = serializers.PrimaryKeyRelatedField(
        queryset=Tier.objects.all(), source="tier", write_only=True, required=False
    )

    class Meta:
        model = MaterialPrice
        fields = ("id", "tier", "tier_id", "price_per_gram", "min_price_per_gram", "max_price_per_gram")

class MaterialSerializer(serializers.ModelSerializer):
    # input accepts technology id, output shows technology id
    class Meta:
        model = Material
        fields = ("id", "name", "technology", "density_g_per_cm3")
        read_only_fields = ("id",)

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ("id", "name", "hex")  

class UploadedSTLSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField()
    material = MaterialSerializer(read_only=True)
    tier = TierSerializer(read_only=True)
    color = ColorSerializer(read_only=True)

    class Meta:
        model = UploadedSTL
        fields = (
            "id","file","file_url","uploaded_at","technology","material","tier","color",
            "volume_cm3","weight_grams","price_per_gram","material_cost","gst_percent","gst_value","total_price"
        )
        read_only_fields = ("volume_cm3","weight_grams","price_per_gram","material_cost","gst_value","total_price","uploaded_at")

    def get_file_url(self, obj):
        request = self.context.get("request", None)
        if request:
            return request.build_absolute_uri(obj.file.url)
        return obj.file.url
