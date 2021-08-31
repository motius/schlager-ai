import json

import torch
from aitextgen.TokenDataset import TokenDataset
from aitextgen.utils import model_max_length
from pytorch_lightning.loggers import TensorBoardLogger
from torch.utils.data import DataLoader

from aitextgen import aitextgen
from schlag.config import DATA_DIR, RESULTS_DIR
from schlag.data.process import clean_lyrics


def main():
    hf_model = "dbmdz/german-gpt2"

    # Load textgen
    ai = aitextgen(model=hf_model, verbose=True)

    # load data
    raw_dir = DATA_DIR / "raw"
    texts = []
    for filename in raw_dir.glob("*.json"):
        with open(filename) as f:
            song = json.load(f)
            lyrics = song["lyrics"]

            texts.append(clean_lyrics(lyrics))

    # set up data set
    block_size = model_max_length(ai.model.config)
    train_data = TokenDataset(
        tokenizer=ai.tokenizer,
        bos_token=ai.bos_token,
        eos_token=ai.eos_token,
        unk_token=ai.unk_token,
        block_size=block_size,
        texts=texts,
    )

    out_dir = str(RESULTS_DIR / "no_freeze")
    tb_logger = TensorBoardLogger(out_dir)

    ai.train(
        train_data,
        n_gpu=1,
        seed=27,
        num_steps=5000,
        generate_every=100,
        output_dir=out_dir,
        loggers=[tb_logger],
        # freeze_layers=True,
        # num_layers_freeze=11,
        line_by_line=False,
        header=False,
    )


if __name__ == "__main__":
    main()
