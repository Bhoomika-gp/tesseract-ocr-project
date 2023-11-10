import cv2
import pytesseract
import pandas as pd

# Path to your image file
# image_path = r'C:\\Users\\patel\Downloads\\HGS_Task\\HGS_Task\\Image_table.jpg'
image_path = "C:\Users\patel\Downloads\HGS_Task\HGS_Task\table.pdf"

# Read the image using OpenCV
image = cv2.imread(image_path)

# Convert the image to grayscale (required for Tesseract OCR)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Use Tesseract to do OCR on the image
extracted_text = pytesseract.image_to_string(gray_image)

# Split the extracted text into rows and columns (customize based on your image structure)
rows = extracted_text.split('\n')  # Split text into rows
table_data = [row.split('\t') for row in rows]  # Split rows into columns (assuming tab-separated data)

# Create a Pandas DataFrame from the table data
df = pd.DataFrame(table_data)

# Saving the DataFrame to an Excel file
output_excel_path = r'C:\Users\patel\Downloads\HGS_Task\HGS_Task\output_table.xlsx'
df.to_excel(output_excel_path, index=False, header=False)
print(f"Table data extracted and saved to: {output_excel_path}")
