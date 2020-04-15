from django.core import serializers
from django.db.models import Count, Avg, Max, Min
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from orm_all_queries_cookbook.models import Country, State, City


def indexView(request):
    return render(request, 'index.html')


def viewCountries(request):
    if request.is_ajax and request.method == 'GET':
        countries = Country.objects.all().order_by('country_name')
        json_countries = serializers.serialize("json", countries)
    return JsonResponse({"countries": json_countries}, status=200)


def viewStatesByCountry(request):
    if request.is_ajax and request.method == 'GET':
        country_id = request.GET.get('countryId')
        states = State.objects.filter(country_id=country_id).order_by('state_name')
        json_states = serializers.serialize("json", states)
    return JsonResponse({"states": json_states}, status=200)


def viewCitiesByState(request):
    if request.is_ajax and request.method == 'GET':
        state_id = request.GET.get('stateId')
        cities = City.objects.filter(state_id=state_id).order_by('city_name')
        json_cities = serializers.serialize("json", cities)
    return JsonResponse({"cities": json_cities}, status=200)


def getCount(request):
    if request.method == 'GET':
        countryCount = Country.objects.count()
        stateCount = State.objects.count()
        cityCount = City.objects.count()
        print('countryCount = ', countryCount, 'stateCount = ', stateCount, 'cityCount = ', cityCount)
        return render(request, 'index.html',
                      {'countryCount': countryCount, 'stateCount': stateCount, 'cityCount': cityCount})


def getCountBy(request):
    if request.method == 'GET':
        noOfState = Country.objects.values('country_name').order_by('country_name').annotate(count=Count('state'))
    return render(request, 'index.html', {'CountBy': noOfState})


def getAvg(request):
    if request.method == 'GET':
        avg = Country.objects.all().aggregate(Avg('id'))
        print('Average : ', avg)
        return render(request, 'index.html', {'Average': avg})


def getMax(request):
    if request.method == 'GET':
        maxValue = Country.objects.all().aggregate(Max('id'))
        print('Max : ', maxValue)
        return render(request, 'index.html', {'Max': maxValue})


def getMin(request):
    if request.method == 'GET':
        minValue = Country.objects.all().aggregate(Min('id'))
        print('Min : ', minValue)
        return render(request, 'index.html', {'Min': minValue})


def doAnd(request):
    if request.method == 'GET':
        queryset = Country.objects.filter(country_name__startswith='I', id=1)
        print(queryset)
        return render(request, 'index.html', {'and': queryset})


def doOr(request):
    if request.method == 'GET':
        queryset = Country.objects.filter(country_name__startswith='R') | Country.objects.filter(id=2)
        print(queryset)
        return render(request, 'index.html', {'or': queryset})


def doSelectSomeFields(request):
    queryset = Country.objects.values('country_name', 'state')
    print(queryset)
    return render(request, 'index.html', {'SomeFields': queryset})


def doFindSecondLargest(request):
    queryset = Country.objects.order_by('-country_name')[1]  # Second Highest record
    print(queryset)
    return render(request, 'index.html', {'SecondLargest': queryset})


def doAsc(request):
    queryset = Country.objects.all().order_by('country_name')
    print(queryset)
    return render(request, 'index.html', {'asc': queryset})


def doDesc(request):
    queryset = Country.objects.all().order_by('-country_name')
    print(queryset)
    return render(request, 'index.html', {'desc': queryset})


def doLike(request):
    queryset = Country.objects.filter(country_name__contains='I')
    print(queryset)
    return render(request, 'index.html', {'like': queryset})


def doBetween(request):
    queryset = Country.objects.filter(id__range=(1, 5))
    print(queryset)
    return render(request, 'index.html', {'between': queryset})
