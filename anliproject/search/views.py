from django.shortcuts import render
from anli.models import Room
from django.db.models import Q

def searchResult(request):
    if 'location' in request.GET:
        query_1 = request.GET.get('location')
    if 'select_home' in request.GET:
        query_2 = request.GET.get('select_home')

        results = Room.objects.filter(
            Q(location__icontains=query_1) &
            Q(select_home__icontains=query_2)
        )
    
    return render(request, 'search.html', {'query_1': query_1, 'query_2': query_2, 'results': results})