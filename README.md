[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/creyesp/Meetup_uy/master)
[![Colab](https://colab.research.google.com/img/colab_favicon.ico)](https://colab.research.google.com/github/creyesp/Meetup_uy/blob/master/)
# Meetup_uy
Introduction to scikit-learn in a regression problem

# Quick Start

## Run in mybinder server
MyBinder is a free service to run repository en a notebook sesion without install anything, just click [here](https://mybinder.org/v2/gh/creyesp/Meetup_uy/master).

**Warning**: MyBinder run a temporal sesion, when you leave sesion all your changes are going to be delete.

## Run in Google Colab
Colab is a google service to run notebook, but you can only run 1 notebook and to access to complete resources of the repository you should clone repository manually.

Click here to run in colab. 

When the sesion are ready run in a new cell the following commnads:
	!git clone https://github.com/creyesp/Meetup_uy.git
	!mv Meetup_uy/* .

Finally change all path to the current location, for example '../data/ready/properties.csv' to 'data/ready/properties.csv'

## Run in a local environment

Install python 3.5+ in your own machine and clone this repository following next step:

	$ git clone https://github.com/creyesp/Meetup_uy.git
	$ cd Meetup_uy
	$ virtualenv --python=python3.6 venv
	$ source venv/bin/activate
	$ python3 -m pip install --user --upgrade -r binder/requirements.txt
	$ jupyter notebook