# Deploying Backend to Heroku
## 1
The flask server is not production ready so we need to use a different server thing. We will use gunicorn. Install like this
```
pip install gunicorn
```
Also  after you install it make sure to add the updated list of dependencies to your requirements.txt using
```
pip freeze > requirements.txt
```
## 2
You also need a Procfile so that Heroku can use gunicorn to set stuff up. Create a file called “Procfile” which contains the following
```
web: gunicorn name-of-flask-app:app
```
## 3
By default heroku deploys using python 3 but we might be using python 2. To get heroku to deploy using your version of python create a runtime.txt file which specifies the version of python you want it to use for deployment.  A sample runtime.txt file will contain the following line.
```
python-2.7.15
```
## 4
Install the heroku cli. Then run 
```
heroku login
```

To create a heroku project run
```
heroku create project-name
```
Im pretty sure what this does is create a heroku project and add the link to the heroku project’s git repository as a remote of your current git repository. You could also create the heroku project through the heroku dashboard and then manually add the heroku project’s git repo link to your current project’s remote.
```
git remote add heroku link-to-heroku-project-repo.git
```
This link the heroku project’s git repo can be found on the heroku dashboard for your project under the settings tab.

If you run the following command
```
git remote -v
```
You  should see something like this
```
heroku https://git.heroku.com/accelerator-backend-test.git (fetch)
heroku https://git.heroku.com/accelerator-backend-test.git (push)
origin https://github.com/Salamander1012/FlaskDecoratorExample.git (fetch)
origin https://github.com/Salamander1012/ FlaskDecoratorExample.git (push)
```

It’s a list of your remotes. You should see origin, which is the name of the remote on GitHub, and heroku, which is the name of the remote on heroku. Every time you try to push to the remote on heroku using 
```
git push heroku master
```
Heroku will try and host you server and give you a link to where it is hosted.

## 5
When you push to heroku keep your gitignore in mind. If your firebase app credentials are in your gitignore to keep them off of GitHub, when you push to heroku your app won’t work because the version you pushed to heroku also doesn’t have the credentials. To fix this you will need to force add the credentials file when pushing to heroku 
```
git add -f firebase-credentials.json
git commit -m "blah"
git push heroku master
```
(Not sure if this needs to be done)
Make sure to untrack the firebase-credentials file before you push to github. The way I did this is
```
git rm -r --cached .
git add .
git commit -m "blah"
git push origin master
```
This untracks all the files, then you add them all back but the firebase-credentials file is ignored because its in the gitignore

## 6
To view the logs and check for error details you can do 
```
heroku logs --tail
```
 
Or  go to your project dashboard and next to “open app” there should be a “more” button. If you click more a dropdown will appear with an option to view logs.
