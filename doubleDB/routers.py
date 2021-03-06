
class PrimaryRouter:
    def db_for_read(self, model, **hints):
        """
        Reads depending on type
        """
        return 'default'

    def db_for_write(self, model, **hints):
        """
        Writes always go to primary.
        """
        # print(hints['instance'].type)
        if hints['instance'].default_database:
            return 'default'
        else:
            return 'seconddb'

    def allow_relation(self, obj1, obj2, **hints):
        """
        For now nothing
        """
        return 'default'

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        All non-auth models end up in this pool.
        """
        return True


