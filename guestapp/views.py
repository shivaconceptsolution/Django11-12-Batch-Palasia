from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	s="<html>"
	s+="<head><style type='text/css'>*{margin:0px;} a{color:white;margin-left:20px;}</style></head>"
	s+= "<body>"
	s+="<header style='background-color:black;color:white;height:100px;'>"
	s+="<h1><a href='home'>Home</a><a href='about'>About</a><a href='contact'>Contact us</a></h1>"
	s+="</header>"
	s+="<section style='background-color:gray;color:white;height:480px;'>"
	s+="<p>Home page dhfjdshdhg</p>"
	s+="</section>"
	s+="<footer style='background-color:black;color:white;height:100px;'>"
	s+="</footer>"
	s+="</body>"
	s+="</html>"
	return HttpResponse(s)
def about(request):
	s="<html>"
	s+="<head><style type='text/css'>*{margin:0px;} a{color:white;margin-left:20px;}</style></head>"
	s+= "<body>"
	s+="<header style='background-color:black;color:white;height:100px;'>"
	s+="<h1><a href='home'>Home</a><a href='about'>About</a><a href='contact'>Contact us</a></h1>"
	s+="</header>"
	s+="<section style='background-color:gray;color:white;height:480px;'>"
	s+="<p>About Page</p>"
	s+="</section>"
	s+="<footer style='background-color:black;color:white;height:100px;'>"
	s+="</footer>"
	s+="</body>"
	s+="</html>"
	return HttpResponse(s)

def contact(request):
	s="<html>"
	s+="<head><style type='text/css'>*{margin:0px;} a{color:white;margin-left:20px;}</style></head>"
	s+= "<body>"
	s+="<header style='background-color:black;color:white;height:100px;'>"
	s+="<h1><a href='home'>Home</a><a href='about'>About</a><a href='contact'>Contact us</a></h1>"
	s+="</header>"
	s+="<section style='background-color:gray;color:white;height:480px;'>"
	s+="<p>Contact Page</p>"
	s+="</section>"
	s+="<footer style='background-color:black;color:white;height:100px;'>"
	s+="</footer>"
	s+="</body>"
	s+="</html>"
	return HttpResponse(s)   	


