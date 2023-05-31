from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, './first_app/index.html', {"name": "I am Rahim", "marks": 86, 
    "courses": [
        {
            "id": 1,
            "course": "C",
            "teacher": "Rahim"
        },
        {
            "id": 2,
            "course": "C++",
            "teacher": "Karim"
        },
        {
            "id": 3,
            "course": "Python",
            "teacher": "Fahim"
        }
    ]
    
    })
    
def about(request):
    render(request, './first_app/about.html')