from PyPDF2 import PdfReader

pdf_file = input("Enter PDF file name: ")

try:
    reader = PdfReader(pdf_file)

    extracted_text = ""

    for page in reader.pages:
        extracted_text += page.extract_text() + "\n"

    output_file = "output.txt"

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(extracted_text)

    print(f"✅ Text extracted successfully!")
    print(f"Saved as: {output_file}")

except FileNotFoundError:
    print("❌ PDF file not found.")
except Exception as e:
    print("Error:", e)
