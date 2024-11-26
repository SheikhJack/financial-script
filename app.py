from flask import Flask, request, jsonify 
from flask_cors import CORS
import pdfplumber 

app = Flask(__name__)
CORS(app)

@app.route('/analyze_pdf', methods=['POST'])
def analyze_pdf():
    print("Request Files:", request.files)
    pdf_file = request.files.get('pdf')
    if not pdf_file:
        return "No file uploaded", 400
    

    with pdfplumber.open(pdf_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
    
    
    revenue = "1000"  
    expenses = "800"  
    profit = int(revenue) - int(expenses)
    
    return jsonify({"revenue": revenue, "expenses": expenses, "profit": profit})
    

if __name__ == '__main__':
    app.run(debug=True, port=8080)
