import load_db

userdict = {}

def clear_answers(userID):
	global userdict
	userdict[userID].clear()

def add_answer(userID, answerText):
	global userdict
	match answerText:
		case 'cb_no':
			userdict[userID].append(1)
		case 'cb_mbno':
			userdict[userID].append(2)
		case 'cb_mbyes':
			userdict[userID].append(3)
		case 'cb_yes':
			userdict[userID].append(4)

def calc_answer_inv(answer):
	#answerInv = map(lambda x: 5 - answer[x], answer)
	for x in range(get_max_len_answer()):
	 	answerInv.append(5 - answer[x])
	return answerInv

def get_len_answer(userID):
	return len(userdict[userID])

def get_max_len_answer():
	return len(load_db.questionsText)

def add_user(userID):
	global userdict
	if userID not in userdict:
		answerlist = []
		userdict[userID] = answerlist

# def delete_user(userID):
# 	global userdict
# 	if userID in userdict:
# 		userdict.pop(userID)