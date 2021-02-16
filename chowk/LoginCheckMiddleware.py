from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.http import HttpResponseRedirect
from shop.models import totalVisit

class LoginCheckMiddleWare(MiddlewareMixin):
        

    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        user = request.user
        if user.is_authenticated:
            if user.user_type == "1":
               
                if modulename == "owner.views":
                    pass
                elif modulename == 'shop.views' or modulename == 'staff.views' or modulename == 'alluse.views' or modulename == "django.views.static":
                    pass
                elif modulename == "django.contrib.auth.views" or modulename == 'alluse.views'  or modulename =="django.contrib.admin.sites" or modulename == "django.contrib.admin.sites.AdminSite":
                    try:
                        address = request.META.get('HTTP_X_FORWARDED_FOR')
                        if address:
                            ip =address.split(',')[-1].strip()
                        else:
                            ip = request.META.get('REMOTE_ADDR')
                        try:
                            totalV = totalVisit()
                            totalV.ip = ip
                            totalV.save()
                        except:
                            pass
                        
                    except:
                        pass
                    pass
                else:
                    return HttpResponseRedirect(reverse("owner:AdminDashboard"))
            elif user.user_type == "2":
                try:
                    address = request.META.get('HTTP_X_FORWARDED_FOR')
                    if address:
                        ip =address.split(',')[-1].strip()
                    else:
                        ip = request.META.get('REMOTE_ADDR')
                    try:
                        totalV = totalVisit()
                        totalV.ip = ip
                        totalV.save()
                    except:
                        pass
                    
                except:
                    pass
                if modulename == "seller.views":
                    pass
                elif modulename == 'shop.views' or modulename == 'alluse.views' or modulename == 'staff.views' or modulename == "django.views.static" or  modulename == "django.contrib.auth.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("seller:sellerDashboard"))
            elif user.user_type == "3":
                try:
                    address = request.META.get('HTTP_X_FORWARDED_FOR')
                    if address:
                        ip =address.split(',')[-1].strip()
                    else:
                        ip = request.META.get('REMOTE_ADDR')
                    try:
                        totalV = totalVisit()
                        totalV.ip = ip
                        totalV.save()
                    except:
                        pass
                        
                except:
                    pass
                if modulename == "customer.views":
                    pass
                elif modulename == 'shop.views' or modulename == 'alluse.views' or modulename == "django.views.static" or  modulename == "django.contrib.auth.views":
                    pass
                else:
                    return HttpResponseRedirect(reverse("customer:customerDashboard"))
        else:
            try:
                address = request.META.get('HTTP_X_FORWARDED_FOR')
                if address:
                    ip =address.split(',')[-1].strip()
                else:
                    ip = request.META.get('REMOTE_ADDR')
                try:
                    totalV = totalVisit()
                    totalV.ip = ip
                    totalV.save()
                except:
                    pass
                        
            except:
                pass
            if modulename == 'shop.views' or modulename == "django.contrib.auth.views" or modulename == "django.views.static":
                pass
            else:
                return HttpResponseRedirect(reverse("shop:loginPage"))
