"""
URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:

    https://docs.djangoproject.com/en/3.1/topics/http/urls/

Examples:

    Function views
        1. Add an import:  from my_app import views
        2. Add a URL to urlpatterns:  path('', views.home, name='home')

    Class-based views
        1. Add an import:  from other_app.views import Home
        2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

    Including another URLconf
        1. Import the include() function: from django.urls import include, path
        2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.conf import settings

from . import views

# Main URLs
urlpatterns = [
    path("", views.HomePageView.as_view(), name="index"),
    path("admin/", admin.site.urls, name="admin"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path("privacy-policy/", views.PrivacyPolicyView.as_view(), name="privacy-policy"),
    path(
        "terms-of-service/", views.TermsOfServiceView.as_view(), name="terms-of-service"
    ),
    path("thank-you/", views.ThankYouView.as_view(), name="thank-you"),
    path(
        "issues/", views.ThankYouView.as_view(), name="issues"
    ),  # TODO: Redirect to Github
    path("donate/", views.DonateView.as_view(), name="donate"),
    path("posts/", views.ThankYouView.as_view(), name="posts"),
    path("software/", views.ThankYouView.as_view(), name="software"),
    path("software/coverletter-ai", views.ThankYouView.as_view(), name="coverletter-ai"),
]

# Authentication (Optional)
# https://docs.djangoproject.com/en/3.1/topics/auth/default/#user-objects
# urlpatterns += [
#     # Custom authentication app
#     path("account/", include("auth.urls"), name="auth"),
#     # Django authentication
#     # path('accounts/', include('django.contrib.auth.urls')),
#     # path('accounts/login/', auth_views.LoginView.as_view(template_name='personal_website/login.html')),
#     # path('change-password/', auth_views.PasswordChangeView.as_view()),
# ]

# Functions
# urlpatterns += [
#     path("ajax/send-message/", send_message, name="send_message"),
# ]

# Serve static assets in development and production.
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
