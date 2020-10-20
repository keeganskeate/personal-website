import os
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from markdown import markdown

from . import forms
from . import state # Save text in Firestore?
from utils.markdown_utils import load_markdown

def create_page_context(context, markdown_file=None, options=None):
    """ Create context for a normal page. """
    context["state"] = state.state
    context["header"] = state.header
    context["footer"] = state.footer
    if markdown_file:
        file_path = os.path.dirname(os.path.realpath(__file__))
        context = load_markdown(context, file_path, markdown_file, options)
    return context

# def load_markdown(context, page, options): # TODO: Generalize
#     """ Load markdown for context given page. """
#     file_name = f"/static/personal_website/docs/{page}.md"
#     file_path = os.path.dirname(os.path.realpath(__file__))
#     file_path += file_name
#     markdown_file = open(file_path, "r")
#     context["markdown"] = markdown(
#         markdown_file.read(), extensions=options
#     )
#     return context

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
        context = create_page_context(context, markdown_file="about")
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
