from django.test import TestCase
from django.core.urlresolvers import resolve
<<<<<<< HEAD
from main.views import index
import unittest
from django.shortcuts import render_to_response
from main.models import Marketing_items

=======
from main.views import index, report
import unittest
from django.shortcuts import render_to_response
from main.models import MarketingItem
from django import template
from payments.models import User
>>>>>>> abe8bb86f1cf84d3b030cc1e77193d2909d60e28

class MainPageTests(TestCase): 

    @classmethod
    def setUpClass(cls):
        from django.test import RequestFactory
        request_factory = RequestFactory()
        cls.request = request_factory.get('/')
        cls.request.session = {}
        

    def test_root_resolves_to_main_view(self ):
        main_page = resolve('/')
        self.assertEqual(main_page.func, index)

    def test_returns_appropriate_html_respos_code(self):
        resp = index(self.request)
        self.assertEqual(resp.status_code,200)

    def test_returns_exact_html (self):
<<<<<<< HEAD
        market_items = Marketing_items.objects.all()
=======
        market_items = MarketingItem.objects.all()
>>>>>>> abe8bb86f1cf84d3b030cc1e77193d2909d60e28
        resp = index(self.request)
        self.assertEqual(resp.content,
                         render_to_response("main/index.html",
                                            {"marketing_items":market_items})
                         .content)

    def  test_index_handles_logged_in_user(self):
        #create a session that appears to have a logged in user
        self.request.session = {"user" : "1"}
        
        #setup dummy user
        #we need to save user so user -> badges relationship is created
        u = User(email="test@user.com")
        u.save()

        import mock
        with mock.patch('main.views.User') as user_mock:
            
            #tell the mock what to do when called
            config = {'get_by_id.return_value': u}
            user_mock.configure_mock(**config)

            #run the test
            resp = index(self.request)

            #ensure we return the state of the session back to normal 
            self.request.session = {}
            u.delete()
           
            #we are now sending a lot of state for logged in users, rather than
            #recreating that all here, let's just check for some text
            #that should only be present when we are logged in.
            self.assertContains(resp, "Report back to base")

