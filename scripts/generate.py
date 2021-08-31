from aitextgen import aitextgen
from schlag.config import RESULTS_DIR

# HF hub
# hf_model = "dbmdz/german-gpt2"
# Local
hf_model = RESULTS_DIR / "no_freeze"

# Load textgen
if isinstance(hf_model, str):
    ai = aitextgen(model=hf_model, verbose=True)
else:
    ai = aitextgen(model_folder=hf_model, verbose=True)

ai.to_gpu()

print("\n\n\n")

# prompt = "Wir ziehen durch die Straßen"
prompt = "Wir stehen an der Bar"
while prompt != "q":

    output = ai.generate(
        prompt="[Intro]\n" + prompt,
        seed=27,
        # Model params
        n=10,
        min_len=None,
        max_len=256,
        temperature=0.8,
        do_sample=True,
        use_cache=True,
        # Custom model params
        early_stopping=False,  # whether to stop beam search when at least num_beams sentences are finished
        num_beams=1,  # num beams for beam search, 1 = no beam search
        top_k=50,  # num highest probaba tokens to keep for top-k filtering
        top_p=0.95,  # float < 1 if most probable tokens with probs that add up to top_p are kept for generation
        repetition_penalty=1.2,  # penalty for repetition. 1.0 = no penalty
        length_penalty=1.0,  # < 1.0 shorter, > 1.0 longer
        no_repeat_ngram_size=0,  # > 0, all ngrams of that size can only occur once.
        # bad_words_id=[], # token ids not allowed to be generated
        num_beam_groups=1,  # num groups to divide num_beams into to ensure diversity
        diversity_penalty=0.0,  # value subtracted from beamscore if generates token same as any beam from other group
        remove_invalid_values=True,
        # output
        return_as_list=True,
        lstrip=False,
        skip_special_tokens=False,
    )

    for i, text in enumerate(output):
        print("\n==============")
        print(f"Text: {i}\n")
        print(text)

    print("\n==============")
    print("==============\n")
    prompt = input("Next prompt: ")
