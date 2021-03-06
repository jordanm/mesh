SCHEME_PARAMETERS = {'readonly': False, 'deferred': False, 'sortable': False, 'operators': None}
RETURNING = 'returning'

INHERIT = 'inherit'

DELETE = 'DELETE'
GET = 'GET'
HEAD = 'HEAD'
LOAD = 'LOAD'
OPTIONS = 'OPTIONS'
POST = 'POST'
PUT = 'PUT'

HTTP_METHODS = (DELETE, GET, HEAD, OPTIONS, POST, PUT)

OK = 'OK'
CREATED = 'CREATED'
ACCEPTED = 'ACCEPTED'
SUBSET = 'SUBSET'
PARTIAL = 'PARTIAL'

VALID_STATUS_CODES = (OK, CREATED, ACCEPTED, SUBSET, PARTIAL)

BAD_REQUEST = 'BAD_REQUEST'
FORBIDDEN = 'FORBIDDEN'
NOT_FOUND = 'NOT_FOUND'
METHOD_NOT_ALLOWED = 'METHOD_NOT_ALLOWED'
INVALID = 'INVALID'
TIMEOUT = 'TIMEOUT'
CONFLICT = 'CONFLICT'
GONE = 'GONE'

SERVER_ERROR = 'SERVER_ERROR'
UNIMPLEMENTED = 'UNIMPLEMENTED'
BAD_GATEWAY = 'BAD_GATEWAY'
UNAVAILABLE = 'UNAVAILABLE'

ERROR_STATUS_CODES = (BAD_REQUEST, FORBIDDEN, NOT_FOUND, METHOD_NOT_ALLOWED, INVALID, TIMEOUT,
    CONFLICT, GONE, SERVER_ERROR, UNIMPLEMENTED, BAD_GATEWAY, UNAVAILABLE)

STATUS_CODES = tuple(list(VALID_STATUS_CODES) + list(ERROR_STATUS_CODES))

JSON = 'application/json'
URLENCODED = 'application/x-www-form-urlencoded'

__all__ = [name for name in locals().keys() if name.upper() == name and not name.startswith('_')]
