from flask import Flask, jsonify, request, Response
from peewee import DoesNotExist, IntegrityError

from control import ConfigController


app = Flask(
    __name__,
    static_url_path="/static/",
    static_folder="static/")


@app.after_request
def cross_origin(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    return response


@app.route("/config")
def get_config():
    """获取配置项
    """
    controller = ConfigController()
    data = controller.get(request.args.get("config_name", None))
    return jsonify(data)


@app.route("/config", methods=["POST"])
def create_config():
    """创建配置项目
    """
    data = request.json
    controller = ConfigController()
    redata = controller.post(
        config_name=data.get("config_name"),
        config_type=data.get("config_type"),
        config_value=data.get("config_value")
    )
    return jsonify(redata)


@app.route("/config", methods=["PUT"])
def update_config():
    """更新配置项目
    """
    data = request.json
    controller = ConfigController()
    redata = controller.put(
        data.get("config_name"),
        data.get("config_type"),
        data.get("config_value")
    )
    return redata


@app.route("/config", methods=["DELETE"])
def delete_config():
    """删除配置项目
    """
    config_names = request.json.get("config_names")
    controller = ConfigController()
    redata = controller.delete(config_names)
    return redata


@app.route("/config", methods=["OPTIONS"])
def options_method():
    """Request from Front
    """
    res = Response(headers={
        "Allow": ["GET", "POST", "PUT", "DELETE", "OPTIONS"]
    })
    return res


@app.errorhandler(DoesNotExist)
def record_do_not_exist(exception):
    return {
        "success": True,
        "data": None
    }


@app.errorhandler(IntegrityError)
def record_already_created(exception):
    return {
        "success": False
    }


if __name__ == "__main__":
    app.run(debug=True)
