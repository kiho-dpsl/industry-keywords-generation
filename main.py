import logging

import pandas as pd
from langchain_openai import ChatOpenAI

from config import DATA_DIR, MODEL_NAME
from utils import build_prompt


logging.basicConfig(filename='keywords.log', level=logging.INFO, format='%(message)s')

def main():
    df = pd.read_csv(f"{DATA_DIR}/sub_industry.csv")
    llm = ChatOpenAI(model=MODEL_NAME, temperature=0.5)
    prompt = build_prompt()
    chain = prompt | llm
    keywords = []
    for _, row in df.iterrows():
        input = {'industry': row['industry'], 'description': row['description'], 'sub_industry': row['sub_industry']}
        response = chain.invoke(input)
        response = response.content
        keywords.append(response)
        logging.info(f"Sub-Industry: {row['sub_industry']}, Keywords: {response}")
    df['keywords'] = keywords
    df.to_csv(f"{DATA_DIR}/sub_industry_keywords.csv", index=False)


if __name__ == "__main__":
    main()