# Picasso

### 23/08/2019

## By **[Brian Sunday](https://github.com/Sundaybrian/Picasso)**

## Description

This is a django web app that allows users to see various types of photos posted by me.They can search the images by category,author,location and image name.They can also click an image to view all the details about if.

## User Stories

As a user I would like:
* to see various photos
* to search for a photo based on category
* to filter photos based on location
* to click and photo and see all the details about it in a modal

As an admin
* to post various photos
* to update the photos
* to delete the photos

## Specifications

| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Click an image| Click| A modal pop up with the image details |
| Search by category| Enter category name into form field | Redirect to a search results page and Images of that category are fetched|
| Search by location| Enter location name into form field | Redirect to a search results page and Images associated with that location are fetched|
| Search by author| Enter author name into form field | Redirect to a search results page and Images associated with that author are fetched|
| Search by image name| Enter image name into form field | Redirect to a search results page and Images associated with that name fetched|
| Search by any specified criteria | Enter the keyword| Redirect to a search results page and if criteria is matched to any keyword a message is shown of zero results found|


## Setup/Installation Requirements

* `$ git clone` [Picasso](https://github.com/Sundaybrian/Picasso)
* `$ cd picasso`   
* `$ python3.6 -m venv virtual` to create a  virtual environment
* `$ source virtual/bin/activate` to activate the virtual environment
* `$ psql` to activate the postgres server
* `$ username=create database picasso` create db with the name blogfest
* run `$ python3.6 -m pip install -r requirements.txt ` to install dependencies
* `$ python3.6 manage.py makemigration` to initialize database migrations
* `$ python3.6 manage.py migrate ` to commit the migration you are running
* `$ python3.6 manage.py createsuperuser ` to create admin credentials that will enable you to log in to the admin side
* `$ python manage.py runserver` to start the application

## Known Bugs

* No known Bugs

## Technologies Used

* Python3.6
* Django
* Bootstrap
* Masonry Grid
* Javascript
* Postgres Database
* CSS
* HTML

### License

MIT