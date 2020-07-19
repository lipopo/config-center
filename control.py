from typing import List

from model import Config


class Controller:
    pass


class ConfigController(Controller):

    def get(self, config_name: str = None):
        """获取模型数据
        """
        if config_name is None:
            configs = Config.select()
            data = []
            for config in configs:
                data.append(
                    {
                        "config_name": config.config_name,
                        "config_type": config.config_type,
                        "config_value": config.config_value
                    }
                )
        else:
            config = Config.select().where(
                Config.config_name == config_name).get()
            data = {
                "config_name": config.config_name,
                "config_type": config.config_type,
                "config_value": config.config_value
            }
        return {
            "success": True,
            "data": data
        }

    def put(self, config_name: str, config_type: str, config_value: str):
        """更新模型数据
        """
        config_instance = Config.select().where(
            Config.config_name == config_name).get()
        if config_type is not None:
            config_instance.config_type = config_type
        if config_value is not None:
            config_instance.config_value = config_value
        config_instance.save()
        return {
            "success": True,
            "data": {
                "config_name": config_name,
                "config_type": config_type,
                "config_value": config_value
            }
        }

    def post(self, config_name: str, config_type: str, config_value: str):
        """创建模型数据
        """
        print(config_name, config_type, config_value)
        Config.create(
            config_name=config_name,
            config_type=config_type,
            config_value=config_value)
        return {
            "success": True,
            "data": {
                "config_name": config_name,
                "config_type": config_type,
                "config_value": config_value
            }
        }

    def delete(self, config_names: List[str] = []):
        """删除模型数据
        """
        configs = []

        for name in config_names:
            _config = Config.select().where(
                Config.config_name == name).get()
            configs.append(_config)

        for _config in configs:
            _config.delete_instance()

        return {
            "success": True,
            "data": config_names
        }
