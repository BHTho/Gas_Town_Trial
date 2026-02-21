-- IoT Asset Management SaaS - PostgreSQL Schema Initialization
-- Version 1.1

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Organizations
CREATE TABLE organisations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(255) NOT NULL,
    billing_customer_id VARCHAR(255),
    subscription_tier VARCHAR(50) DEFAULT 'free',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Users
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    oauth_provider VARCHAR(50) NOT NULL,
    oauth_subject VARCHAR(255) NOT NULL,
    display_name VARCHAR(255),
    is_super_user BOOLEAN DEFAULT FALSE,
    is_site_owner BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(oauth_provider, oauth_subject)
);

-- Organization Members
CREATE TABLE organisation_members (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    organisation_id UUID NOT NULL REFERENCES organisations(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    role VARCHAR(50) NOT NULL CHECK (role IN ('owner', 'admin', 'worker', 'viewer')),
    permissions JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(organisation_id, user_id)
);

-- Assets
CREATE TABLE assets (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    organisation_id UUID REFERENCES organisations(id) ON DELETE CASCADE,
    owner_user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    manufacturer VARCHAR(255),
    make VARCHAR(255),
    model VARCHAR(255),
    year INTEGER,
    serial_number VARCHAR(255),
    asset_model_key VARCHAR(500), -- normalized: manufacturer+make+model+year
    data_sharing_enabled BOOLEAN DEFAULT FALSE,
    metadata JSONB DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Sensors
CREATE TABLE sensors (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    asset_id UUID NOT NULL REFERENCES assets(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    sensor_type VARCHAR(100) NOT NULL,
    sensor_manufacturer VARCHAR(255),
    sensor_model VARCHAR(255),
    accuracy_class VARCHAR(50) CHECK (accuracy_class IN ('low', 'medium', 'high', 'industrial')),
    unit VARCHAR(50) NOT NULL,
    api_key_hash VARCHAR(255) NOT NULL, -- hashed API key
    ingest_endpoint_slug VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Sensor Labels
CREATE TABLE sensor_labels (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    sensor_id UUID NOT NULL REFERENCES sensors(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    label VARCHAR(100) NOT NULL,
    colour VARCHAR(7), -- hex color code
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(sensor_id, label)
);

-- Sensor Alarms
CREATE TABLE sensor_alarms (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    sensor_id UUID NOT NULL REFERENCES sensors(id) ON DELETE CASCADE,
    created_by_user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    name VARCHAR(255) NOT NULL,
    condition VARCHAR(10) NOT NULL CHECK (condition IN ('above', 'below', 'equals')),
    threshold DOUBLE PRECISION NOT NULL,
    notify_email VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    triggered_state BOOLEAN DEFAULT FALSE,
    last_triggered_at TIMESTAMP WITH TIME ZONE,
    last_reset_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Notifications
CREATE TABLE notifications (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    alarm_id UUID REFERENCES sensor_alarms(id) ON DELETE SET NULL,
    sensor_id UUID NOT NULL REFERENCES sensors(id) ON DELETE CASCADE,
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    reading_value DOUBLE PRECISION NOT NULL,
    threshold DOUBLE PRECISION NOT NULL,
    condition VARCHAR(10) NOT NULL CHECK (condition IN ('above', 'below', 'equals')),
    message TEXT NOT NULL,
    is_read BOOLEAN DEFAULT FALSE,
    email_sent BOOLEAN DEFAULT FALSE,
    triggered_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Marketplace Listings
CREATE TABLE marketplace_listings (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    asset_id UUID NOT NULL REFERENCES assets(id) ON DELETE CASCADE,
    organisation_id UUID REFERENCES organisations(id) ON DELETE CASCADE,
    listed_by_user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    price_per_1000_rows INTEGER NOT NULL CHECK (price_per_1000_rows >= 0),
    hidden_columns JSONB DEFAULT '[]',
    is_active BOOLEAN DEFAULT TRUE,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Marketplace Purchases
CREATE TABLE marketplace_purchases (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    listing_id UUID NOT NULL REFERENCES marketplace_listings(id) ON DELETE CASCADE,
    buyer_user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    buyer_organisation_id UUID REFERENCES organisations(id) ON DELETE SET NULL,
    row_count INTEGER NOT NULL CHECK (row_count > 0),
    gross_amount INTEGER NOT NULL CHECK (gross_amount >= 0),
    seller_fee_amount INTEGER NOT NULL CHECK (seller_fee_amount >= 0),
    buyer_fee_amount INTEGER NOT NULL CHECK (buyer_fee_amount >= 0),
    net_seller_amount INTEGER NOT NULL CHECK (net_seller_amount >= 0),
    polar_payment_id VARCHAR(255),
    status VARCHAR(50) NOT NULL CHECK (status IN ('pending', 'completed', 'refunded')) DEFAULT 'pending',
    purchased_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    download_expires_at TIMESTAMP WITH TIME ZONE
);

-- Audit Log (for site admin actions, especially impersonation)
CREATE TABLE audit_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    action VARCHAR(100) NOT NULL,
    actor_user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    target_user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    target_organisation_id UUID REFERENCES organisations(id) ON DELETE SET NULL,
    details JSONB DEFAULT '{}',
    ip_address INET,
    user_agent TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance
CREATE INDEX idx_organisation_members_user_id ON organisation_members(user_id);
CREATE INDEX idx_organisation_members_organisation_id ON organisation_members(organisation_id);
CREATE INDEX idx_assets_organisation_id ON assets(organisation_id);
CREATE INDEX idx_assets_owner_user_id ON assets(owner_user_id);
CREATE INDEX idx_assets_asset_model_key ON assets(asset_model_key);
CREATE INDEX idx_sensors_asset_id ON sensors(asset_id);
CREATE INDEX idx_sensors_api_key_hash ON sensors(api_key_hash);
CREATE INDEX idx_sensor_labels_sensor_id ON sensor_labels(sensor_id);
CREATE INDEX idx_sensor_alarms_sensor_id ON sensor_alarms(sensor_id);
CREATE INDEX idx_sensor_alarms_triggered_state ON sensor_alarms(triggered_state);
CREATE INDEX idx_notifications_user_id ON notifications(user_id);
CREATE INDEX idx_notifications_is_read ON notifications(is_read);
CREATE INDEX idx_marketplace_listings_asset_id ON marketplace_listings(asset_id);
CREATE INDEX idx_marketplace_listings_organisation_id ON marketplace_listings(organisation_id);
CREATE INDEX idx_marketplace_purchases_buyer_user_id ON marketplace_purchases(buyer_user_id);
CREATE INDEX idx_marketplace_purchases_listing_id ON marketplace_purchases(listing_id);
CREATE INDEX idx_audit_logs_actor_user_id ON audit_logs(actor_user_id);
CREATE INDEX idx_audit_logs_created_at ON audit_logs(created_at);

-- Function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Triggers for updated_at
CREATE TRIGGER update_organisations_updated_at BEFORE UPDATE ON organisations
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_users_updated_at BEFORE UPDATE ON users
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_assets_updated_at BEFORE UPDATE ON assets
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_sensors_updated_at BEFORE UPDATE ON sensors
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_sensor_alarms_updated_at BEFORE UPDATE ON sensor_alarms
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_marketplace_listings_updated_at BEFORE UPDATE ON marketplace_listings
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();