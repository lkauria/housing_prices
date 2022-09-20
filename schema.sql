CREATE TABLE sold_apartment (
    id SERIAL PRIMARY KEY, 
    street_address TEXT, 
    apartment_number INTEGER, 
    stairwell TEXT, 
    zip_code TEXT, 
    selling_price DOUBLE PRECISION, 
    squares_m2 INTEGER, 
    housing_company_code TEXT, 
    sales_date DATE, 
    user_id TEXT,
    date timestamp NOT NULL DEFAULT NOW()
);

CREATE TABLE housing_company (
    company_code TEXT PRIMARY KEY, 
    street_address TEXT, 
    zip_code TEXT, 
    construction_year INTEGER, 
    last_pipe_renovation_year INTEGER, 
    date timestamp NOT NULL DEFAULT NOW()
);

CREATE TABLE postal_area (
    zip_code TEXT PRIMARY KEY,
    postal_area_name TEXT,
    municipality TEXT,
    region TEXT,
    country TEXT,
    date timestamp NOT NULL DEFAULT NOW()
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY, 
    username TEXT,
    first_name TEXT,
    last_name TEXT,
    role TEXT, 
    password TEXT
);
