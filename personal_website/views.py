import os
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import ContactForm
from . import state # Save text in Firestore?
from utils.utils import load_markdown

def create_page_context(context, markdown_file=None, options=None):
    """ Create context for a normal page. """
    context["state"] = state.state
    context["header"] = state.header
    context["footer"] = state.footer
    if markdown_file:
        file_path = os.path.dirname(os.path.realpath(__file__))
        context = load_markdown(
            context,
            file_path,
            markdown_file,
            options,
        )
    return context


class HomePageView(TemplateView):

    template_name = "personal_website/homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homepage'] = state.homepage
        context['posts'] = state.posts
        return create_page_context(context)


class AboutView(TemplateView):

    template_name = "personal_website/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return create_page_context(context, "about")


class ContactView(FormView):

    form_class = ContactForm
    template_name = "personal_website/contact.html"
    success_url = '/thank-you/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return create_page_context(context)

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form) 


class DonateView(TemplateView):

    template_name = "personal_website/donate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return create_page_context(context)


class PostsView(TemplateView):

    template_name = "personal_website/posts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = state.posts        
        return create_page_context(context)


class PrivacyPolicyView(TemplateView):

    template_name = "personal_website/privacy-policy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return create_page_context(context, "privacy_policy")


class ThankYouView(TemplateView):

    template_name = "personal_website/thank-you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return create_page_context(context)
