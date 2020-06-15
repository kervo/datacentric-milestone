# Testing

Making sure that my flask enviroment is running by `flask run` on the command line.

### Heroku error H10 status 503
* Solution: Making sure Heroku had all essencial part installed in the virtual environment folder. To solve this I followed the following video. https://www.youtube.com/watch?v=w25ea_I89iM

### ! [rejected]        master -> master (non-fast-forward)
* Solution: In this I could use on the command line `git push --force` because I am the only user working on this project (https://intellipaat.com/community/22482/rejected-master-master-non-fast-forward-what-does-git-push-non-fast-forward-updates-were-rejected-mean)

### ImportError: cannot import name 'abc' from 'bson.py3compat'
* Solution: I had installed bson and pymongo and apparently they cause a mismatch, to solve this I had to uninstall bson and pymongo and re-inatll pymongo after. 

# References

* CLI cheatsheet for commands: https://github.com/0nn0/terminal-mac-cheatsheet

* How to work with Virtual Environments: https://docs.python.org/3/tutorial/venv.html