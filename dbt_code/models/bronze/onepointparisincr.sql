
/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below 
*/

{{ config(
        materialized='incremental',
        unique_key = '_airbyte_ab_id'
    ) 
    }}

with source_data as (

    SELECT
    *
    FROM  {{ source('source', 'onepointparis') }}
    {% if is_incremental() %}
    WHERE
    json_extract_scalar(_airbyte_data, '$.coord.lon') IS NOT NULL
    AND json_extract_scalar(_airbyte_data, '$.coord.lat') IS NOT NULL
    AND _airbyte_emitted_at >= (select max(_airbyte_emitted_at) from {{ this }})
    {% endif %}
)

select *
from source_data

/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null
