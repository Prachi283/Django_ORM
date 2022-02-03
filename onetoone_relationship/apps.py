from django.apps import AppConfig


class OnetooneRelationshipConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'onetoone_relationship'
    def ready(self):
        import onetoone_relationship.signals