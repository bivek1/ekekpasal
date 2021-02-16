from django.shortcuts import redirect, render
from .forms import FormChangePassword
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

# Create your views here.
def changePassword(request):
    if request.user.user_type == '1':
        base = 'owner/ownerDashboard.html'
    elif request.user.user_type == '2':
        base = 'seller/sellerDashboard.html'
    else:
        base = 'customer/customerDashboard.html'

    if request.method == 'POST':
        form = FormChangePassword(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('alluse:changePassword')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = FormChangePassword(request.user)
    return render(request, 'alluse/changePassword.html', {
        'form': form,
        'base':base
    })
   