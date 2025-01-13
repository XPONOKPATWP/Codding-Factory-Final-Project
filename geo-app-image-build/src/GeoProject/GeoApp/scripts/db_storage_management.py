from django.db.models.functions import datetime

from GeoApp.models import UserQueryLogs


def pass_to_database(request):
    curr_se = request.session

    if 'calculated_consumption' in request.session:
        username = curr_se.get('user').get('username')
        city_1_instance = curr_se.get('city_1')
        city_2_instance = curr_se.get('city_2')
        city_1_address = city_1_instance.get('data').get('address')
        city_2_address = city_2_instance.get('data').get('address')
        city_1_coords = str(
            "( " + str(city_1_instance.get('data').get('latitude'))
            + " , "
            + str(city_1_instance.get('data').get('longitude')) + " )"
        )
        city_2_coords = str(
            "( " + str(city_2_instance.get('data').get('latitude'))
            + " , "
            + str(city_2_instance.get('data').get('longitude')) + " )"
        )
        result_calculation = curr_se.get('calculated_consumption')
        fuel = curr_se.get('fuel_consumption')
        distance_calculated = curr_se.get('distance')
        submition_date = datetime.datetime.now()
        miles_or_kilometers = curr_se.get('is_kilometers')

        instanced_object = UserQueryLogs(username=username,
                                         query_city_1=city_1_address,
                                         query_city_2=city_2_address,
                                         coordinates_1=city_1_coords,
                                         coordinates_2=city_2_coords,
                                         fuel_consumption=fuel,
                                         is_kilometers=miles_or_kilometers,
                                         result=result_calculation,
                                         calculated_distance=distance_calculated,
                                         submition_date=submition_date
                                         )
        instanced_object.save()


def check_if_in_session(dict_name, request):
    return dict_name in request.session
