from django.contrib.sites import requests
from django.shortcuts import render, redirect

import GeoAuthenticationApp
from GeoApp.forms import QueryForm
from GeoApp.models import UserQueryLogs
from GeoApp.scripts.acquired_data_management import geo_parameters_manage_distance, \
    calculate_and_store_consumption_result, manage_mode_and_parameters
from GeoApp.scripts.db_storage_management import pass_to_database
from GeoApp.scripts.geo_loc_finder import geo_data_acquire


# Create your views here.
def home(request=requests):
    user_queries = UserQueryLogs.objects.order_by('-submition_date')
    context = {
        'user_queries': user_queries,
    }
    if request.POST is not None:
        if 'delete_query_btn' in request.POST:
            id_instance = request.POST.get('delete_query_btn')
            print(id_instance)
            query = UserQueryLogs.objects.get(id=id_instance)
            query.delete()
    print(context)
    return render(request, "home.html", context)


def not_logged_in(request=requests):
    curr_se = request.session
    se_user = curr_se.get("user") or None
    if se_user is None or not se_user['is_authenticated']:
        return redirect(GeoAuthenticationApp.views.account_view)
    else:
        return redirect(home)


# Create your views here.
def geo(request):
    context = {
        "query_form": QueryForm
    }
    geo_data_acquire(request)
    manage_mode_and_parameters(request)
    geo_parameters_manage_distance(request)
    calculate_and_store_consumption_result(request)

    pass_to_database(request)

    return render(request, "geo_submit_templates/geo_start.html", context)
