# NY Times Typing

New York Times Typing is a program that the uses the New York Times API 
and web scraping to select a random paragraph from a recent top article in
the New York Times and allow the user to track their typing speed on the
article with live metrics. It is not sponsored or supported by the New 
York Times in any way.

## Installation

You can use this through git clone.

```bash
git clone https://github.com/AidanG1/typingSpeedTest
```

## Usage

#### Set Up
Create a file in the main directory named api-key.txt
The only content of this file should be an api key which you can get 
here: https://developer.nytimes.com/
Next create an environment variable for the secret key and put it in
an environment variable named TYPING_SPEED_SECRET_KEY.
#### Migrations
This project is currently set up with an extremely basic model for 
saving typing test data. If you want to use the model, you can write some 
simple code to implement registration and login and then just run 
ajax/axios post requests after the typing test is finished to save.
If you want to use the website in the simplest way possible, you do 
not need to run migrations.
```bash
python manage.py migrate
```
#### Run
```bash
python manage.py runserver
```
Visit localhost:8000 in your browser to use.