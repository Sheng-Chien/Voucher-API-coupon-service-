-- =======================================
-- Coupon Service - Database Initialization
-- =======================================

DROP TABLE IF EXISTS coupons;

CREATE TABLE coupons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code VARCHAR(50) NOT NULL UNIQUE,
    discount INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Seed data
INSERT INTO coupons (code, discount, is_active) VALUES
('WELCOME10', 10, 1),
('SUMMER20', 20, 1),
('VIP50', 50, 0);
