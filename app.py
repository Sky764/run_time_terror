from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Get the uploaded file from the form
            excel_file = request.files["file"]

            # Load the Excel file into a pandas DataFrame
            df = pd.read_excel(excel_file)

            # Preprocessing steps (modify as needed)
            # Example: drop rows with missing values
            df = df.dropna()

            # Display the preprocessed DataFrame
            return render_template("result.html", data=df.to_html())
        except Exception as e:
            return f"Error: {e}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
