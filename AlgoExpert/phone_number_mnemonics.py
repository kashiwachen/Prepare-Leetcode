import pdb


DIGIT_LETTER = {
	"0": "0",
	"1": "1",
	"2": ["a", "b", "c"],
	"3":["d", "e", "f"],
	"4":["g", "h", "i"],
	"5":["j", "k", "l"],
	"6":["m", "n", "o"],
	"7":["p", "q", "r", "s"],
	"8":["t", "u", "v"],
	"9":["w", "x", "y", "z"],
}


def phoneNumberMnemonics(phoneNumber):
    # Write your code 
    mnemonics_list = phone_number_mnemonics_helper(0, phoneNumber, [], [])
    return mnemonics_list

def phone_number_mnemonics_helper(idx, phone_number, current_mnemonics, mnemonics_list):
    if idx == len(phone_number):
        pdb.set_trace()
        current_mnemonics = "".join(current_mnemonics)
        mnemonics_list.append(current_mnemonics)
        return mnemonics_list
    else:
        digit = phone_number[idx]
        letters = DIGIT_LETTER[digit]
        for letter in letters:
            print(current_mnemonics)
            next_mnemonics = current_mnemonics + letter
            mnemonics_list = phone_number_mnemonics_helper(
                idx+1, phone_number, next_mnemonics, mnemonics_list
                )
phoneNumberMnemonics("1905")
