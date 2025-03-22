# AI-Based-Resume-Screening-and-Candidate-Ranking-System
AI-powered resume screening and ranking system built with Streamlit, NLP, and cosine similarity. Extracts, preprocesses, and ranks PDF resumes based on job descriptions, providing a structured and visualized ranking output.

## Features
- Upload multiple PDF resumes
- Extract text from resumes automatically
- Preprocess text using NLP techniques (lemmatization, stopword removal)
- Rank resumes based on cosine similarity with job description
- Display ranked results in a table
- Download ranked results as a CSV file
- Visualize ranking scores with an interactive bar chart

## Technologies Used
- Python
- Streamlit
- PDFPlumber
- NLTK
- Scikit-learn
- Plotly
- Pandas

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/TejasRawool186/AI-Based-Resume-Screening-and-Candidate-Ranking-System.git
   cd resume-screening-app
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```sh
   streamlit run resume_ranking_system.py
   ```

2. Open the browser and go to the provided URL (usually `http://localhost:8501`).

3. Enter a job description, upload resumes, and view ranking results.


## Future Enhancements
- Add support for DOCX and TXT resume formats
- Implement Named Entity Recognition (NER) for better candidate profiling
- Integrate with a database for storing candidate information
- Improve ranking algorithm using deep learning models

## Snapshot:
![Screenshot 2025-03-22 131534](https://github.com/user-attachments/assets/c7b0054a-ee97-4887-9492-d99a696256d4)

![Screenshot 2025-03-22 131622](https://github.com/user-attachments/assets/9a3e683e-c861-45b4-a9ef-e141f84db635)

![Screenshot 2025-03-22 131645](https://github.com/user-attachments/assets/7caa948e-655f-4016-9369-a7393074cb83)

![Screenshot 2025-03-22 131703](https://github.com/user-attachments/assets/0b560805-31b2-43bc-95a1-fbc3a4044c7d)






## License
This project is open-source and available under the MIT License.

## Contributing
Pull requests and feature suggestions are welcome! Feel free to open an issue or submit a PR.

## Author
- [Tejas Rawool](www.linkedin.com/in/tejas-rawool-067a722ab)

