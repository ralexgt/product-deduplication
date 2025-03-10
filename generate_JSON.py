import pandas as pd

try:
    # read the Parquet file
    df = pd.read_parquet("veridion_product_deduplication_challenge.snappy.parquet", engine="pyarrow")

    # save it as a JSON file for readability
    df.to_json("input.json", orient="records", indent=4)
 
    print("File successfully written!")
except Exception as e:
    print(f"Error: {e}")





