-- Create the cabs table
CREATE TABLE cabs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price_per_minute FLOAT NOT NULL
);

-- Insert sample data into cabs table (you can customize this)
INSERT INTO cabs (name, price_per_minute) VALUES 
    ('Cab 1', 0.5),
    ('Cab 2', 0.6),
    ('Cab 3', 0.7),
    ('Cab 4', 0.8),
    ('Cab 5', 0.9);

-- Create the bookings table
CREATE TABLE bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_email VARCHAR(255) NOT NULL,
    cab_id INT NOT NULL,
    source VARCHAR(255) NOT NULL,
    destination VARCHAR(255) NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    FOREIGN KEY (cab_id) REFERENCES cabs(id)
);

-- Insert sample data into bookings table (you can customize this)
INSERT INTO bookings (user_email, cab_id, source, destination, start_time, end_time) VALUES 
    ('user1@example.com', 1, 'A', 'B', '2023-10-17 08:00:00', '2023-10-17 08:15:00'),
    ('user2@example.com', 2, 'C', 'D', '2023-10-17 08:30:00', '2023-10-17 08:45:00'),
    ('user3@example.com', 3, 'E', 'F', '2023-10-17 09:00:00', '2023-10-17 09:30:00');

