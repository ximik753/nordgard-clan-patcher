from requests import get


class Offsets:
    try:
        offset = get(
            "https://raw.githubusercontent.com/ximik753/nordgard-clan-patcher/refs/heads/master/offsets/northgard.json"
        ).json()

        base = offset["base"]
    except:
        exit("Error: Invalid offsets, wait for an update")
