from os import environ

APP_VERSION = "v1.0.0 beta 22"
LCM_DEFAULT_MODEL = "stabilityai/sdxl-turbo"
LCM_DEFAULT_MODEL_OPENVINO = "rupeshs/sd-turbo-openvino"
APP_NAME = "Image generation"
APP_SETTINGS_FILE = "settings.yaml"
RESULTS_DIRECTORY = "results"
CONFIG_DIRECTORY = "configs"
DEVICE = environ.get("DEVICE", "cpu")
SD_MODELS_FILE = "stable-diffusion-models.txt"
LCM_LORA_MODELS_FILE = "lcm-lora-models.txt"
OPENVINO_LCM_MODELS_FILE = "openvino-lcm-models.txt"
TAESD_MODEL = "madebyollin/taesd"
TAESDXL_MODEL = "madebyollin/taesdxl"
TAESD_MODEL_OPENVINO = "deinferno/taesd-openvino"
LCM_MODELS_FILE = "lcm-models.txt"
TAESDXL_MODEL_OPENVINO = "rupeshs/taesdxl-openvino"
