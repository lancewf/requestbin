import os, urlparse
DEBUG = True
REALM = os.environ.get('REALM', 'local')

{{#if cfg.http.listen.local_only ~}}
ROOT_URL = "http://127.0.0.1:{{cfg.http.listen.port}}"
{{else ~}}
ROOT_URL = "http://0.0.0.0:{{cfg.http.listen.port}}"
{{/if ~}}

PORT_NUMBER = {{cfg.http.listen.port}}

ENABLE_CORS = False
CORS_ORIGINS = "*"

FLASK_SESSION_SECRET_KEY = os.environ.get("SESSION_SECRET_KEY", "N1BKhJLnBqLpexOZdklsfDKFJDKFadsfs9a3r324YB7B73AglRmrHMDQ9RhXz35")

BIN_TTL = 48*3600
STORAGE_BACKEND = "requestbin.storage.redis.RedisStorage"
MAX_RAW_SIZE = int(os.environ.get('MAX_RAW_SIZE', 1024*10))
IGNORE_HEADERS = []
MAX_REQUESTS = 20
CLEANUP_INTERVAL = 3600

REDIS_URL = "http://127.0.0.1:6379"
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_DB = 9

REDIS_PREFIX = "requestbin"

BUGSNAG_KEY = ""
