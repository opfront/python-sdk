class Model(object):

    """
    Model represents a single resource instance (Ex: a specific Store)
    
    Args:
        resource (OpfrontResource): Resource that instantiated this model
        **attrs (dict): Attributes of the model
    """

    def __init__(self, resource, **attrs):
        self._res = resource
        self._existing_keys = dir(self)

        for attr_name, attr_value in attrs.items():
            setattr(self, attr_name, attr_value)

    def save(self):
        """
        Creates or updates the model
        
        Returns:
            Model: Updated model (with generated ID, if applicable)

        """
        if hasattr(self, 'id') and self._res.exists(self.id):
            # Update
            return self._res.update(self)

        # Create
        return self._res.create(self)

    def delete(self):
        """
        Deletes the model
        """
        if hasattr(self, 'id'):
            self._res.delete(self.id)
        else:
            # TODO: Raise warning here?
            # Error seems to harsh since deleting a non-existent resource isn't such a big deal
            pass

    @property
    def serialized(self):
        return {k: getattr(self, k) for k in dir(self) if k not in self._existing_keys and not k.startswith('_')}
