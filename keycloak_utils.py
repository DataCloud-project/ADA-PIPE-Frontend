from keycloak import KeycloakOpenID
from keycloak.exceptions import KeycloakAuthenticationError

import api_config


def _get_keycloak_open_id() -> KeycloakOpenID:
    return KeycloakOpenID(
        server_url=api_config.KEYCLOAK_SERVER_URL,
        client_id=api_config.KEYCLOAK_CLIENT_ID,
        realm_name=api_config.KEYCLOAK_REALM_NAME,
        client_secret_key=api_config.KEYCLOAK_SECRET_KEY
    )


__keycloak_open_id = _get_keycloak_open_id()


def _get_keycloak_token() -> dict:
    """Get the assigned KeyCloak token for the ADA-PIPE backend to be able to send requests to other DataCloud services.

    Returns:
        dict: the keycloak token for ADA-PIPE
    """
    token = __keycloak_open_id.token(
        api_config.KEYCLOAK_TOKEN_USERNAME,
        api_config.KEYCLOAK_TOKEN_PASSWORD)
    return token


def verify_keycloak_token(keycloak_token: dict) -> bool:
    """Verify a given KeyCloak token

    Args:
        keycloak_token (dict): a KeyCloak token to be verified

    Returns:
        bool:  returns True if the token could be verified by KeyCloak, else returns False
    """
    if keycloak_token is None or len(keycloak_token) == 0:
        return False
    if 'access_token' not in keycloak_token:
        return False
    try:
        keycloak_response = __keycloak_open_id.userinfo(
            keycloak_token['access_token'])

        if 'email_verified' not in keycloak_response or 'preferred_username' not in keycloak_response:
            return False

        return True

    except KeycloakAuthenticationError as err:
        # Token could not be verified
        print('Invalid Access Token', err)
        return False


def verify_access_token(access_token: str) -> bool:
    """Verify the (KeyCloak) access token of a service request.

    Args:
        access_token (str): the access token to be verified

    Returns:
        bool:  returns True if the token could be verified by KeyCloak, else returns False
    """
    if access_token is None or len(access_token) == 0:
        return False

    try:
        keycloak_response = __keycloak_open_id.userinfo(access_token)

        if 'email_verified' not in keycloak_response or 'preferred_username' not in keycloak_response:
            return False

        return True

    except KeycloakAuthenticationError as err:
        # Token could not be verified
        print('Invalid Access Token', err)
        return False
