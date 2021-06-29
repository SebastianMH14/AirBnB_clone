"""Creating a class base model"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base model class"""

    def __init__(self, *args, **kwargs):
        """Initialization of the base model"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "create_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String representation of the class itself."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """updates the attribute 'updated_at' with the current time"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a new dic with the class values"""
        self.__dict__["__class__"] = __class__.__name__
        self.__dict__["created_at"] = self.created_at.isoformat()
        self.__dict__["updated_at"] = self.updated_at.isoformat()

        return self.__dict__
