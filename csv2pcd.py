import pandas as pd
import numpy as np
def csv_to_pcd(input_csv, output_pcd):
    # Read CSV file into a Pandas DataFrame
    df = pd.read_csv(input_csv)

    # Extract necessary columns
    x = df['x(m)'].values
    y = df['y(m)'].values
    z = df['z(m)'].values
    intensity = df['Rfl'].apply(lambda x: int(x)).values  # Convert to integer

    # Combine the data into a single NumPy array
    data = np.column_stack((x, y, z, intensity))

    # Write data to PCD file
    with open(output_pcd, 'w') as f:
        # Write PCD header
        f.write("# .PCD v.7 - Point Cloud Data file format\n")
        f.write("VERSION .7\n")
        f.write("FIELDS x y z intensity\n")
        f.write("SIZE 4 4 4 4\n")
        f.write("TYPE F F F F\n")  # 'F' represents float
        f.write("COUNT 1 1 1 1\n")
        f.write("WIDTH {}\n".format(len(data)))
        f.write("HEIGHT 1\n")
        f.write("VIEWPOINT 0 0 0 1 0 0 0\n")
        f.write("POINTS {}\n".format(len(data)))
        f.write("DATA ascii\n")

        # Write data
        for i in range(len(x)):
            f.write("{:.6f}, {:.6f}, {:.6f}, {}\n".format(x[i], y[i], z[i], intensity[i]))

    print("PCD file saved successfully.")

# Example usage
csv_to_pcd(r"C:\Users\bingo\Desktop\test.csv", "output.pcd")
