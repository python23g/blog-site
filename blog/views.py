from django.shortcuts import render
from django.views import View
from django.http import HttpRequest, HttpResponse


class HomeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        pass


class AboutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        pass


class ContactView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        pass


class BlogsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        pass