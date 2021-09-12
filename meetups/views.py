from django.shortcuts import render


# Create your views here.

def index(request):
    meetups = [
        {'title': 'First meetup!', 'location': 'Ha Noi', 'slug': 'hanoi'},
        {'title': 'Second meetup!', 'location': 'Ho Chi Minh', 'slug': 'hochiminh'}
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })


def meetup_details(request, meetup_slug):
    print(meetup_slug)
    selected_meetup = {
        'title': 'First meetup!',
        'location': 'Ha Noi', 'slug': 'hanoi',
        'description': 'This is description'
    }
    return render(request, 'meetups/meetup-details.html', {
        'selected_meetup': selected_meetup
    })
