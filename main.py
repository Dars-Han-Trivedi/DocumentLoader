from flask import Flask, request, jsonify

from chromaDb import chromaDbFunctions

app = Flask(__name__)

@app.route('/api/process_pdf', methods=['POST'])
def process_pdf():
    # Check if the request contains a file
    if 'pdf_file' not in request.files:
        return jsonify({'error': 'No PDF file provided.'}), 400

    # Get the file object from the request
    pdf_file = request.files['pdf_file']

    # Process the PDF file (You can add your processing logic here)
    # For example, you can save the file, extract text, or analyze its content.
    chromaDbClient = chromaDbFunctions()
    chromaDbClient.uploadPdf(pdf_file, pdf_file.name)

    # Return a response (Here, we just return a success message)
    return jsonify({'message': 'PDF file processed successfully.'})

@app.route('/api/peek', methods=['GET'])
def peek():
    chromaDbClient = chromaDbFunctions()
    return chromaDbClient.peek()


if __name__ == '__main__':
    app.run(debug=True)
