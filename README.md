# IoT Asset Management SaaS - Database Schemas

This project defines database structures for an IoT Asset Management SaaS using SQLAlchemy (PostgreSQL) and MongoDB with appropriate indexes.

## Schema Overview

The database schema supports multi-tenant IoT asset management with organisations, users, assets, sensors, alarms, notifications, and a marketplace for data sharing.

### PostgreSQL Tables (SQLAlchemy Models)

- **organisations**: Multi-tenancy container with subscription tiers
- **users**: OAuth-authenticated users with roles
- **organisation_members**: Membership with roles and permissions
- **assets**: IoT devices with manufacturer/model metadata
- **sensors**: Sensors attached to assets with API keys
- **sensor_labels**: User-assigned labels for sensors
- **sensor_alarms**: Threshold-based alarm configurations
- **notifications**: Alarm-triggered notifications to users
- **marketplace_listings**: Asset data listings for sale
- **marketplace_purchases**: Purchase records
- **audit_logs**: Admin action audit trail

### MongoDB Collections

- **sensor_readings**: Time-series sensor data with TTL index (30 days retention)
- **asset_models**: Normalized asset model catalog

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Copy environment file:
   ```bash
   cp .env.example .env
   ```

3. Update `.env` with your PostgreSQL and MongoDB connection strings.

4. Initialize databases:
   ```bash
   python scripts/init_db.py
   ```

This will create PostgreSQL tables and MongoDB indexes.

## Configuration

- `DATABASE_URL`: PostgreSQL connection URL (default: `postgresql://postgres:postgres@localhost:5432/iot_assets`)
- `MONGODB_URL`: MongoDB connection string (default: `mongodb://localhost:27017`)
- `MONGODB_DB`: MongoDB database name (default: `iot_assets`)

## Usage

Import models from `src.models` and use `SessionLocal` from `src.database` for SQL operations.

Use `mongo_db` from `src.database` for MongoDB operations.

## Schema Details

See `scripts/init-dbs.sql` and `scripts/mongo-init.js` for raw SQL and MongoDB initialization scripts.

## Development

Add new SQLAlchemy models in `src/models/` and ensure they are imported in `src.models.__init__.py`.

Add new MongoDB indexes in `src/mongodb/indexes.py`.