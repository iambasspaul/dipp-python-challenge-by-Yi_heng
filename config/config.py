"""
Configuration Module
"""

__all__ = [
    'DevelopmentConfig',
    'TestConfig',
    'ProductionConfig',
    'get_config'
]


class Config:
    """
    Default configuration
    """
    HOST = '127.0.0.1'
    PORT = 3030
    API_HOST = 'http://localhost'
    API_VERSION = 'v1'
    API_BASE_PATH = 'api/{}'.format(API_VERSION)
    API_URL = '{}:{}/{}'.format(API_HOST, PORT, API_BASE_PATH)
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'ThisIsNotASecret'
    OUTPUT_DIR = 'output/'


class DevelopmentConfig(Config):
    """
    Development environment configuration
    """
    DEBUG = True


class TestConfig(Config):
    """
    Test environment configuration
    """
    TESTING = True


class ProductionConfig(Config):
    """
    Production environment configuration
    """
    SECRET_KEY = 'ThisIsNotASecret'


def get_config(env):
    """
    Get specific environment specific config
    """
    switch = {
        'development': DevelopmentConfig,
        'test': TestConfig,
        'production': ProductionConfig
    }
    return switch[env]
