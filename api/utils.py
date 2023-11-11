from rest_framework_simplejwt.tokens import AccessToken
from .models import User_Info
from datetime import date, timedelta

def get_user_id_from_token(token):
    token_object = AccessToken(token)
    return token_object['user_id']

def get_token_from_headers(headers):
    authorization = headers['Authorization']
    new_string = authorization.split("Bearer ")
    return new_string[1]

def get_user_info_from_user_id(id):
    return User_Info.objects.get(user = id)

def get_user_info_from_headers(headers):
    token = get_token_from_headers(headers)
    user_id = get_user_id_from_token(token=token)
    user_info = get_user_info_from_user_id(user_id)
    return user_info

def filter_results_depending_on_role(headers, admin_action, client_action, psico_action):
    authorization = headers['Authorization']
    new_string = authorization.split("Bearer ")
    current_request_user_id = get_user_id_from_token(new_string[1])
    
    user_info = User_Info.objects.get(user = current_request_user_id)

    if user_info.role.role_name == 'admin':
        return admin_action(user_info)
       
    elif user_info.role.role_name == 'client':
        return client_action(user_info)
       
    else:
        return psico_action(user_info)

def num_of_days(start_date, end_date):
    date_a = date.fromisoformat(start_date)
    date_b = date.fromisoformat(end_date)

    return (date_b-date_a).days + 1

def dates_array(num_of_days, start_date):
    days = list()
    current_date=date.fromisoformat(start_date)
    for i in range(num_of_days):
        if i > 0:
            delta = timedelta(days=1)
            current_date = current_date + delta
            
        days.append(current_date)
    return days

