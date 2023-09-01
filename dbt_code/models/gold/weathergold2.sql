{{ config(materialized='table') }}

WITH standardized_data AS (
  SELECT 
    'Bordeaux' AS city_name,
    dt,
    main_temp,
    main_humidity,
    main_pressure,
    clouds,
    wind_speed
  FROM  {{ source('sourcesilver','bordeauxsilver') }}
  
  UNION ALL
  
  SELECT 
    'Montreal' AS city_name,
    dt,
    main_temp,
    main_humidity,
    main_pressure,
    clouds,
    wind_speed
  FROM  {{ source('sourcesilver','montrealsilver') }}

  
  UNION ALL
  
  SELECT 
    'Paris' AS city_name,
    dt,
    main_temp,
    main_humidity,
    main_pressure,
    clouds,
    wind_speed
  FROM  {{ source('sourcesilver','parissilver') }}

  
  UNION ALL
  
  SELECT 
    'Rennes' AS city_name,
    dt,
    main_temp,
    main_humidity,
    main_pressure,
    clouds,
    wind_speed
  FROM  {{ source('sourcesilver','rennessilver') }}

)
SELECT 
  dt,
  main_temp,
  CAST(main_humidity) AS DOUBLE,
  CAST(main_pressure) AS DOUBLE,
  CAST(clouds) AS DOUBLE,
  CAST(wind_speed) AS DOUBLE,
  city_name
FROM standardized_data
ORDER BY dt