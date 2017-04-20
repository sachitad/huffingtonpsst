# huffpsst Django Project #

## Prerequisites ##

- python >= 2.5
- pip
- virtualenv/wrapper (optional)
- foreman (gem)
- heroku (gem)

## Installation ##

### Creating the environment ###

Create a virtual python environment for the project.
If you're not using virtualenv or virtualenvwrapper you may skip this step.

#### For virtualenvwrapper ####

```mkvirtualenv --no-site-packages huffpsst-env```

#### For virtualenv ####

```virtualenv --no-site-packages huffpsst-env```

```cd huffpsst-env```

```source bin/activate```

### Install requirements ###

```cd huffpsst```

```pip install -r requirements.txt```

### Create app at heroku ###

```heroku apps:create -s cedar huffpsst```

### Setup addons ###

Add sentry addon to your heroku app, to enable exception logging (optional)

```heroku addons:add sentry:developer```

### Configure project ###

Edit file ```.env```

### Sync database ###

```foreman run python huffpsst/manage.py syncdb```

## Running ##

```foreman start```

Open browser to 127.0.0.1:5000
