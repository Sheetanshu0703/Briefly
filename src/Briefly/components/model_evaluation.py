import os
os.environ["TRANSFORMERS_NO_TF"] = "1"  # Disable TensorFlow dependency in transformers

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from datasets import load_from_disk
import evaluate
import torch
import pandas as pd
from tqdm import tqdm

from Briefly.entity import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self, config):
        self.config = config

    def generate_batch_sized_chunks(self, list_of_elements, batch_size):
        """
        Yield successive batch-sized chunks from the input list.
        """
        for i in range(0, len(list_of_elements), batch_size):
            yield list_of_elements[i: i + batch_size]

    def calculate_metric_on_test_ds(self, dataset, metric, model, tokenizer,
                                    batch_size=16, device="cpu",
                                    column_text="dialogue",
                                    column_summary="summary"):

        article_batches = list(self.generate_batch_sized_chunks(dataset[column_text], batch_size))
        target_batches = list(self.generate_batch_sized_chunks(dataset[column_summary], batch_size))

        for article_batch, target_batch in tqdm(zip(article_batches, target_batches),
                                                total=len(article_batches), desc="Evaluating"):
            inputs = tokenizer(article_batch,
                               max_length=1024,
                               truncation=True,
                               padding="max_length",
                               return_tensors="pt")

            summaries = model.generate(
                input_ids=inputs["input_ids"].to(device),
                attention_mask=inputs["attention_mask"].to(device),
                length_penalty=0.8,
                num_beams=8,
                max_length=128
            )

            decoded_summaries = [
                tokenizer.decode(s, skip_special_tokens=True, clean_up_tokenization_spaces=True)
                for s in summaries
            ]

            metric.add_batch(predictions=decoded_summaries, references=target_batch)

        score = metric.compute()
        return score

    def evaluate(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path).to(device)

        dataset = load_from_disk(self.config.data_path)

        rouge = evaluate.load("rouge")  # using the modern `evaluate` package

        score = self.calculate_metric_on_test_ds(
            dataset=dataset["test"][:10],
            metric=rouge,
            model=model,
            tokenizer=tokenizer,
            batch_size=2,
            device=device,
            column_text="dialogue",
            column_summary="summary"
        )

        rouge_names = ["rouge1", "rouge2", "rougeL", "rougeLsum"]
        rouge_dict = dict((rn, score[rn].mid.fmeasure if hasattr(score[rn], 'mid') else score[rn]) for rn in rouge_names)

        df = pd.DataFrame([rouge_dict])
        df.to_csv(self.config.metric_file_name, index=False)

        print("[INFO] Evaluation complete. Results saved to", self.config.metric_file_name)