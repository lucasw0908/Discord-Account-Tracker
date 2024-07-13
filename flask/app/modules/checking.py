import re
from base64 import b64decode
from datetime import datetime


def is_token(token: str) -> tuple[bool, dict]:
    """
    Parameters
    ----------
    token: :type:`str`
        The token to check.
        
    Returns
    -------
    valid: :type:`bool`
        True if the token is valid, otherwise False.
    data: :type:`dict`
        The data extracted from the token.
    """
    
    data = {}
    pattern = re.compile(r"[0-9A-Za-z]+\.[0-9A-Za-z]+\.[0-9A-Za-z]+")
    if pattern.match(token) is not None:
        userid, timestamp, hmac = pattern.match(token).group().split(".")
        try:
            userid = b64decode(userid)
            timestamp = b64decode(timestamp)
        except Exception:
            return False, data
        
        if re.search(r"\d{18}", userid) is not None:
            data["userid"] = userid
            
        if re.search(r"\d+", timestamp) is not None:
            data["timestamp"] = datetime.fromtimestamp(int(timestamp) + 1293840000).strftime("%Y-%m-%d %H:%M:%S")
            
        data["hmac"] = hmac
        
        if len(data.values()) == 3:
            return True, data

    return False, data