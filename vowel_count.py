enter_input = input('Enter word to count vowel: ').split()
if len(enter_input) > 1:
    print('Breaking the script as it has more than one word.')
else:
    gathering_string=enter_input[0]
    vow_count = [val for val in gathering_string if val in 'AaEeIiOoUu']
    print(len(vow_count))
    print('Vowels found: ', vow_count)
    

