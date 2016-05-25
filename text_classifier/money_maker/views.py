from django.shortcuts import render



class HomeView(TemplateView):
    template_name = "money_maker/home.html"
