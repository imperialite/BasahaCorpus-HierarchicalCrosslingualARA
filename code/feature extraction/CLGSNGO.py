import re

def clean(text):
  text = re.sub('[^A-Za-z ]',' ',text)
  text = re.sub(' +',' ',text)
  text = text.lower()
  return text

def get_ngrams(s, n):
  n_gram_list = [s[i:i+n] for i in range(len(s)-n+1)]
  n_gram_list_filtered = [] #remove ngrams with spaces
  for i in n_gram_list:
    if " " not in i:
      n_gram_list_filtered.append(i)
  return n_gram_list_filtered

def get_bigram_CLGSNGO(text):
  text = clean(text)
  input_text_ngram = get_ngrams(text,2)
  input_text_ngram_count = len(input_text_ngram)

  bigram_tag_counter = 0
  bigram_ceb_counter = 0
  bigram_bik_counter = 0
  bigram_hil_counter = 0
  bigram_rin_counter = 0
  bigram_min_counter = 0
  bigram_kar_counter = 0

  bigram_tag_match = 0
  bigram_bik_match = 0
  bigram_ceb_match = 0
  bigram_hil_match = 0
  bigram_rin_match = 0
  bigram_min_match = 0
  bigram_kar_match = 0

  bigram_tag_loc = "ngrams list/tag_top25_2gram.txt"
  bigram_ceb_loc = "ngrams list/ceb_top25_2gram.txt"
  bigram_bik_loc = "ngrams list/bik_top25_2gram.txt"
  bigram_hil_loc = "ngrams list/hil_top25_2gram.txt"
  bigram_rin_loc = "ngrams list/rin_top25_2gram.txt"
  bigram_min_loc = "ngrams list/min_top25_2gram.txt"
  bigram_kar_loc = "ngrams list/kar_top25_2gram.txt"

  bigram_tag_list = []
  bigram_ceb_list = []
  bigram_bik_list = []
  bigram_hil_list = []
  bigram_rin_list = []
  bigram_min_list = []
  bigram_kar_list = []

  with open(bigram_tag_loc,'r') as bigram_tag_file:
    bigram_tag_file_contents = bigram_tag_file.readlines()
    for i in bigram_tag_file_contents:
      item = i.strip().split(",")
      bigram_tag_list.append(item[0])

  with open(bigram_ceb_loc,'r') as bigram_ceb_file:
    bigram_ceb_file_contents = bigram_ceb_file.readlines()
    for i in bigram_ceb_file_contents:
      item = i.strip().split(",")
      bigram_ceb_list.append(item[0])

  with open(bigram_bik_loc,'r') as bigram_bik_file:
    bigram_bik_file_contents = bigram_bik_file.readlines()
    for i in bigram_bik_file_contents:
      item = i.strip().split(",")
      bigram_bik_list.append(item[0])

  with open(bigram_hil_loc,'r') as bigram_hil_file:
    bigram_hil_file_contents = bigram_hil_file.readlines()
    for i in bigram_hil_file_contents:
      item = i.strip().split(",")
      bigram_hil_list.append(item[0])

  with open(bigram_rin_loc,'r') as bigram_rin_file:
    bigram_rin_file_contents = bigram_rin_file.readlines()
    for i in bigram_rin_file_contents:
      item = i.strip().split(",")
      bigram_rin_list.append(item[0])

  with open(bigram_min_loc,'r') as bigram_min_file:
    bigram_min_file_contents = bigram_min_file.readlines()
    for i in bigram_min_file_contents:
      item = i.strip().split(",")
      bigram_min_list.append(item[0])

  with open(bigram_kar_loc,'r') as bigram_kar_file:
    bigram_kar_file_contents = bigram_kar_file.readlines()
    for i in bigram_kar_file_contents:
      item = i.strip().split(",")
      bigram_kar_list.append(item[0])

  for i in input_text_ngram:
    if i in bigram_tag_list:
      bigram_tag_counter += 1
    if i in bigram_bik_list:
      bigram_bik_counter += 1
    if i in bigram_ceb_list:
      bigram_ceb_counter += 1
    if i in bigram_hil_list:
      bigram_hil_counter += 1
    if i in bigram_rin_list:
      bigram_rin_counter += 1
    if i in bigram_min_list:
      bigram_min_counter += 1
    if i in bigram_kar_list:
      bigram_kar_counter += 1

  if bigram_tag_counter != 0:
    bigram_tag_match = bigram_tag_counter/input_text_ngram_count
  if bigram_bik_counter != 0:
    bigram_bik_match = bigram_bik_counter/input_text_ngram_count
  if bigram_ceb_counter != 0:
    bigram_ceb_match = bigram_ceb_counter/input_text_ngram_count
  if bigram_hil_counter != 0:
    bigram_hil_match = bigram_hil_counter/input_text_ngram_count
  if bigram_rin_counter != 0:
    bigram_rin_match = bigram_rin_counter/input_text_ngram_count
  if bigram_min_counter != 0:
    bigram_min_match = bigram_min_counter/input_text_ngram_count
  if bigram_kar_counter != 0:
    bigram_kar_match = bigram_kar_counter/input_text_ngram_count

  return bigram_tag_match,bigram_bik_match,bigram_ceb_match,bigram_hil_match,bigram_rin_match,bigram_min_match,bigram_kar_match


