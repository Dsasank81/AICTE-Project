"""Retail sales analysis and reorder suggestions from a transaction CSV."""
import argparse
import pandas as pd

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--data",default="sales.csv")
    p.add_argument("--date",default="date")
    p.add_argument("--product",default="product")
    p.add_argument("--quantity",default="quantity")
    p.add_argument("--revenue",default="revenue")
    p.add_argument("--reorder-threshold",type=int,default=10)
    a=p.parse_args()
    df=pd.read_csv(a.data,parse_dates=[a.date])
    required=[a.product,a.quantity,a.revenue,a.date]
    missing=set(required)-set(df.columns)
    if missing: raise ValueError(f"Missing columns: {sorted(missing)}")
    print("\nRevenue by product")
    print(df.groupby(a.product)[a.revenue].sum().sort_values(ascending=False).to_string())
    print("\nDaily revenue")
    print(df.groupby(df[a.date].dt.date)[a.revenue].sum().tail(14).to_string())
    stock_col="stock" if "stock" in df.columns else None
    if stock_col:
        latest=df.sort_values(a.date).groupby(a.product).tail(1)
        low=latest[latest[stock_col] <= a.reorder_threshold]
        print("\nReorder candidates")
        print(low[[a.product,stock_col]].to_string(index=False) if len(low) else "None")
    else: print("\nNo stock column supplied; reorder suggestions skipped.")

if __name__=="__main__": main()
