import os, urlparse

REALM = "{{cfg.realm}}"
DEBUG = {{cfg.debug}}

PORT_NUMBER = {{cfg.http.listen.port}}

ENABLE_CORS = {{cfg.enable_cors}}
CORS_ORIGINS = "{{cfg.cors_origins}}"

FLASK_SESSION_SECRET_KEY = "{{cfg.flask_session_secret_key}}"

BIN_TTL = {{cfg.bin_ttl}}
STORAGE_BACKEND = "requestbin.storage.redis.RedisStorage"
MAX_RAW_SIZE = {{cfg.max_raw_size}}
IGNORE_HEADERS = "{{strJoin cfg.ignore_headers ","}}".split(",")
MAX_REQUESTS = {{cfg.max_requests}}
CLEANUP_INTERVAL = {{cfg.cleanup_interval}}

REDIS_URL = "http://127.0.0.1:{{bind.redis.first.cfg.port}}"
REDIS_HOST = "127.0.0.1"
REDIS_PORT = {{bind.redis.first.cfg.port}}
REDIS_PASSWORD = None
REDIS_DB = {{cfg.redis.db}}

REDIS_PREFIX = "{{cfg.redis.prefix}}"

BUGSNAG_KEY = "{{cfg.bugsnag_key}}"
