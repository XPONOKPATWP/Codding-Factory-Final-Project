import geopy.distance
from django.contrib.sites import requests


def calculate_and_store_consumption_result(request):
    curr_se = request.session
    if 'distance' in request.session and 'fuel_consumption' in request.session:
        get_ratio = curr_se['distance'] / 100.0
        consumption_in_liters = get_ratio * float(curr_se['fuel_consumption'])
        print(consumption_in_liters)
        curr_se['calculated_consumption'] = consumption_in_liters
    elif 'calculated_consumption' in curr_se:
        del curr_se['calculated_consumption']


def geo_parameters_manage_distance(request=requests):
    curr_se = request.session
    distance = find_distance(curr_se.get('city_1') or None, curr_se.get('city_2') or None, curr_se.get('is_kilometers'))
    curr_se['distance'] = distance
    if curr_se.get('distance') == 0.0:
        del curr_se['distance']


def find_distance(city_1, city_2, is_kilometers):
    distance_instance = 0.0
    if city_1 is not None and city_2 is not None:
        city_1_cords = city_1.get('data').get('latitude'), city_1.get('data').get('longitude')
        city_2_cords = city_2.get('data').get('latitude'), city_2.get('data').get('longitude')
        if is_kilometers:
            distance_instance = geopy.distance.distance(city_1_cords, city_2_cords).kilometers
        else:
            distance_instance = geopy.distance.distance(city_1_cords, city_2_cords).miles
    return distance_instance


def manage_mode_and_parameters(request):
    curr_se = request.session
    curr_se['is_kilometers'] = True
    if request.POST is not None:
        if 'fuel_consumption_btn' in request.POST:
            curr_se['fuel_consumption'] = request.POST.get("fuel_consumption")
        if 'clear_fuel_consumption_btn' in request.POST and curr_se.get('fuel_consumption'):
            del curr_se['fuel_consumption']
        if 'kilometers_btn' in request.POST:
            curr_se['is_kilometers'] = True
            pass
        if 'miles_btn' in request.POST:
            curr_se['is_kilometers'] = False
            pass
