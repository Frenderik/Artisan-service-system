from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from accounts.models import User

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'))


class CustomPasswordValidator:
    def __call__(self, password):
        # Your custom password policy here
        if not (len(password) >= 8 and any(c.isupper() for c in password) and any(c.isdigit() for c in password) and any(not c.isalnum() for c in password)):
            raise ValidationError(
                "Password must be at least 8 characters long and include at least 1 uppercase letter, 1 number, and 1 special character."
            )




class CustomerRegistrationForm(UserCreationForm):
    # gender = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=GENDER_CHOICES)

    def __init__(self, *args, **kwargs):
        super(CustomerRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['gender'].required = True
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['password1'].validators.append(CustomPasswordValidator())
        self.fields['password2'].label = "Confirm Password"
        self.fields['phone_number'].label="Phone Number"

        # self.fields['gender'].widget = forms.CheckboxInput()

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )
        self.fields['phone_number'].widget.attrs.update(
            {
                'placeholder': 'Phone Number',
            }
        )
    

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2', 'gender','phone_number']
        error_messages = {
            'first_name': {
                'required': 'First name is required',
                'max_length': 'Name is too long'
            },
            'last_name': {
                'required': 'Last name is required',
                'max_length': 'Last Name is too long'
            },
            'gender': {
                'required': 'Gender is required'
            }
        }

    def clean_gender(self):
        gender = self.cleaned_data.get('gender')
        if not gender:
            raise forms.ValidationError("Gender is required")
        return gender

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.role = "customer"
        if commit:
            user.save()
        return user


class ArtisanRegistrationForm(UserCreationForm):
    profile_picture = forms.ImageField(label="Profile Picture", required=False)


    def __init__(self, *args, **kwargs):
        super(ArtisanRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['password1'].validators.append(CustomPasswordValidator())
        self.fields['password2'].label = "Confirm Password"
        self.fields['contact'].label="Contact"
        self.fields['profile_picture'].label="Profile Picture"

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter your First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Your Last Name',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )
        self.fields['contact'].widget.attrs.update(
            {
                'placeholder': 'Contact',
            }
        )
       

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2','contact','profile_picture']
        error_messages = {
            'first_name': {
                'required': 'First name is required',
                'max_length': 'Name is too long'
            },
            'last_name': {
                'required': 'Last name is required',
                'max_length': 'Last Name is too long'
            }
        }

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.role = "artisan"
        if self.cleaned_data['profile_picture']:
            user.profile_picture = self.cleaned_data['profile_picture']
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter Email'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter Password'})

    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user = authenticate(email=email, password=password)

            if self.user is None:
                raise forms.ValidationError("User Does Not Exist.")
            if not self.user.check_password(password):
                raise forms.ValidationError("Password Does not Match.")
            if not self.user.is_active:
                raise forms.ValidationError("User is not Active.")

        return super(UserLoginForm, self).clean(*args, **kwargs)

    def get_user(self):
        return self.user


class CustomerProfileUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CustomerProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['phone_number'].widget.attrs.update(
            {
                'placeholder': 'Phone Number',
            }
        )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "gender","phone_number"]



class ArtisanProfileUpdateForm(forms.ModelForm):
   

    def __init__(self, *args, **kwargs):
        super(ArtisanProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['contact'].widget.attrs.update(
            {
                'placeholder': 'Contact',
            }
        )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "contact","profile_picture"]

 
    def save(self, commit=True):
        user = super(ArtisanProfileUpdateForm, self).save(commit=False)
        # You can add any additional logic here if needed
        if commit:
            user.save()
        return user
    

