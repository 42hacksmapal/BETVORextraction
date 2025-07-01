import fitz  # PyMuPDF
import re

def extract_profit_from_pdf(pdf_path):
    profit_patterns = [
        r"Jahresgewinn\s*[/:]?\s*([\d\'\.,]+)",  # e.g., Jahresgewinn: 62'999.52
        r"Jahresgewinn\s*/\s*Jahresverlust\s+([\d\'\.,]+)"
    ]
    
    with fitz.open(pdf_path) as doc:
        text = "\n".join(page.get_text() for page in doc)

        for pattern in profit_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                profit_str = match.group(1).replace("'", "").replace(",", ".")
                try:
                    profit = float(profit_str)
                    return profit
                except ValueError:
                    continue

    return None

# Example usage
pdf_file_path = r"C:\Users\mapal\Desktop\21_Buchhaltung Bitzi.pdf"
profit = extract_profit_from_pdf(pdf_file_path)

if profit is not None:
    print(f"Extracted annual profit: {profit:,.2f} CHF")
else:
    print("Profit value not found in the PDF.")
