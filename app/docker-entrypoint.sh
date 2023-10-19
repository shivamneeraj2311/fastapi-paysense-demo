#!sh

exec uvicorn \
    sparc_pay_api.server:server \
    --host 0.0.0.0 \
    --port 80 \
    --log-level debug \
    --no-access-log \
    --log-config uvicorn_disable_logging.json \
    --no-server-header \
    --proxy-headers
