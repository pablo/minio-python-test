ACCESS_KEY="my-access-key"
SECRET_KEY="my-secret-key"

try:
    from local_config import *
except ImportError as e:
    pass
