from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Player


class PlayerCreationForm(forms.ModelForm):
    """
    Creates new players. Includes all required fields plus a repeat password
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Player
        fields = ('username', 'email', 'password')

    def password_validation(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords do not match!')
        return password1

    def save(self, commit=True):
        # save the provided password, hashed
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class PlayerChangeForm(forms.ModelForm):
    """
    Updates the players details
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Player
        fields = ('username', 'email', 'password', 'is_active', 'is_superuser')

    def clean_password(self):
        return self.initial['password']


class PlayerAdmin(BaseUserAdmin):
    # player management forms
    form = PlayerChangeForm
    add_form = PlayerCreationForm

    # fields for displaying the user model
    list_display = ('username', 'email', 'is_active', 'is_superuser')
    list_filter = ('is_superuser', )
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_superuser', )})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# register the new playeradmin
admin.site.register(Player, PlayerAdmin)