def get_trigram_CLGSNGO(text):
  text = clean(text)
  input_text_ngram = get_ngrams(text,3)
  input_text_ngram_count = len(input_text_ngram)

  trigram_tag_counter = 0
  trigram_ceb_counter = 0
  trigram_bik_counter = 0
  trigram_hil_counter = 0
  trigram_rin_counter = 0
  trigram_min_counter = 0
  trigram_kar_counter = 0

  trigram_tag_match = 0
  trigram_bik_match = 0
  trigram_ceb_match = 0
  trigram_hil_match = 0
  trigram_rin_match = 0
  trigram_min_match = 0
  trigram_kar_match = 0

  trigram_tag_loc = "ngrams list/tag_top25_3gram.txt"
  trigram_ceb_loc = "ngrams list/ceb_top25_3gram.txt"
  trigram_bik_loc = "ngrams list/bik_top25_3gram.txt"
  trigram_hil_loc = "ngrams list/hil_top25_3gram.txt"
  trigram_rin_loc = "ngrams list/rin_top25_3gram.txt"
  trigram_min_loc = "ngrams list/min_top25_3gram.txt"
  trigram_kar_loc = "ngrams list/kar_top25_3gram.txt"

  trigram_tag_list = []
  trigram_ceb_list = []
  trigram_bik_list = []
  trigram_hil_list = []
  trigram_rin_list = []
  trigram_min_list = []
  trigram_kar_list = []

  with open(trigram_tag_loc,'r') as trigram_tag_file:
    trigram_tag_file_contents = trigram_tag_file.readlines()
    for i in trigram_tag_file_contents:
      item = i.strip().split(",")
      trigram_tag_list.append(item[0])

  with open(trigram_ceb_loc,'r') as trigram_ceb_file:
    trigram_ceb_file_contents = trigram_ceb_file.readlines()
    for i in trigram_ceb_file_contents:
      item = i.strip().split(",")
      trigram_ceb_list.append(item[0])

  with open(trigram_bik_loc,'r') as trigram_bik_file:
    trigram_bik_file_contents = trigram_bik_file.readlines()
    for i in trigram_bik_file_contents:
      item = i.strip().split(",")
      trigram_bik_list.append(item[0])

  with open(trigram_hil_loc,'r') as trigram_hil_file:
    trigram_hil_file_contents = trigram_hil_file.readlines()
    for i in trigram_hil_file_contents:
      item = i.strip().split(",")
      trigram_hil_list.append(item[0])

  with open(trigram_rin_loc,'r') as trigram_rin_file:
    trigram_rin_file_contents = trigram_rin_file.readlines()
    for i in trigram_rin_file_contents:
      item = i.strip().split(",")
      trigram_rin_list.append(item[0])

  with open(trigram_min_loc,'r') as trigram_min_file:
    trigram_min_file_contents = trigram_min_file.readlines()
    for i in trigram_min_file_contents:
      item = i.strip().split(",")
      trigram_min_list.append(item[0])

  with open(trigram_kar_loc,'r') as trigram_kar_file:
    trigram_kar_file_contents = trigram_kar_file.readlines()
    for i in trigram_kar_file_contents:
      item = i.strip().split(",")
      trigram_kar_list.append(item[0])

  for i in input_text_ngram:
    if i in trigram_tag_list:
      trigram_tag_counter += 1
    if i in trigram_bik_list:
      trigram_bik_counter += 1
    if i in trigram_ceb_list:
      trigram_ceb_counter += 1
    if i in trigram_hil_list:
      trigram_hil_counter += 1
    if i in trigram_rin_list:
      trigram_rin_counter += 1
    if i in trigram_min_list:
      trigram_min_counter += 1
    if i in trigram_kar_list:
      trigram_kar_counter += 1

  if trigram_tag_counter != 0:
    trigram_tag_match = trigram_tag_counter/input_text_ngram_count
  if trigram_bik_counter != 0:
    trigram_bik_match = trigram_bik_counter/input_text_ngram_count
  if trigram_ceb_counter != 0:
    trigram_ceb_match = trigram_ceb_counter/input_text_ngram_count
  if trigram_hil_counter != 0:
    trigram_hil_match = trigram_hil_counter/input_text_ngram_count
  if trigram_rin_counter != 0:
    trigram_rin_match = trigram_rin_counter/input_text_ngram_count
  if trigram_min_counter != 0:
    trigram_min_match = trigram_min_counter/input_text_ngram_count
  if trigram_kar_counter != 0:
    trigram_kar_match = trigram_kar_counter/input_text_ngram_count

  return trigram_tag_match,trigram_bik_match,trigram_ceb_match,trigram_hil_match,trigram_rin_match,trigram_min_match,trigram_kar_match