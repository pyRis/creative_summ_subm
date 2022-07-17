#!/#!/usr/bin/env python3

# Author: Rishu Kumar

import os
import json
from datasets import load_dataset
dataset = load_dataset('json', data_files='../TVMegaSite/tms_anonymize_dev.json')

for item in dataset["train"]:
    print(item)
    break
exit()

with open("../TVMegaSite/tms_anonymize_dev.json") as f:
    content = f.readlines()

recap_list = []
recap_list_edited = []


jj = json.loads(content[0])


for key in jj.keys():
    print(f"{key} has length {len(jj[key])}")
    print(jj[key][0])

with open("temp.txt", "w+") as f:
    json.dump(jj, f)

exit()
for _, val in enumerate(content):
    jj = json.loads(val)
    recap = jj["Recap"]
    print(len(recap))


with open("recap_list.txt", "a+") as f:
    for item in recap_list:
        f.write(item+"\n")

with open("recap_list_edit.txt", "a+") as f:
    for item in recap_list_edit:
        f.write(item+"\n")
