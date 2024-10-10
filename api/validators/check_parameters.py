from ..exceptions import CustomException, ErrorCode

def check_body(body, mandatory_keys):
    send_keys = []

    for key in body:
        send_keys.append(key)

    for key in mandatory_keys:
        if key not in send_keys or body[key] is None:
            raise CustomException(ErrorCode.MISSING_PARAMETERS, key)
 