from django import forms

from GeoApp.models import UserQueryLogs


# class QueryForm(forms.ModelForm):
#
#     country=forms.ModelChoiceField(empty_label='select a country',queryset=distinct_countries(),required=False,widget=forms.Select(attrs={"onChange":'submit()'}))
#     sub_country=forms.ModelChoiceField(empty_label='select state',queryset=WorldData.objects.none(),required=False,widget=forms.Select(attrs={"onChange":'submit()'}))
#     city=forms.ModelChoiceField(empty_label='select a city',queryset=WorldData.objects.none(), required=False, widget=forms.Select(attrs={"onChange":'submit()'}))
#     def __init__(self, country='',sub_country='', **kwargs):
#         super(QueryForm, self).__init__(**kwargs)
#         if country!='':
#             self.fields['sub_country'].queryset = distinct_filtered_sub_countries(country)
#         if sub_country!='':
#             self.fields['city'].queryset=filtered_cities_only_by_county(sub_country)
#
#     class Meta:
#         model = UserQueryLogs
#         fields = ['country','sub_country','city']
#         attrs={'onchange': 'this.form.submit();'}
#         #'world_dat_query_cities','world_dat_query_countries','world_dat_query_sub_countries'
class QueryForm(forms.ModelForm):
    class Meta:
        model = UserQueryLogs
        fields = ['fuel_consumption', 'query_city_1', 'query_city_2', 'is_kilometers']
