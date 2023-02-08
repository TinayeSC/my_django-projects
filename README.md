# Django Projects
This project was intended as my introduction to Django and as a means of furthering my skills with HTML and Bootstrap. The files present are all required inorder to succesfully run the websites. 

Within these Django projects there are two different websites; one in the folder 'capstone' and one in the folder 'hyperion'. 

* ## Capstone Project
The capstone project is the most recent django project I have completed. It is a fake website which I made for one of my friends who makes music. The website has simple functionality of switching between the home page, merchnadise page, and album page. I did not add any function to most of the price buttons, however I want to add a basket function in the future. So far, the main functionaility is playing the UouTube video of the song and embedding a spotify link to the song within the website. 

* ## Hyperion Project
This project was my first exploration into django, through the guidance of the HyperionDev bootcamp. This project was used to learn about creating apps, creating different views, handling models, among other necessities for django projects. This specific project, is a random amalgam of apps with differing functionality. There is a page which displays blogs, and allows the superuser to upload new ones. There is a page that allows users to vote on different polls, and there is a page containing my CV. Additionally, this porject has the added functionality of requiring users to create an account before they can use the site. 


### Installation
To install the project, I suggest cloning this repository using Github Desktop. Github does not support django websites so you will need the files on your own device if you wish to run the websites. If you struggle to clone the repositories to your own device, you could download each file directly from my github page; however, this will take much longer. 

### Usage
Once you have installed or downloaded the project succesfully. Make sure that you know the path of the project. Next you need to make a new virtual environment. 

python3 -m venv /path/to/new/virtual/environment

The command above should work depending on your device. If it does not, there are many sources that will explain simply how to do so. 
Once the virtual envrionment is created, you must change directory (cd) to the virtual environment. Once there implement this line of code into the terminal:

source env/bin/activate 

This will activate the virtual environment. The django project does not need to be within this virtual environment, but it will save time from having to chnage directory jmore than once. The penultimate step is to change directory into one of the two django projects you installed for example: 

cd my-djang-projects/capstone

Latly, you need to run the server with this line of code. 

python3 manage.py runserver 


## Credits 
The music and visuals used in the capstone project are from Chosan. Links to him are in the project. The clothing in the capstone project is from @bywonderkid on Instagram. Many of the techniques used were learnt from the HyperionDev software engineering bootcamp, and the blogs on the hyperion project are ones from my previous studies. 
