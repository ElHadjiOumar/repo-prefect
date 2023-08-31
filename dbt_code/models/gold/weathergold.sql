{{ config(materialized='table') }}

WITH silver_bordeaux AS (
    SELECT
      dt,
      main_temp AS main_temp_bordeaux,
      main_humidity AS main_humidity_bordeaux,
      wind_speed AS wind_speed_bordeaux,
      'Bordeaux' AS city_name
    FROM {{ source('sourcesilver', 'bordeauxsilver') }}
),
silver_montreal AS (
    SELECT
      dt,
      main_temp AS main_temp_montreal,
      main_humidity AS main_humidity_montreal,
      wind_speed AS wind_speed_montreal,
      'Montreal' AS city_name
    FROM {{ source('sourcesilver', 'montrealsilver') }}
),
silver_paris AS (
    SELECT
      dt,
      main_temp AS main_temp_paris,
      main_humidity AS main_humidity_paris,
      wind_speed AS wind_speed_paris,
      'Paris' AS city_name
    FROM {{ source('sourcesilver', 'parissilver') }}
),
silver_rennes AS (
    SELECT
      dt,
      main_temp AS main_temp_rennes,
      main_humidity AS main_humidity_rennes,
      wind_speed AS wind_speed_rennes,
      'Rennes' AS city_name
    FROM {{ source('sourcesilver', 'rennessilver') }}
)
SELECT
    b.dt,
    b.main_temp_bordeaux,
    b.main_humidity_bordeaux,
    b.wind_speed_bordeaux,
    b.city_name AS city_name_bordeaux,
    m.main_temp_montreal,
    m.main_humidity_montreal,
    m.wind_speed_montreal,
    m.city_name AS city_name_montreal,
    p.main_temp_paris,
    p.main_humidity_paris,
    p.wind_speed_paris,
    p.city_name AS city_name_paris,
    r.main_temp_rennes,
    r.main_humidity_rennes,
    r.wind_speed_rennes,
    r.city_name AS city_name_rennes
FROM silver_bordeaux b
JOIN silver_montreal m ON b.dt = m.dt
JOIN silver_paris p ON b.dt = p.dt
JOIN silver_rennes r ON b.dt = r.dt