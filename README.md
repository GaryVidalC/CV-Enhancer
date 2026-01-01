# CV-Enhancer

This project is a tool to enhance and customize a curriculum vitae (CV) based on a specific job offer. It uses Google's AI (Gemini) to analyze the job offer and adapt the existing CV to better match the job requirements.

## How to Use

1. **Preparation**:
   - Ensure you have Python 3.x installed.
   - Install the required library: `pip install google-genai`
   - Place your Google GenAI API key in the `key.txt` file (must be in the project root).
   - Prepare your resume in JSON format in `data/resume_gary_en.json`.
   - Ensure the LaTeX template is in `data/latex_template.tex`.

2. **Execution**:
   - Open a terminal in the project folder.
   - Run the script with the job offer URL as an argument:
     ```
     python main.py <JOB_OFFER_URL>
     ```
     For example:
     ```
     python main.py https://example.com/job-offer
     ```

3. **Result**:
   - The script will generate an `output.tex` file with the customized CV in LaTeX format.
   - You can compile `output.tex` with a LaTeX processor (like pdflatex) to get a PDF.

## Requirements

- Python 3.x
- `google-genai` library
- Valid Google GenAI API key
- Data files: `data/resume_gary_en.json` and `data/latex_template.tex`

## Notes

- The language of the generated CV is set to French; you can change it in the code if necessary.
- Ensure the job offer URL is accessible and contains the necessary information.