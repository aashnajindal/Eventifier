# Eventifier #

### An event manager that will help you plan and execute <b>every<b> kind of event! ###

### Author: Aashna Jindal ###

## Set Up Instructions ##

Open a terminal and go to the directory where you wish to install Eventifier

Install `oauth2` and `smtplib` by executing the following command:

`sudo easy_install && pip install oauth2 && pip install smtplib`

Install the Eventifier package by executing this command:

`git clone https://github.com/aashnajindal/Eventifier.git`

Run Eventifier by executing this command:

`python -i mvc.py`

## Video Tutorial ##

To get you started off with Eventifier, have a look at a <a href="http://www.youtube.com/watch?v=ycYo26ceWok">3 minute tutorial</a> that gives you an overview of how Eventifier can make event-planning so much easier and faster for you.

## About ##

Eventifier is an event manager, which will take you step by step through all the aspects you need to go through when planning an event. If you don’t have a venue in mind it will search for venues for you based on the location and type of event that you provide it. In the end you can send an email to all your friends and colleagues inviting them to your event. 

The simple application starts off by letting you pick the kind of event you want to organize. This can range from a birthday partty for your best friend to marriage anniversary party for your grandparents. Once you've decided what you want to organize, you tell Eventifier where, in general, you want this event to be. You could give it a zip code or even a street address. This is where Eventifier becomes a powerful tool. Knowing the kind of event you want to organize and the general vicinity of where you want this event to be, Eventifier intelligently queries Yelp and returns a list of results that would be relevant to you. You can also choose to sort these results by Yelp's ratings! Clicking on any of these results expands them and gives you information like street address and contact details. Once you know where exactly you want to host your party, you can move on to the next stage. If you already know specifically where you are going to host this event then you can choose to bypass the work Eventifier will do for you.