class CustomUser:
    def __init__(self, user_data):
        self.user_data = user_data

    def __getattr__(self, attr):
        # Access user_data attributes like a regular object
        return self.user_data.get(attr, None)

    @property
    def is_authenticated(self):
        # Always return True, since the token has already been verified
        return True

    def get(self, key, default=None):
        return self.user_data.get(key, default)

    @property
    def id(self):
        # Assume 'id' exists in user_data
        return self.user_data.get('id')

    @property
    def username(self):
        # Assume 'username' exists in user_data
        return self.user_data.get('username')
