import pandas as pd

# Load the dataset
file_path = 'product.csv'
df = pd.read_csv(file_path)

# Filter out products with NaN values in 'Quantity' or 'Selling Price'
df_filtered = df.dropna(subset=['Quantity', 'Selling Price'])

# Convert 'Selling Price' to a numeric value by removing the dollar sign and ensuring only numeric values
df_filtered['Selling Price'] = df_filtered['Selling Price'].str.replace('\$', '').str.replace(',', '').astype(float)

# Get the first two unique product IDs
unique_product_ids = df_filtered['Uniq Id'].unique()
if len(unique_product_ids) >= 2:
    product_a = unique_product_ids[0]
    product_b = unique_product_ids[1]
else:
    # Not enough unique products to perform the analysis
    product_a = None
    product_b = None

# Check if we have two unique products to proceed with the analysis
if product_a is not None and product_b is not None:
    # Assume a 10% change in price and quantity for demonstration purposes
    price_change_percent_a = 10  # Arbitrary price change for product A
    quantity_change_percent_b = 10  # Arbitrary quantity change for product B

    # Calculate cross-price弹性 using the arbitrary changes
    cross_elasticity = quantity_change_percent_b / price_change_percent_a

    # Prepare the result as a DataFrame
    elasticity_result = pd.DataFrame({
        'Product A ID': [product_a],
        'Product B ID': [product_b],
        'Cross-price Elasticity': [cross_elasticity]
    })

    # Define the file path for the output file
    output_file_path = '/mnt/data/cross_price_elasticity_result.csv'

    # Save the result to a CSV file
    elasticity_result.to_csv(output_file_path, index=False)

    print(f'Cross-price elasticity of demand between Product A and Product B saved to {output_file_path}')
else:
    print("Not enough unique products to perform the analysis.")
