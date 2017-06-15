# Day-Three-Bootcamp

#api.py 
The first console app, api.py, consumes the github API and gives a list of dicts of various github events such as push and pull. 
To use it one only needs to pip install requests as it doesnt require any API key.To run, open cmd and run python api.py from the 
directotry in which you will have saved the py file

#api2.py
The second console app uses facebook's GraphAPI. To use it you will have to install facebook-sdk by doing pip install facebook-sdk. You will also have to install requests.
Additionally, you need an access token. The one on my code is valid for approx 60 days. Based on the values you pass as type and q into th search method, the 
app can pull a users friends, as that is the functionality that my access token is allowed to do. 

#api3.py
The third console app is for footbal lovers. It gives various info related to football. The data response is formatted in a dict data structure.
One needs a token in order to use it, and the token can be easily obtained from football-data.org after creating a free account. 

#MaxandMin 
This contains the lab for finding a maximum and minimum number from a list

#WordCount
This folder contains the lab for determining the number of times that words in a sentence appear in that sentence. 
