# WonderCook Milestone
## Milestone project 3
This project studies the interaction between usr and handling data.

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

# References

## General 
* Photos by Ella Olsson, Abhinav Goswami from Pexels

* Bootstrap template: https://startbootstrap.com/themes/grayscale/

* CLI cheatsheet for commands: https://github.com/0nn0/terminal-mac-cheatsheet

## Flask/Python

* Flask documentation and usage: https://flask.palletsprojects.com/en/1.1.x/

* How to work with Virtual Environments: https://docs.python.org/3/tutorial/venv.html

* How to work with Flask-WTForms: https://flask-wtf.readthedocs.io/en/stable/index.html