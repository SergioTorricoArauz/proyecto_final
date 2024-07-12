class CustomAuthUser:
    def __init__(self, roles=None, groups=None):
        self.pk = 0
        self.username = ''
        self.is_authenticated = False
        self._groups = groups or []

    @property
    def groups(self):
        return self._groups

    @groups.setter
    def groups(self, value):
        self._groups = value

    def is_in_group(self, group_name):
        return group_name in self.groups
