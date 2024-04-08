import pandas
import numpy as np

def read_data():
    df = pandas.read_csv("../data/Material-Konstanz_aufb.csv")
    return df

def create_prompt(df):
    # Subset df to only include experiments item
    # cond = k, p or n 
    cond = ["k", "p", "n"]
    new_df = df[df["cond"].isin(cond)]


    # Reset index
    new_df = new_df.reset_index(drop=True)
    # Drop cols has_question_2 and has_question_1
    new_df = new_df.drop(columns=["has_question_2", "has_question_1"])
    # Remove html tags <b>, </b>, <br> in sentence column, tags are also string
    # Replace b with "", br with backspace
    new_df["sentence"] = new_df["sentence"].str.replace("<b>", "<Beginn der zu bewertenden Aussage>").str.replace("</b>", "<Ende der zu bewertenden Aussage>").str.replace("<br>", "")
    #print(new_df.sentence)

    prompt_muster = "[Instruction] +[Sentence] + [Question]"

    # read the instruction from instruction.txt
    with open("instruction.txt", "r") as f:
        instruction = f.read()
    #print(instruction)

    # Create a new column called prompt, which has the format of prompt_muster
    for index, row in new_df.iterrows():
        new_df.at[index, "prompt_1"] = (
            instruction + "\n" + 
            row["sentence"] + "\n" + 
            row["question_1"]
        )
        new_df.at[index, "prompt_2"] = (
            instruction + "\n" + 
            row["sentence"] + "\n" + 
            row["question_2"]
        )
    
    print(new_df.head())
    return new_df

def main():
    df = read_data()
    #print(df)
    #print(df.columns)
    new_df = create_prompt(df)
    new_df.to_csv("../prompts/prompt.csv")

if __name__ == "__main__":
    main()
