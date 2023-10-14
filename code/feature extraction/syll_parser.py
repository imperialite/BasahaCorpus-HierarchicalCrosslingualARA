from TRAD import *
from SYLL import *
import pandas as pd

with open('karaya.txt', 'r', encoding='utf-8', errors='ignore') as file:
	file_contents = file.readlines()

	label = []
	title = []

	consonant_cluster = [] #kk pattern
	v_density = []
	cv_density = []
	vc_density = []
	cvc_density = []
	vcc_density = []
	cvcc_density = []
	ccvc_density = []
	ccv_density = []
	ccvcc_density = []
	ccvccc_density = []

	for item in file_contents:
		parsed_text = item.split(',',2)
		parsed_text[2] = parsed_text[2].strip()

		print(parsed_text[0], parsed_text[1])

		title.append(parsed_text[0])
		label.append(parsed_text[1])

		consonant_cluster.append(get_consonant_cluster(parsed_text[2]))
		v_density.append(get_v(parsed_text[2]))
		cv_density.append(get_cv(parsed_text[2]))
		vc_density.append(get_vc(parsed_text[2]))
		cvc_density.append(get_cvc(parsed_text[2]))
		vcc_density.append(get_vcc(parsed_text[2]))
		cvcc_density.append(get_cvcc(parsed_text[2]))
		ccv_density.append(get_ccv(parsed_text[2]))
		ccvc_density.append(get_ccvc(parsed_text[2]))
		ccvcc_density.append(get_ccvcc(parsed_text[2]))
		ccvccc_density.append(get_ccvccc(parsed_text[2]))

df = pd.DataFrame(list(zip(title, consonant_cluster, v_density, cv_density, vc_density, cvc_density, vcc_density, cvcc_density, ccvc_density, ccv_density,ccvcc_density, ccvccc_density, label)),columns=['book_title', 'consonant_cluster_density', 'v_density', 'cv_density', 'vc_density','cvc_density','vcc_density','cvcc_density','ccvc_density','ccv_density','ccvcc_density','ccvccc_density','grade_level'])

df.to_csv('kar_syll.csv',index=False)

print('\nFEATURE EXTRACTION DONE')