import yaml
from box import Box

def get_config(path):
    """
    Загружает и возвращает конфигурацию из YAML-файла.

    Args:
        path (str): Путь к YAML-файлу с конфигурацией.

    Returns:
        Box: Конфигурация, загруженная из YAML-файла, обернутая в объект Box для удобного доступа.
    """
    with open(path, 'r') as f:
        config = yaml.safe_load(f)
    return Box(config)
