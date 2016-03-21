"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from django.test import RequestFactory

from .views import index
from payments.models import User
import mock


class MainPageTest(TestCase):

    # setup

    @classmethod
    def setUpClass(cls):
        request_factory = RequestFactory()
        cls.request = request_factory.get('/')
        cls.request.session = {}

    # Testing routes

    def test_root_resolves_to_main_view(self):
        main_page = resolve('/')
        self.assertEqual(main_page.func, index)

    def test_returns_appropriate_html_response_code(self):
        resp = index(self.request)
        self.assertEquals(resp.status_code, 200)

    # Testing tempaltes and views

    def test_returns_appropriate_html(self):
        index_page = self.client.get('/')
        self.assertTemplateUsed(index_page, 'index.html')

    def test_returns_exact_html(self):
        resp = index(self.request)
        self.assertEquals(
            resp.content,
            render_to_response('index.html').content
        )

    def test_index_handles_logged_in_user(self):

        self.request.session = {'user': '1'}

        with mock.patch('main.views.User') as user_mock:

            config = {'get_by_id.return_value': mock.Mock()}
            user_mock.objects.configure_mock(**config)

            resp = index(self.request)

            self.request.session = {}

            expected_html = render_to_response(
                'user.html',
                {'user': user_mock.get_by_id(1)}
            ).content
            self.assertTemplateUsed(resp.content, 'user.html')
