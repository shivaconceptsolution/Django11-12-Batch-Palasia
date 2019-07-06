from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<header style='background-color:red;height:100px;'><h1>Welcome in DJANGO</h1><a href='home'>HOME</a><a href='about'>About </a><a href='si'>SI</a> </header><section style='background-color:blue;height:500px;color:white;'>danfg adg fgadhfg dfhgdfg hjadghdag hda fgdjfg dfg adfgjhadg hjadghdsa ghd gsjhg dahfg dahfg jfg jhdf ghjad fjhgd fjhd gfjh dgjfgdhfg djf ghdf hdg fhgd hfg dhfg jd gfhdfg</section><footer style='background-color:red;height:50px;'><center>Footer</center></footer>")

def about(request):
	 return HttpResponse("<header style='background-color:red;height:100px;'><h1>Welcome in ABOUT US</h1><a href='home'>HOME</a><a href='about'>About </a><a href='si'>SI</a> </header><section style='background-color:blue;height:500px;'></section><footer style='background-color:red;height:50px;'><center>Footer</center></footer>")
def calculatesi(request):
    p=50000
    r=2.2
    t=2
    si=(p*r*t)/100
    return HttpResponse("result is %.2f" % si)


