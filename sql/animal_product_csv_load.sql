
/*
    Uncomment DROP and CREATE if needed 

*/
-- DROP SCHEMA IF EXISTS animal_products_db;
-- CREATE SCHEMA animal_products_db;
USE animal_products_db;

-- This would have to change for each chunk that has been created 
-- For example animal_products(1,2,3,etc)
DROP TABLE IF EXISTS animal_products2;

-- This allows null because at the start of this analysis we couldnt see all the entries 
-- So I allowed NUll values so mySQL wouldn't get the null value found error
CREATE TABLE animal_products2(
    SOURCE_DESC TEXT NULL,
    SECTOR_DESC TEXT NULL,
    GROUP_DESC TEXT NULL,
    COMMODITY_DESC TEXT NULL,
    CLASS_DESC TEXT NULL,
    PRODN_PRACTICE_DESC TEXT NULL,
    UTIL_PRACTICE_DESC TEXT NULL,
    STATISTICCAT_DESC TEXT NULL,
    UNIT_DESC TEXT NULL,
    SHORT_DESC TEXT NULL,
    DOMAIN_DESC TEXT NULL,
    DOMAINCAT_DESC TEXT NULL,
    AGG_LEVEL_DESC TEXT NULL,
    STATE_NAME TEXT NULL,
    COUNTY_NAME TEXT NULL,
    REGION_DESC TEXT NULL,
    LOCATION_DESC TEXT NULL,
    YEAR TEXT NULL,
    FREQ_DESC TEXT NULL,
    VALUE TEXT NULL,
    `CV_%` TEXT NULL
);

-- You would have to transfer the chunks directory into a similar directory as below
LOAD DATA INFILE 'C:\\ProgramData\\MySQL\\MySQL Server 8.3\\Uploads\\data_chunks\\qs_animals_products_chunk_2.csv' 
INTO TABLE animal_products2 -- CHANGE THIS BASED ON THE TABLE YOU CREATED , FOR EXAMPLE IF YOU ARE IN ANIMALS_PRODUCTS2 THIS SHOULD MATCH AS WELL (look at line 16 they should be the same )
FIELDS TERMINATED BY ','  -- Comma-separated values
ENCLOSED BY '"'  -- Handle values enclosed in double quotes
LINES TERMINATED BY '\n'  -- Newline as row delimiter
IGNORE 1 LINES  -- Skip the header row
(SOURCE_DESC, SECTOR_DESC, GROUP_DESC, COMMODITY_DESC, CLASS_DESC, 
PRODN_PRACTICE_DESC, UTIL_PRACTICE_DESC, STATISTICCAT_DESC, UNIT_DESC, 
SHORT_DESC, DOMAIN_DESC, DOMAINCAT_DESC, AGG_LEVEL_DESC, 
STATE_NAME, COUNTY_NAME, REGION_DESC, LOCATION_DESC, 
YEAR, FREQ_DESC, VALUE, @cv_percent)
SET `CV_%` = NULLIF(@cv_percent, '');  -- Convert empty fields to NULL