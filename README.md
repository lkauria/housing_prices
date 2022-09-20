# Housing prices

This tool is for real estate agents to add prices for their sold 
real estates to get statistics on postal areas actual prices. This is also for common users to see the price level on average.

The production version can be found in Heroku: https://tsoha-housing-prices.herokuapp.com/
 
## Realtors can:
- register to housing prices tool
- login 
- add prices and other information of the sold real estate
- see statistics of sold real estate by zip code
TO DO: 
- change information that they've added

## Admin can:
- register/login
- remove/add/change a housing company
- remove/add/change postal code area  


## database tables

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
