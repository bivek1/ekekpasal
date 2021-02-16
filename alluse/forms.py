from django.contrib.auth.forms import PasswordChangeForm

class FormChangePassword(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(FormChangePassword, self).__init__(*args, **kwargs)
        for field in ('old_password', 'new_password1', 'new_password2'):
            self.fields['old_password'].widget.attrs = {'class': 'form-control ch', 'placeholder':"Old Password"}
            self.fields['new_password1'].widget.attrs = {'class': 'form-control ch', 'placeholder':"New Password"}
            self.fields['new_password2'].widget.attrs = {'class': 'form-control ch', 'placeholder':"Re New Password"}