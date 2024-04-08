# ~~~~~~~~~~~~~~~~~~~ Script for querying OpenAI API models

import numpy as np
import pandas as pd
import openai
from openai import OpenAI
import argparse
from tqdm import tqdm

def softmax(x):
    return np.exp(x)/sum(np.exp(x))


def get_completion(model="text-ada-001", instruction = None, sentence = None, question = None,  answer_choices=["1","2","3","4"], **kwargs):
    client = OpenAI()
    # Get generated answers
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": instruction},
            {"role": "user", "content": sentence},
            {"role": "user", "content": question}
        ],
        **kwargs
    ).choices[0]
    generated_answer = completion.message

    return generated_answer
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run GPT-3 completion on pre-constructed prompts.")
    parser.add_argument("--num_examples", type=int, default=0)
    parser.add_argument("--seed", "-S", type=int, default=0)
    parser.add_argument("--model", "-M", type=str, default="gpt-3.5-turbo")
    parser.add_argument("--suffix", default=None, choices=["no-story"])
    parser.add_argument("--temperature", "-T", type=float, default=0)

    args = parser.parse_args()
    
    # Random seed.
    np.random.seed(args.seed)
    
    # Secret file with API key (DO NOT commit this)
    with open("key.txt", "r") as f:
        key = f.read()
    openai.api_key = key
    
    answer_choices = ["1","2","3","4","5","6","7"]
    
    # These were obtained from the tokenizer tool https://beta.openai.com/tokenizer?view=bpe
    # answer_token_ids = {
    #     "1": 16,
    #     "2": 17,
    #     "3": 18,
    #     "4": 19,
    #     "5": 20
    # }
    avoid_token_ids = {
        "\n": 198
    }
    logit_bias = {
        str(token_id): -100 for token_id in avoid_token_ids.values()
    }

    # Parameters for all completions
    completion_params = dict(
        max_tokens=1,
        logprobs=True,
        temperature=args.temperature, # equivalent to taking argmax
        logit_bias=logit_bias
    )
    
    if args.suffix is not None:
        suffix = "_"+args.suffix
    else:
        suffix = ""

    scenarios = pd.read_csv(
        f"../prompts/prompt.csv"
    ).dropna()
    print(scenarios.head())

    with open("instruction.txt", "r") as f:
        instruction = f.read()
    
    for i, row in tqdm(scenarios.iterrows()):
        prompt_1 = row.prompt_1
        generated_answer_1 = get_completion(
            model=args.model, 
            instruction=instruction,
            sentence=row.sentence,
            question=row.question_1,
            answer_choices=answer_choices,
            **completion_params
        )
        prompt_2 = row.prompt_2
        generated_answer_2 = get_completion(
            model=args.model, 
            instruction=instruction,
            sentence=row.sentence,
            question=row.question_2,
            answer_choices=answer_choices,
            **completion_params
        )
        # Evaluate generated text.
        print(generated_answer_1)
        scenarios.loc[i, "generation_1"] = generated_answer_1.content
        # scenarios.loc[i, "generation_isvalid_1"] = (generated_answer_1.strip() in answer_choices)
        # # Record probability distribution over valid answers.
        # scenarios.loc[i, "distribution_1"] = str(probs_1)
        # # Take model "answer" to be argmax of the distribution.
        # sorted_probs_1 = [probs_1[answer] for answer in answer_choices]
        # chosen_answer_1 = str(np.argmax(sorted_probs_1) + 1)
        # scenarios.loc[i, "answer_1"] = chosen_answer_1

        scenarios.loc[i, "generation_2"] = generated_answer_2.content
        # scenarios.loc[i, "generation_isvalid_2"] = (generated_answer_2.strip() in answer_choices)
        # # Record probability distribution over valid answers.
        # scenarios.loc[i, "distribution_2"] = str(probs_2)
        # # Take model "answer" to be argmax of the distribution.
        # sorted_probs_2 = [probs_2[answer] for answer in answer_choices]
        # chosen_answer_2 = str(np.argmax(sorted_probs_2) + 1)
        # scenarios.loc[i, "answer_2"] = chosen_answer_2
     
    scenarios["model"] = args.model
    scenarios["temperature"] = args.temperature
    scenarios["seed"] = args.seed

    scenarios.to_csv(f"../model_data/model_data{suffix}_{args.model}_temperature{args.temperature}_seed{args.seed}_examples{args.num_examples}.csv", index=False)
