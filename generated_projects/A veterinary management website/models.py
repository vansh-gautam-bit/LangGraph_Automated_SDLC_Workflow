Here's the `models.py` file for the `database_service`:

```python
# models.py

from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from typing import Optional

Base = declarative_base()

class User(Base):
    """User model."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    chatbot_interactions = relationship("ChatbotInteraction", backref="user")
    chatbot_performance = relationship("ChatbotPerformance", backref="user")

class ChatbotInteraction(Base):
    """Chatbot interaction model."""
    __tablename__ = "chatbot_interactions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    interaction_text = Column(Text, nullable=False)
    response_text = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default="NOW()")

class ChatbotPerformance(Base):
    """Chatbot performance model."""
    __tablename__ = "chatbot_performance"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    accuracy = Column(String, nullable=False)
    response_time = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default="NOW()")
```

And here's the `models.py` file for the `chatbot_service`:

```python
# models.py

from sqlalchemy import Column, Integer, String, Text, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from typing import Optional

Base = declarative_base()

class ChatbotInteraction(Base):
    """Chatbot interaction model."""
    __tablename__ = "chatbot_interactions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    interaction_text = Column(Text, nullable=False)
    response_text = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False, server_default="NOW()")

    user = relationship("User", backref="chatbot_interactions")
```

Note that we've defined the `ChatbotInteraction` model in both `models.py` files, as it's used by both services. We've also defined the relationships between the models, as specified in the requirements.

Also, note that we've used the `server_default` parameter to set the default value for the `created_at` column to the current timestamp. This is a PostgreSQL-specific feature.

Make sure to update the `__init__.py` files in the `database_service` and `chatbot_service` directories to import the `models` module:

```python
# __init__.py

from .models import *
```

This will make the models available to the rest of the application.