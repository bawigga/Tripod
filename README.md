## About Tripod

Tripods is a photo gallery manager built on [Tornado](http://www.tornadoweb.org/). It's not meant to provide a gallery interface for your users, it's meant to be an admin panel and provide an API so you can tightly integrate galleries into any application.

## Requirements

### Install virtualenv and virtualenvwrapper

I recommend you use `virtualenv` with `virtualenvwrapper` to get a sandboxed environment. This way you won't mess with any other python apps you might have. Here's how you can get that setup. Might need to run as root.

	$ pip install virtualenv virtualenvwrapper

Then you need to source virtualenvwrapper.sh in your bash_profile or bashrc. Add the following lines:

	export WORKON_HOME=$HOME/.virtualenvs
	export PIP_VIRTUALENV_BASE=$WORKON_HOME
	export PIP_RESPECT_VIRTUALENV=true
	source /usr/local/bin/virtualenvwrapper.sh

Now restart your shell or source your bash_profile in your current session.

### Create an environment for tripod

To setup a sandboxed env for tripod, run the following in your shell:

	$ mkvirtualenv tripod

`mkvirtualenv` sets up an environment in `~/.virtualenvs/tripod`

	$ toggleglobalsitepackages

`toggleglobalsitepackages` will disable access to the global packages you have on your machine.

## Installation

	$ workon tripod
	$ pip install -r requirments.txt
