from google import genai
import pathlib, json
import argparse

parser = argparse.ArgumentParser(description="Inputs CV-enhancer with job offer URL and personal details.")

parser.add_argument("url", type=str, help="URL Oferta")

args = parser.parse_args()

API_key = open("key.txt").read()

client = genai.Client(api_key = API_key)
modelo = "gemini-2.5-pro"

url = args.url  # Job offer URL passed as a command-line argument
language = "French"

json_resume_path = pathlib.Path("data/resume_gary_en.json")
with open(json_resume_path, 'r') as f:
    json_resume = json.load(f)

tex_resume_path = pathlib.Path("data/latex_template.tex")
with open(tex_resume_path, 'r') as f:
    tex_template = f.read()

first_prompt = f"""
You are a helpful assistant that extracts relevant information from job offers to enhance a CV. 
Read the job offer at the provided URL {url} and summarize the key skills, qualifications, and experiences required for the position. 
You also have a .json resume file, and a .tex template. 
You have to pick the most relevant information form the .json resume that fits the CV and create a .tex file following the .tex structure, the text in the .tex file must be in {language}. 
You can tweak the decriptions in order to match better the job offer, but you must follow the .tex template structure. Put all the work experience and the projects in the CV, but arrange the order based on the job offer requirements.
Create a summary that matches the job offer requirements as closely as possible with the information available in the .json resume, but don't write too much text, keep it concise and to the point.
Always add the Outstanding student in the CV. Add the references if you think they are relevant for the job offer.
If you want to itemize inside de joblong envorimoent of the .tex template, don't use the \item, go with a dash - and add the description after that. use \\ to separate lines and add a new item.
here is the .json resume file: {json.dumps(json_resume)} 
here is the .tex template: {tex_template}
"""
response = client.models.generate_content(
    model=modelo,
    contents=first_prompt,
    config={'tools': [{'url_context': {}}]},
)

latex_output = response.text

with open("output.tex", "w", encoding="utf-8") as f:
    f.write(latex_output)

print("File 'output.tex' has been created successfully!")