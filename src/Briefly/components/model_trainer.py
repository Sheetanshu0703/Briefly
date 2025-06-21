from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
from Briefly.entity import ModelTrainerConfig
import torch


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"

        # Load tokenizer and model
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)

        # Load preprocessed dataset (already tokenized during DataTransformation)
        dataset = load_from_disk(self.config.data_path)

        # Data collator
        data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

        # Training arguments
        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=1,
            warmup_steps=500,
            per_device_train_batch_size=1,
            per_device_eval_batch_size=1,
            weight_decay=0.01,
            logging_steps=10,
            evaluation_strategy='steps',
            eval_steps=500,
            save_steps=1e6,
            gradient_accumulation_steps=16
        )

        # Trainer
        trainer = Trainer(
            model=model,
            args=trainer_args,
            tokenizer=tokenizer,
            data_collator=data_collator,
            train_dataset=dataset["train"],
            eval_dataset=dataset["validation"]
        )

        # Start training
        trainer.train()

        # Save model and tokenizer
        model.save_pretrained(os.path.join(self.config.root_dir, "pegasus-samsum-model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))
