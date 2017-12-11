from pprint import pprint

items = {61170, 51206, 63455, 37985, 47604, 61260, 51853, 27713, 39404, 25287, 20853, 37492, 65262, 22132, 8396, 24308,
				 43064, 50827, 30481, 65172, 63318, 17272, 60912, 58712, 20444, 48950, 9463, 4627, 13382, 13774, 22912, 6723}
bags = [1111062, 666431, 848372, 1096306, 503315, 1110531, 708859, 1173231, 681602, 672415, 1086793, 806143, 505906,
				776307, 616308, 525781]

bbag = max(bags)
combo_list = dict()
for i in items:
	combo_list[i] = {i}

useful_bags = set()
print('Biggest bag: {}'.format(bbag))

iter = 0
while min(combo_list) < bbag:
	sm_set = min(combo_list)
	if sm_set in bags:
		useful_bags.add(sm_set)
		print('Match for {}'.format(sm_set))
		pprint(combo_list[sm_set])
	if (iter % 1000) == 0:
		print('New iteration: {} sets, smallest sum is {}'.format(len(combo_list), sm_set))
	iter += 1
	new_set = combo_list[sm_set]
	del combo_list[sm_set]
	for a_bag in items:
		if a_bag not in new_set:
			combo_list[a_bag + sm_set] = new_set | {a_bag}

print('Smallest combo: {}'.format(min(combo_list)))
# pprint(combo_list)
out = ''
for b in bags:
	out += '1' if b in useful_bags else '0'
print('Done: {}'.format(out))
