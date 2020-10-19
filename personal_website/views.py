import os
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from markdown import markdown

from . import forms
from . import state # Save text in Firestore?
from utils.markdown_utils import load_markdown

def create_page_context(context):
    """ Create context for a normal page. """
    context["state"] = state.state
    context["header"] = state.header
    context["footer"] = state.footer
    return context

class HomePageView(TemplateView):
    """ Home page. """

    template_name = "personal_website/homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = create_page_context(context)
        context['homepage'] = state.homepage
        return context


class AboutView(TemplateView):
    """ About page. """

    template_name = "personal_website/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = create_page_context(context)
        return context


class ContactView(TemplateView):
    """ Terms of Service page. """

    template_name = "personal_website/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = create_page_context(context)
        return context


class DonateView(TemplateView):
    """ Donate page. """

    template_name = "personal_website/donate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = create_page_context(context)
        return context


class PrivacyPolicyView(TemplateView):
    """ Privacy Policy page. """

    template_name = "personal_website/privacy-policy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = create_page_context(context)
        return context


class TermsOfServiceView(TemplateView):
    """ Terms of Service page. """

    template_name = "personal_website/terms-of-service.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = create_page_context(context)
        return context


class ThankYouView(TemplateView):
    """ Thank you page. """

    template_name = "personal_website/thank-you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = create_page_context(context)
        return context
