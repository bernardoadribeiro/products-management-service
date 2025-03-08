import json
from flask import Flask, Response

app = Flask(__name__)
app.secret_key = settings.SECRET_KEY


@app.route("/health", methods=["GET"])
def health():
    return Response(
        response=json.dumps({"status": "up"}), status=200, mimetype="application/json"
    )


@app.route("/health/database", methods=["GET"])
def health_database():
    from products_api.core.database import mongodb

    try:
        ping = mongodb.sync_client.admin.command("ping")
        return Response(
            response=json.dumps({"status": "up", "ping": ping}),
            status=200,
            mimetype="application/json",
        )
    except Exception as e:
        return Response(
            response=json.dumps({"status": "down", "error": str(e)}),
            status=503,
            mimetype="application/json",
            headers={"Retry-After": 30},
        )
