class Baseconfig:
    """Base Configuration"""
    TESTING = False


class DevelopmentConfig:
    """Development Configuration"""
    pass


class TestingConfig:
    """Test Config"""
    TESTING = True


class ProductionConfig:
    """Deployment Config"""
    pass
