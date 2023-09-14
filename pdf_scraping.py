import tabula
import pandas as pd
import os

# List of PDF files to process
pdf_files = ["LV225538B.pdf", "LX235067_1.pdf"]

# Create an empty list to store the output data from all PDF files
output_data = []

# Loop through each PDF file
for file in pdf_files:
    # Read the PDF file and extract the first page
    df = tabula.read_pdf(file, pages=1)

    # Extract the first table from the dataframe
    first_table = df[0]

    # Convert the table to a Pandas DataFrame
    df_table = pd.DataFrame(first_table)

    # Loop through each row in the table and extract the required data
    for i in range(len(df_table)):
        tender_no = df_table.iloc[1, 1]
        tender_type = df_table.iloc[1, 3]
        tender_title = df_table.iloc[12, 1]
        description = df_table.iloc[12, 1]

        # Check if the row already exists in the output list
        row_exists = False
        for row in output_data:
            if row["Tender No."] == tender_no:
                row_exists = True
                break

        # If the row doesn't exist, add it to the output list
        if not row_exists:
            output_data.append({
                "Sno.": len(output_data) + 1,
                "Tender No.": tender_no,
                "Tender Type": tender_type,
                "Tender Title": tender_title,
                "Description": description,
                "PDF File": file
            })

# Convert the output list to a DataFrame
output_df = pd.DataFrame(output_data, columns=["Sno.", "Tender No.", "Tender Type", "Tender Title", "Description", "PDF File"])

# Save the output DataFrame to an Excel file in the current working directory
output_file = os.path.join(os.getcwd(), "output.xlsx")
output_df.to_excel(output_file, index=False)

# Print a message to confirm that the file has been saved
print(f"Output file saved to {output_file}")
