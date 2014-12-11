Instructions

1. django-admin.py mysite - Start your project
2. cd mysite - Change directory to your project
3. python manage.py startapp polls - Create the polls application in your project
4. Create the poll and choice models in polls/models.py
5. Register your models in the polls/admin.py file
5. Insert your app ('polls') in the 'installed apps' array in mysite/settings.py
6. python manage.py syncdb - Run syncdb to make Django create your models in the DB, register a username and password (meet, meet)
7. python manage.py runserver - Run the development server to preview your site
8. Go to http://localhost:8000/admin and sign in using (meet, meet).
9. Create a poll and add choices to it.
10. Decide on the views to handle your polls (index, details, vote, results)
10. Write down your routes/views in polls/urls.py, also add the polls application in mysite/urls.py
11. Create templates for how each view will look.
12. Create the views to handle your requests.
13. run the server and check that everything works
