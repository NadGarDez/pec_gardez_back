from rest_framework_simplejwt.tokens import AccessToken
from .models import User_Info

def get_user_id_from_token(token):
    token_object = AccessToken(token)
    return token_object['user_id']

def get_token_from_headers(headers):
    authorization = headers['Authorization']
    new_string = authorization.split("Bearer ")
    return new_string[1]

def get_user_info_from_user_id(id):
    return User_Info.objects.get(user = id)

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
