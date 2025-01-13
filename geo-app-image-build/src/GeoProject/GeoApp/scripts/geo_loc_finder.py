from geopy import Nominatim


def geo_data_acquire(request):
    curr_se = request.session
    curr_se['selected_city'] = geo_view_manage("")
    if request.POST is not None:
        if 'check_source_city' in request.POST:
            query = request.POST.get('query_city_1')
            city_1 = geo_view_manage(query)
            curr_se['city_1'] = {
                "query": query,
                'data': city_1
            }
            curr_se['selected_city'] = city_1
        if 'check_target_city' in request.POST and curr_se.get('city_1'):
            city_2 = geo_view_manage(request.POST.get('query_city_2'))
            curr_se['city_2'] = {
                "query": request.POST.get('query_city_2'),
                'data': city_2
            }
            curr_se['selected_city'] = city_2
        if 'clear_target_city' in request.POST and curr_se.get('city_2'):
            del curr_se['city_2']
        if 'clear_source_city' in request.POST and curr_se.get('city_1'):
            del curr_se['city_1']


def geo_view_manage(query):
    values_to_be_passed = location_manager(query) or None
    return values_to_be_passed


def location_manager(query):
    values_to_be_passed = {
        "address": "Not Found",
        "latitude": 0.0,
        "longitude": 0.0
    }
    location = get_coordinates(query)

    if location is not None:
        values_to_be_passed.update({
            "address": location.address,
            "latitude": location.latitude,
            "longitude": location.longitude
        })
    return values_to_be_passed or None


# as it is it returns a result of a street and not coordinates
def get_coordinates(city_country):
    geolocator = Nominatim(user_agent="final_exam_exercise")
    try:
        location = geolocator.geocode(city_country)
    except:
        location = geolocator.geocode("Fox Hill West")
    return location
