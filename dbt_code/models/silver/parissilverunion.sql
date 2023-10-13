{{ config(materialized='view') }}

with historical as (
    select
        *,
        'historical' as _dbt_lambda_view_source,
        '{{ run_started_at }}' as _dbt_last_run_at
    from {{ ref('parissilverincr') }}
    where _airbyte_emitted_at < '{{ run_started_at }}'
),
new as (
    select
        *,
        'new' as _dbt_lambda_view_source,
        '{{ run_started_at }}' as _dbt_last_run_at
    from {{ ref('parissilverview') }}
    where _airbyte_emitted_at >= '{{ run_started_at }}'
),
unioned as (
    select * from new
    union all
    select * from historical
)

select * from unioned