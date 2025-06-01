alphabet_letters = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
    "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

possible_alpha_values = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

def decode_message(alpha_value, beta_value, coded_text):
    
    decoded_message = ""
    
    for character in coded_text:
        
        if character != " ":
            
            original_index = alphabet_letters.index(character)
            
            for decoded_index in range(26):
                
                if (alpha_value * decoded_index + beta_value) % 26 == original_index:
                    
                    decoded_character = alphabet_letters[decoded_index]
                    break
                    
            decoded_message += decoded_character
            
        else:
            
            decoded_message += " "
    
    return decoded_message


number_of_cases = int(raw_input())

for case_index in range(number_of_cases):
    
    encrypted_code = raw_input()
    
    found_valid_decoding = False
    
    for alpha_candidate in possible_alpha_values:
        
        if found_valid_decoding:
            break
        
        for beta_candidate in range(26):
            
            decrypted_text = decode_message(alpha_candidate, beta_candidate, encrypted_code)
            
            if "that" in decrypted_text or "this" in decrypted_text:
                
                found_valid_decoding = True
                break
    
    print decrypted_text