import load_db
import calc_answer

def get_rare_case_result(IOA, IOE):
	if IOA < 270:
		if IOE < 90:
			finalResult = 'Сложный смешанный тип темперамента: флегматик-меланхолик и флегматик-сангвиник' + output_temperament('MF') + output_temperament('S')
		else:
			finalResult = 'Сложный смешанный тип темперамента: меланхолик-холерик и меланхолик-флегматик' + output_temperament('MH') + output_temperament('F')
	else:
		if IOE < 90:
			finalResult = 'Сложный смешанный тип темперамента: сангвиник-холерик и сангвиник-флегматик' + output_temperament('SF') + output_temperament('H')
		else:
			finalResult = 'Сложный смешанный тип темперамента: холерик-сангвиник и холерик-меланхолик' + output_temperament('HS') + output_temperament('M')
	return finalResult

def output_temperament(inputCode):
	#load_db.resultText[1] - сангвиник
	#load_db.resultText[2] - меланхолик
	#load_db.resultText[3] - холерик
	#load_db.resultText[4] - флегматик
	#load_db.resultText[5] - Меланхолик-флегматик
	#load_db.resultText[6] - Сангвиник-флегматик
	#load_db.resultText[7] - Меланхолик-холерик
	#load_db.resultText[8] - Холерик-сангвиник
	outputText = '\n\n'
	match inputCode:
		case 'S':
			outputText += load_db.resultText[1]
		case 'M':
			outputText += load_db.resultText[2]
		case 'H':
			outputText += load_db.resultText[3]
		case 'F':
			outputText += load_db.resultText[4]
		case 'MF':
			outputText += load_db.resultText[5] + '\n\n' + load_db.resultText[2] + '\n\n' + load_db.resultText[4]
		case 'SF':
			outputText += load_db.resultText[6] + '\n\n' + load_db.resultText[1] + '\n\n' + load_db.resultText[4]
		case 'MH':
			outputText += load_db.resultText[7] + '\n\n' + load_db.resultText[2] + '\n\n' + load_db.resultText[3]
		case 'HS':
			outputText += load_db.resultText[8] + '\n\n' + load_db.resultText[3] + '\n\n' + load_db.resultText[1]
	return outputText

def calc_final_result(userID):
	answer = calc_answer.userdict[userID]
	answerInv = calc_answer.calc_answer_inv(answer)
	
	ERP = answer[0]+answer[3]+answer[31]+answer[57]+answerInv[59]+answerInv[69]+answerInv[74]+answer[83]+answer[91]+answerInv[110]+answer[126]+answer[131]
	ERI = answer[2]+answer[8]+answerInv[16]+answer[35]+answer[47]+answerInv[53]+answer[81]+answerInv[95]+answerInv[119]+answerInv[132]+answer[138]+answer[142]
	ERK = answerInv[6]+answer[32]+answer[34]+answerInv[62]+answer[67]+answer[76]+answer[93]+answerInv[97]+answer[111]+answerInv[113]+answer[124]+answerInv[128]

	PM = answer[10]+answer[12]+answer[38]+answer[39]+answer[63]+answerInv[65]+answer[75]+answer[78]+answer[98]+answer[99]+answer[114]+answerInv[130]
	PI = answerInv[1]+answer[7]+answer[17]+answer[40]+answer[46]+answer[58]+answer[94]+answerInv[96]+answerInv[106]+answer[129]+answerInv[139]+answer[148]
	PK = answer[14]+answer[20]+answer[42]+answer[45]+answer[50]+answer[66]+answer[79]+answer[100]+answerInv[112]+answer[115]+answer[133]+answer[134]

	CM = answer[15]+answer[18]+answer[44]+answer[48]+answer[68]+answerInv[82]+answer[92]+answer[101]+answerInv[117]+answer[121]+answer[127]+answerInv[135]
	CI = answer[4]+answer[13]+answer[22]+answerInv[26]+answerInv[37]+answer[52]+answerInv[61]+answer[64]+answer[86]+answer[118]+answerInv[141]+answer[144]
	CK = answerInv[19]+answerInv[49]+answer[56]+answer[70]+answerInv[80]+answer[84]+answerInv[87]+answerInv[90]+answer[103]+answer[116]+answer[122]+answerInv[136]

	EMP = answer[21]+answer[23]+answer[51]+answer[54]+answer[72]+answer[77]+answer[88]+answer[104]+answer[107]+answer[123]+answer[140]+answer[143]
	EMI = answer[5]+answer[9]+answer[11]+answer[24]+answer[27]+answer[30]+answer[36]+answer[43]+answer[60]+answer[102]+answer[105]+answer[146]
	EMK = answer[25]+answer[29]+answer[55]+answer[71]+answer[73]+answer[89]+answer[108]+answer[109]+answer[125]+answer[137]+answer[145]+answer[147]

	IPA = ERP + PM + CM
	IIA = ERI + PI + CI
	IKA = ERK + PK + CK

	IOA = IPA + IIA + IKA
	IOE = EMP + EMI + EMK
	IOAD = IOA - IOE

	if IOA < 234:
		if IOE < 78:
			finalResult = 'Ваш темперамент: Флегматик' + output_temperament('F')
		elif IOE >= 78 and IOE <= 102:
			finalResult = 'У вас смешанный темперамент: Меланхолик-флегматик' + output_temperament('MF')
		elif IOE > 102:
			finalResult = 'Темперамент: Меланхолик' + output_temperament('M')
	elif IOA >= 234 and IOA <= 306:
		if IOE < 78:
			finalResult = 'Смешанный темперамент: Сангвиник-флегматик' + output_temperament('SF')
		elif IOE >= 78 and IOE <= 102:
		 	finalResult = get_rare_case_result(IOA, IOE)
		elif IOE > 102:
			finalResult = 'Смешанный темперамент: Меланхолик-холерик' + output_temperament('MH')
	elif IOA > 306:
		if IOE < 78:
			finalResult = 'Темперамент: Сангвиник' + output_temperament('S')
		elif IOE >= 78 and IOE <= 102:
			finalResult = 'Смешанный темперамент: Холерик-сангвиник' + output_temperament('HS')
		elif IOE > 102:
			finalResult = 'Темперамент: Холерик' + output_temperament('H')

	finalResult += '\n\n Для повторного прохождения теста нажмите /start'
	return(finalResult)