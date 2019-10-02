Original source code: [here](https://github.com/jakerieger/FlaskIntroduction) by [Jake Rieger](https://github.com/jakerieger).
For the deployment, I found this [video](https://www.youtube.com/watch?v=TEuPE5pUh2w) helpful.

### Usage (Ubuntu)
After cloning this repo, and run the virtual env
```
$ cd flask-sus
$ virtualenv -p python3 venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
```
After installing all the requirements, you can deploy it in local environment first. The port number below can be changed.
```
(venv) $ funicorn app:app -b 0.0.0.0:<port #>
```

Next, `runtime.txt` and `Procfile` should contain the current python version and bootup info of heroku respectively. Then push it to github and create the heroku app.
```
(venv) $ git add .
(venv) $ git commit -m "update"
(venv) $ git push origin master

(venv) $ heroku local web
(venv) $ heroku create
(venv) $ git push heroku master
```

We can actually start the server by this command which heroku calls Dinos.
```
(venv) $ heroku ps:scale web=1
```

To shut down the app, you can change the type = 0.
```
(venv) $ heroku ps:scale web=0
(venv) $ deactivate
$
```

