import os

from django.http import FileResponse, Http404
from django.shortcuts import redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from personal_website import state # Save text in Firestore?
from personal_website.forms import ContactForm
from utils.utils import create_page_context, load_markdown


FILE_PATH = os.path.dirname(os.path.realpath(__file__))

class HomePageView(TemplateView):

    template_name = "personal_website/homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['homepage'] = state.homepage
        context['portfolio'] = state.portfolio[:2]
        context['posts'] = state.posts
        return create_page_context(context, FILE_PATH)


class AboutView(TemplateView):

    template_name = "personal_website/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return create_page_context(context, FILE_PATH, "about")


class ContactView(FormView):

    form_class = ContactForm
    template_name = "personal_website/contact.html"
    success_url = '/thank-you/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return create_page_context(context, FILE_PATH)

    def form_valid(self, form):
        form.send_email()
        return super(ContactView, self).form_valid(form) 


class DonateView(TemplateView):

    template_name = "personal_website/donate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return create_page_context(context, FILE_PATH)


class PortfolioView(TemplateView):

    template_name = "personal_website/portfolio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolio'] = state.portfolio
        return create_page_context(context, FILE_PATH)


class PostsView(TemplateView):

    template_name = "personal_website/posts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = state.posts
        markdown_file = None
        page = self.request.path.split("/")[2]
        if page:
            markdown_file = f"posts/{page}"
        return create_page_context(context, FILE_PATH, markdown_file)


class PrivacyPolicyView(TemplateView):

    template_name = "personal_website/privacy-policy.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return create_page_context(context, FILE_PATH, "privacy_policy")


class ThankYouView(TemplateView):

    template_name = "personal_website/thank-you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return create_page_context(context, FILE_PATH)


def pdf_view(request):
    filename = request.path.split('/pdf/')[-1]
    print('TODO: Get PDF url from Firestore.:', filename)
    file_url = r"https://firebasestorage.googleapis.com/v0/b/keegan-skeate-website.appspot.com/o/public%2Fwebsite%2Fpdfs%2Fresume.pdf?alt=media&token=0560d36a-917c-4c14-a2c0-d11802a65dd4"
    try:
        return redirect(file_url)
    except FileNotFoundError:
        raise Http404()

