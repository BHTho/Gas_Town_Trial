from src.database import mongo_db

def create_indexes():
    """Create MongoDB indexes for collections"""

    # logs collection indexes
    logs = mongo_db.logs
    logs.create_index([("timestamp", -1)], name="timestamp_desc")
    logs.create_index([("level", 1), ("timestamp", -1)], name="level_timestamp")
    logs.create_index([("service", 1), ("timestamp", -1)], name="service_timestamp")

    # events collection indexes
    events = mongo_db.events
    events.create_index([("event_type", 1), ("created_at", -1)], name="event_type_created_at")
    events.create_index([("user_id", 1), ("created_at", -1)], name="user_id_created_at")
    events.create_index([("session_id", 1)], name="session_id")

    # users collection for MongoDB (if used)
    users = mongo_db.users
    users.create_index([("email", 1)], unique=True, name="email_unique")
    users.create_index([("username", 1)], unique=True, name="username_unique")

    print("MongoDB indexes created successfully")

if __name__ == "__main__":
    create_indexes()