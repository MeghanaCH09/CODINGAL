    CREATE TABLE supplier (
    SNO TEXT PRIMARY KEY, 
    SNAME TEXT, 
    STATUS INTEGER, 
    CITY TEXT
);

INSERT INTO supplier (SNO, SNAME, STATUS, CITY) VALUES
('S1', 'Hashmatullah Shahidi', 30, 'Afghanistan'),
('S2', 'Pat Cummins', 31, 'Australia'),
('S3', 'Najmul Hossain Shanto', 26, 'Bangladesh'),
('S4', 'Jos Buttler', 34, 'England'),
('S5', 'Rohit Sharma', 37, 'India'),
('S6', 'Mitchel Santner', 33, 'New Zealand'),
('S7', 'Mohammad Rizwan', 32, 'Pakistan'),
('S8', 'Aiden Markram', 30, 'South Africa'),
('S9', 'Charith Asalanka', 27, 'Sri Lanka'),
('S10', 'Rovman Powell', 31, 'West Indies');

SELECT * FROM supplier