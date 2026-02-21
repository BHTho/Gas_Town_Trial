// IoT Asset Management SaaS - MongoDB Initialization
// Version 1.1

db = db.getSiblingDB('iot_assets');

// Create sensor_readings collection if it doesn't exist
if (!db.getCollectionNames().includes('sensor_readings')) {
    db.createCollection('sensor_readings');
}

// Create indexes for sensor_readings collection
db.sensor_readings.createIndex(
    { sensor_id: 1, timestamp: -1 },
    { name: 'sensor_timestamp_idx' }
);

db.sensor_readings.createIndex(
    { asset_model_key: 1, timestamp: -1 },
    { name: 'asset_model_timestamp_idx' }
);

db.sensor_readings.createIndex(
    { is_faulty: 1, sensor_id: 1 },
    { name: 'faulty_sensor_idx' }
);

db.sensor_readings.createIndex(
    { asset_fault_detected: 1, asset_id: 1 },
    { name: 'asset_fault_idx' }
);

// TTL index for data retention (30 days by default)
// Can be adjusted per subscription tier
db.sensor_readings.createIndex(
    { timestamp: 1 },
    {
        name: 'timestamp_ttl_idx',
        expireAfterSeconds: 2592000 // 30 days
    }
);

// Create other collections that might be needed
if (!db.getCollectionNames().includes('asset_models')) {
    db.createCollection('asset_models');
}

// Index for asset_models lookup
db.asset_models.createIndex(
    { manufacturer: 1, make: 1, model: 1, year: 1 },
    { name: 'manufacturer_make_model_year_idx', unique: true }
);

print('MongoDB initialization complete.');