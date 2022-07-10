# ConVin-Assignment
Assignment
In this assignment I have creted two templates, one is the landing page where the user is initally landed from which he can authenticate selfs with OAuth2 mechanism for viewing his or her event list.

Below is my folfer structure

![Screenshot 2022-07-10 204617](https://user-images.githubusercontent.com/48827728/178150976-8f4046df-5fe5-469d-ad47-0b75fc346f70.png)

The project has an folder called apps which is created to list or program any apps, in our case there is only one app called as googleCalendar
this is the main app which handles our queries

![Capture](https://user-images.githubusercontent.com/48827728/178151201-78243023-fff8-4b70-bf79-dbc8618eb98c.PNG)


above is the simplification of our apps installed 



![Capture](https://user-images.githubusercontent.com/48827728/178151286-2b43fc1d-56ca-4b13-a8c3-3542ac10394a.PNG)


above are the google libraries we have used

The application works fine on the localhost anslo with thw waitress-serve but there is some issue with herkou deployment as a result I am not able to share live link
But below are some images of the site

(1) User Lands on this page, clicks on - Get Access To Events

![Capture](https://user-images.githubusercontent.com/48827728/178155840-750ff68a-d093-4a5d-8dbc-f8af797869cb.PNG)



(2) As soon as the user selects particular email address and authenticate, HttpResponse is got from google API


![Capture](https://user-images.githubusercontent.com/48827728/178155813-45c1f4e6-fbad-413b-a894-c13287c87c92.PNG)


(3) After reciving the toke we are able to display events


![Capture](https://user-images.githubusercontent.com/48827728/178155753-c81c566d-dcc3-4d1d-a841-f8802880524a.PNG)



Thank You
