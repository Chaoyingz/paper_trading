HOST="127.0.0.1"
PORT=5000

.PHONY: server debug test

default:
	@echo "帮助:"
	@echo "\tmake server 启动服务器"
	@echo "\tmake debug 启动调试服务器"

server:
    export FLASK_DEBUG=False
server:
	poetry run gunicorn "paper_trading.app:create_app()" -b $(HOST):$(PORT)

debug:
    export FLASK_DEBUG=True
debug:
	poetry run gunicorn "paper_trading.app:create_app()" -b $(HOST):$(PORT) --reload