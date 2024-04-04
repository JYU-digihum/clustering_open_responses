from tnparser.pipeline import read_pipelines, Pipeline
import pandas as pd
import re
from tqdm import tqdm
import argparse

def main():
    parser = argparse.ArgumentParser(description='Optional app description')
    parser.add_argument('input_data', help='A required string positional argument')
    parser.add_argument('output_data', help='A required string positional argument')
    args = parser.parse_args()
    input_data = args.input_data
    output_data = args.output_data

    # Get only the lemmas from the lemmatizer
    def get_lemmas_from_parsed(sent):
        parsed = p.parse(sent)
        parsed_split = parsed.split("\n")
        lemmas = []
        for i in parsed_split:
            if '\t' in i:
                parsed_more = i.split("\t")
                lemmas.append(parsed_more[2])
        return lemmas


    if ".csv" not in input_data:
        print("Please check the name or input a csv file!")
    else:
        # Load the data from csv file
        df = pd.read_csv(input_data)

        # What pipelines do we have for the Finnish model?
        available_pipelines = read_pipelines("models_fi_tdt_dia/pipelines.yaml")
        # This is a dictionary, its keys are the pipelines
        print(list(available_pipelines.keys()))
        # Instantiate one of the pipelines
        p = Pipeline(available_pipelines["parse_plaintext"])
        
        # Get lemmas for all of data in Pandas dataframe and save the result
        tqdm.pandas()
        df["lemma"] = df["text"].progress_apply(get_lemmas_from_parsed)
        df.to_csv(output_data, index=False)

if __name__ == "__main__":
    main()

