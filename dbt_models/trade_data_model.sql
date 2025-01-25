sql
{{ config(
    materialized='view'
) }}

select
    trade_id,
    stock_symbol,
    trade_volume,
    trade_price,
    trade_timestamp
    FROM
    raw.trade_data
    WHERE trade_timestamp > DATEADD('day', -7, GETDATE()) 