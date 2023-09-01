{{ config(materialized='table') }}

WITH standardized_data AS (
  SELECT 
    'Bordeaux' AS city_name,
    dt,
    main_temp,
    main_humidity,
    wind_speed
 FROM  {{ source('sourcesilver','bordeauxsilver') }}
  
  UNION ALL
  
  SELECT 
    'Montreal' AS city_name,
    dt,
    main_temp,
    main_humidity,
    wind_speed
  FROM  {{ source('sourcesilver','montrealsilver') }}
  
  UNION ALL
  
  SELECT 
    'Paris' AS city_name,
    dt,
    main_temp,
    main_humidity,
    wind_speed
  FROM  {{ source('sourcesilver','parissilver') }}
  
  UNION ALL
  
  SELECT 
    'Rennes' AS city_name,
    dt,
    main_temp,
    main_humidity,
    wind_speed
  FROM  {{ source('sourcesilver','rennessilver') }}
)
SELECT 
  dt,
  MAX(CASE WHEN city_name = 'Bordeaux' THEN main_temp END) AS main_temp_bordeaux,
  MAX(CASE WHEN city_name = 'Bordeaux' THEN main_humidity END) AS main_humidity_bordeaux,
  MAX(CASE WHEN city_name = 'Bordeaux' THEN wind_speed END) AS wind_speed_bordeaux,
  MAX(CASE WHEN city_name = 'Montreal' THEN main_temp END) AS main_temp_montreal,
  MAX(CASE WHEN city_name = 'Montreal' THEN main_humidity END) AS main_humidity_montreal,
  MAX(CASE WHEN city_name = 'Montreal' THEN wind_speed END) AS wind_speed_montreal,
  MAX(CASE WHEN city_name = 'Paris' THEN main_temp END) AS main_temp_paris,
  MAX(CASE WHEN city_name = 'Paris' THEN main_humidity END) AS main_humidity_paris,
  MAX(CASE WHEN city_name = 'Paris' THEN wind_speed END) AS wind_speed_paris,
  MAX(CASE WHEN city_name = 'Rennes' THEN main_temp END) AS main_temp_rennes,
  MAX(CASE WHEN city_name = 'Rennes' THEN main_humidity END) AS main_humidity_rennes,
  MAX(CASE WHEN city_name = 'Rennes' THEN wind_speed END) AS wind_speed_rennes
FROM standardized_data
GROUP BY dt
ORDER BY dt



