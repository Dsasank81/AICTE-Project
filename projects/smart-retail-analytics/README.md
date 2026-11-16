# Smart Retail Analytics

A lightweight analytics baseline for retail transaction exports. It summarizes revenue by product, daily revenue trends and (if a `stock` column exists) low-stock reorder candidates.

## Expected CSV
Required columns: `date,product,quantity,revenue`. Optional: `stock`.

## Run
`python -m pip install pandas`
`python analyze.py --data sales.csv --reorder-threshold 10`

This is an analytics prototype, not an AI demand-forecasting system. Reliable replenishment needs lead times, inventory movements, stockout history, seasonality and forecast validation.
