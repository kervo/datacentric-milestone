# WonderCook Milestone
## Milestone project 3
This project studies the interaction between users and handling data from front-end to back-end of websites.

My project is a playground/boilerplate to understand how Python manages data in between the front-end and the back-end of websites. Python is a versatile and exciting language with a billion of sources, the Python library has been where I spend most of my time learning about how to do stuff depending on the users’ context and interaction.

This is my begging connecting a database with a website, and how to show that information on a card or column on the front-end, as this project evolves, I want to use this process as my journey of the main core of the UX design practices. This is more like a studying messy room where I’m putting all my ideas together.

# UX Design

Creating functions or classes in Python requires to know the type of interaction that the user is having with the site. If you need to display a price in different currencies Python has a converter, among so many other libraries.

### What is the site about?
In this case we want to do a cookbook and the user will be able to do the following actions:

* Create a new account POST
* Log in to an existing account POST
* Search for theirs or other’s recipes GET
* Update or Edit an existing recipe GET and POST
* Add in a new recipe POST
* Delete a recipe GET and POST

As information source this site can be helpful for a person with allergen to know what to cook and what’s convenient for she/he (Allergens ARAY) or simply to explore the cuisine by browsing countries (Countries ARRAY).

Colours to use: Earthy and ochre colour scheme for the backgrounds and a cyan based colour for alerts, links and actions that require the attention of our users. The rest of the image content can be provided by the users. What happens if the user doesn’t upload an image? (add a random image with boolean statement?)

Perhaps users can upload videos when all the site is working.

# Software Development Practices:

* The Structure
Index
```
|—Log in
---| <user> <session>
|—Sign up
  |——-Dashboard
  |—Search recipes <recipe>
  |—Add Recipe
  |—Edit a recipe
  |—Delete a recipe
  |—Log out <session>

|—Index with random recipes <random>
```

### Technologies used
HTML, CSS, Javascript as part of the templates.
Python3, Flask and MongoDB for the back-end.
Heroku as deployment platform (not achieved on my first and simple attempt)

# Testing

### Heroku error H10 status 503
* Solution: Making sure Heroku had all essencial part installed in the virtual environment folder. To solve this I followed the following video. https://www.youtube.com/watch?v=w25ea_I89iM

### ! [rejected]        master -> master (non-fast-forward)
* Solution: In this I could use on the command line `git push --force` because I am the only user working on this project (https://intellipaat.com/community/22482/rejected-master-master-non-fast-forward-what-does-git-push-non-fast-forward-updates-were-rejected-mean)

### ImportError: cannot import name 'abc' from 'bson.py3compat'
* Solution: I had installed bson and pymongo and apparently they cause a mismatch, to solve this I had to uninstall bson and pymongo and re-inatll pymongo after. 

### KeyError: 'A secret key is required to use CSRF.
* Solution: To creat the secret key I followed this answer https://stackoverflow.com/questions/47687307/how-do-you-solve-the-error-keyerror-a-secret-key-is-required-to-use-csrf-whe

### OSError: [Errno 98] Address already in use
* Solution: https://medium.com/@tessywangari05/oserror-errno-98-address-already-in-use-flask-error-ccbff65e2bb5

I don’t know if my testing is the most appropriate, I’m just doing exploratory testing which is some sort of manual testing, I have to say I don’t like the bebug=True option on cause the type errors that I’m getting I have no clue how to read them with line like this:
``` File "/workspace/.pip-modules/lib/python3.8/site-packages/flask/app.py", line 2464, in __call__ ```


I’m just learning now about automating testing:
https://realpython.com/python-testing/


# References

## General 
* Photos by Ella Olsson, Abhinav Goswami from Pexels

* Bootstrap template: https://startbootstrap.com/themes/grayscale/

* CLI cheatsheet for commands: https://github.com/0nn0/terminal-mac-cheatsheet

* FLASK Tutorial: https://blog.miguelgrinberg.com/index

## Flask/Python

* Flask documentation and usage: https://flask.palletsprojects.com/en/1.1.x/

* How to work with Virtual Environments: https://docs.python.org/3/tutorial/venv.html

* How to work with Flask-WTForms: https://flask-wtf.readthedocs.io/en/stable/index.html