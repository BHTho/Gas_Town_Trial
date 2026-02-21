from src.database import mongo_db

def create_indexes():
    """Create MongoDB indexes for collections as per mongo-init.js"""

    # sensor_readings collection indexes
    sensor_readings = mongo_db.sensor_readings
    sensor_readings.create_index(
        [("sensor_id", 1), ("timestamp", -1)],
        name="sensor_timestamp_idx"
    )
    sensor_readings.create_index(
        [("asset_model_key", 1), ("timestamp", -1)],
        name="asset_model_timestamp_idx"
    )
    sensor_readings.create_index(
        [("is_faulty", 1), ("sensor_id", 1)],
        name="faulty_sensor_idx"
    )
    sensor_readings.create_index(
        [("asset_fault_detected", 1), ("asset_id", 1)],
        name="asset_fault_idx"
    )
    # TTL index for data retention (30 days by default)
    sensor_readings.create_index(
        [("timestamp", 1)],
        name="timestamp_ttl_idx",
        expireAfterSeconds=2592000  # 30 days
    )

    # asset_models collection index
    asset_models = mongo_db.asset_models
    asset_models.create_index(
        [("manufacturer", 1), ("make", 1), ("model", 1), ("year", 1)],
        name="manufacturer_make_model_year_idx",
        unique=True
    )

    print("MongoDB indexes created successfully")

if __name__ == "__main__":
    create_indexes()