#!/usr/bin/env python3


# Author: Rishu Kumar

import os
import json

def clean_data_one(text, summary):
    # For summary:
    if len(summary) == 1:
        summary = summary[0]
    else:
        summary = " ".join(summary)

    summary = summary.replace("@@ ","").replace("ENTITY", "PERSON")

    # For Text:
    clean_text = ""

    for item in text:
        item = item.strip()
        if item[0] == "[": continue
        item = item.replace("ENTITY", "PERSON")
        item = item.replace("@@ ","")
        clean_text = clean_text.strip() + " " + item

    return text, summary

if __name__ == '__main__':
    for item in ["train", "dev", "test"]:
        data_path = "/lnet/troja/work/people/kumar/Research_Project/submission/data/" + item
        os.makedirs(data_path, exist_ok=True)

        with open(f"/lnet/troja/work/people/kumar/Research_Project/TVMegaSite/tms_anonymize_{item}.json", encoding="utf8") as f:
            content = f.readlines()

        for item in content:
            jj = json.loads(item)

            text, summary = clean_data_one(jj["Transcript"],jj["Recap"])

            my_dict = {"Summary": summary, "Transcript": text}

            with open(f"{data_path}/{jj['filename']}", "w") as f:
                json.dump(my_dict, f)
