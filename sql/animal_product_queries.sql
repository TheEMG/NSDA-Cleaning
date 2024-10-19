USE animal_products_db;
-- GENERAL QUERIES ---------------------------------------------
SELECT COUNT(*) as total_entries FROM animal_products;

SELECT *
FROM animal_products20 -- Change based on the chunk you want
LIMIT 100;

SELECT DISTINCT GROUP_DESC, COMMODITY_DESC, CLASS_DESC
FROM animal_products20-- Change based on the chunk you want
ORDER BY GROUP_DESC, COMMODITY_DESC, CLASS_DESC;

SELECT DISTINCT
    STATISTICCAT_DESC,
    UNIT_DESC
FROM animal_products
WHERE 
    COMMODITY_DESC = 'CATTLE' 
    AND FREQ_DESC = 'ANNUAL'
ORDER BY 
    STATISTICCAT_DESC,
    UNIT_DESC;
-- GENERAL QUERIES END ---------------------------------------------

/*SAVE THE RESULTS OF RUNNING THE FOLLOWING QUERIES FOR EACH CHUNK INTO A DIRECTORY AS DEMONSTRATED IN THE DIRECTORY STRUCTURE
	EXAMPLE cattle_inventory for queries over cattle 
    OR 
    EXAMPLE chicken_data for chunks over chicken 
*/
-- Total cattle inventory on state level and NOT national level 
SELECT 
    YEAR, 
    COALESCE(NULLIF(STATE_NAME, ''), 'UNKNOWN') AS STATE_NAME,
    COMMODITY_DESC,
    STATISTICCAT_DESC,
    UNIT_DESC,
    SUM(VALUE) AS total_cattle_value
FROM animal_products
WHERE 
    COMMODITY_DESC = 'CATTLE' 
    AND FREQ_DESC = 'ANNUAL' 
    AND STATE_NAME != 'US TOTAL'
GROUP BY 
    YEAR, 
    COALESCE(NULLIF(STATE_NAME, ''), 'UNKNOWN'),
    COMMODITY_DESC,
    STATISTICCAT_DESC,
    UNIT_DESC
ORDER BY 
    YEAR, 
    STATE_NAME;

-- Total chicken on state level and NOT national level 
SELECT 
    YEAR, 
    STATE_NAME, 
    COMMODITY_DESC, 
    STATISTICCAT_DESC, 
    UNIT_DESC, 
    SUM(VALUE) AS total_value
FROM animal_products20
WHERE COMMODITY_DESC = 'CHICKENS'
AND FREQ_DESC = 'ANNUAL'
AND VALUE != '(D)'
GROUP BY 
    YEAR, 
    STATE_NAME, 
    COMMODITY_DESC, 
    STATISTICCAT_DESC, 
    UNIT_DESC
ORDER BY 
    YEAR, 
    STATE_NAME;