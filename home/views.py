from django.shortcuts import render

# Create your views here.
def index(request):
    mySiteDate = {
        "mysite_name": "MySite Home",
        "section3" : [
            ("TEST1"," 1 dir ","home/images/pic06.jpg"),
            ("TEST2","2 dir","home/images/pic07.jpg"),
            ("TEST3","3 dir","home/images/pic08.jpg")
        ]
    }
    return render(request, "home/index.html", mySiteDate)