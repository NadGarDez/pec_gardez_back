from rest_framework_simplejwt.tokens import AccessToken

def get_user_id_from_token(token):
    token_object = AccessToken(token)
    return token_object['user_id']