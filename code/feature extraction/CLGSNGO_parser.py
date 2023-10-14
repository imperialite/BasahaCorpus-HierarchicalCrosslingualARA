from CLGSNGO import *
import pandas as pd

with open('bikolano.txt', 'r', encoding='utf-8', errors='ignore') as file:
	file_contents = file.readlines()

	label = []
	title = []

	tag_bigram = []
	bik_bigram = []
	ceb_bigram = []
	hil_bigram = []
	rin_bigram = []
	min_bigram = []
	kar_bigram = []

	tag_trigram = []
	bik_trigram = []
	ceb_trigram = []
	hil_trigram = []
	rin_trigram = []
	min_trigram = []
	kar_trigram = []

	for item in file_contents:
		parsed_text = item.split(',',2)
		parsed_text[2] = parsed_text[2].strip()

		print(parsed_text[0], parsed_text[1])

		title.append(parsed_text[0])
		label.append(parsed_text[1])

		tag_output, bik_output, ceb_output, hil_output, rin_output, min_output, kar_output = get_bigram_CLGSNGO(parsed_text[2])
		tag_bigram.append(tag_output)
		bik_bigram.append(bik_output)
		ceb_bigram.append(ceb_output)
		hil_bigram.append(hil_output)
		rin_bigram.append(rin_output)
		min_bigram.append(min_output)
		kar_bigram.append(kar_output)

		tag_output, bik_output, ceb_output, hil_output, rin_output, min_output, kar_output = get_trigram_CLGSNGO(parsed_text[2])
		tag_trigram.append(tag_output)
		bik_trigram.append(bik_output)
		ceb_trigram.append(ceb_output)
		hil_trigram.append(hil_output)
		rin_trigram.append(rin_output)
		min_trigram.append(min_output)
		kar_trigram.append(kar_output)

df = pd.DataFrame(list(zip(title, tag_bigram, bik_bigram, ceb_bigram, hil_bigram, rin_bigram, min_bigram, kar_bigram, tag_trigram, bik_trigram, ceb_trigram, hil_trigram, rin_trigram, min_trigram, kar_trigram, label)),columns=['book_title','tag_bigram_sim','bik_bigram_sim','ceb_bigram_sim','hil_bigram_sim','rin_bigram_sim','min_bigram_sim','kar_bigram_sim','tag_trigram_sim','bik_trigram_sim','ceb_trigam_sim', 'hil_trigam_sim','rin_trigam_sim','min_trigam_sim','kar_trigam_sim','grade_level'])

df.to_csv('bik_clgsngo.csv',index=False)

print('\nFEATURE EXTRACTION DONE')