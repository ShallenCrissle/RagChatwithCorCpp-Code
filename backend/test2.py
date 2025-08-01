import time
import os
import openpyxl
import google.generativeai as genai
import cohere
from dotenv import load_dotenv
import evaluate
from bert_score import score as bert_score_fn

# === Setup ===
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
co = cohere.Client(os.getenv("COHERE_API_KEY"))

bleu = evaluate.load("bleu")
rouge = evaluate.load("rouge")

# === Prompts & References ===
PROMPT_REF_PAIRS = {
    "How does the struct '_lprint_job_s' work in lprint-job.h?": 
        "The _lprint_job_s struct holds print job details such as status, format, data, and job metadata in lprint.",
    "What does the function lprint_register_printer do in lprint-printer.c?": 
        "It registers a printer with the system and sets up its attributes and capabilities.",
    "How is the main loop handled in lprint-main.c?": 
        "The main loop starts the lprint server, initializes the system, and processes incoming requests.",
    "Explain how job status is updated in lprint-job.c.": 
        "The job status is updated based on job state transitions like processing, completed, or aborted.",
    "What happens when a new print request is received by the server?": 
        "The server creates a new job, processes the data, and sends it to the appropriate printer.",
    "What is the purpose of lprint-printer.c and how does it manage printer capabilities?": 
        "It implements printer registration, capabilities setup, and operations like start, pause, or cancel jobs."
}

# === Excel Setup ===
wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "Model Evaluation"
sheet.append([
    "Prompt",
    "Gemini BLEU", "Gemini ROUGE-L", "Gemini BERTScore",
    "Cohere BLEU", "Cohere ROUGE-L", "Cohere BERTScore",
    "Gemini Time (s)", "Cohere Time (s)"
])

# === Evaluation Loop ===
for prompt, reference in PROMPT_REF_PAIRS.items():
    print(f"\n🔍 Prompt: {prompt}")

    # Gemini
    gemini_start = time.time()
    try:
        gemini_response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt).text.strip()
    except Exception as e:
        gemini_response = f"❌ Error: {e}"
    gemini_time = time.time() - gemini_start

    # Cohere
    cohere_start = time.time()
    try:
        cohere_response = co.generate(
            model='command-r-plus',
            prompt=prompt,
            max_tokens=1024,
            temperature=0.3
        ).generations[0].text.strip()
    except Exception as e:
        cohere_response = f"❌ Error: {e}"
    cohere_time = time.time() - cohere_start

    # Evaluate Gemini
    g_bleu = bleu.compute(predictions=[gemini_response], references=[reference])['bleu']
    g_rouge = rouge.compute(predictions=[gemini_response], references=[reference])['rougeL']
    g_bert, _, _ = bert_score_fn([gemini_response], [reference], lang='en', verbose=False)
    g_bert = round(g_bert[0].item(), 4)

    # Evaluate Cohere
    c_bleu = bleu.compute(predictions=[cohere_response], references=[reference])['bleu']
    c_rouge = rouge.compute(predictions=[cohere_response], references=[reference])['rougeL']
    c_bert, _, _ = bert_score_fn([cohere_response], [reference], lang='en', verbose=False)
    c_bert = round(c_bert[0].item(), 4)

    # Save to Excel
    sheet.append([
        prompt,
        round(g_bleu, 4), round(g_rouge, 4), g_bert,
        round(c_bleu, 4), round(c_rouge, 4), c_bert,
        round(gemini_time, 2), round(cohere_time, 2)
    ])

# Save results
output_file = "model_comparison_with_metrics.xlsx"
wb.save(output_file)
print(f"\n✅ Results saved to {output_file}")
