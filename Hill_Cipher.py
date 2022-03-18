# Created By Yessine Jallouli on 17/03/2022

import numpy as np
from egcd import egcd
import math

def matrix_mod_inv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))  # Step 1)
    det_inv = egcd(det, modulus)[1] % modulus  # Step 2)
    matrix_modulus_inv = (
            det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % modulus
    )  # Step 3)

    return matrix_modulus_inv

def Hill_Cipher_Solver(all_cipher, plain, alphabet):
    cipher = all_cipher[0:len(plain)]
    letter_to_index = dict(zip(alphabet, range(len(alphabet))))
    index_to_letter = dict(zip(range(len(alphabet)), alphabet))
    for order in range(int(math.sqrt(len(plain))), 1, -1):
        if len(all_cipher)%order:
            continue
        matrix_system = np.array(order * [order * [0]])
        for i in range(order):
            for j in range(order):
                matrix_id = i * order + j
                matrix_system[i][j] = letter_to_index[cipher[matrix_id]]
        inv_matrix_system = matrix_mod_inv(matrix_system, len(alphabet))
        key_inverse = np.array(order * [order * [0]])
        for i in range(order):
            matrix_system_ans = np.array(order * [0])
            for j in range(i, order * order, order):
                matrix_system_ans[int(j // order)] = letter_to_index[plain[j]]
            matrix_solution = np.matmul(inv_matrix_system, matrix_system_ans) % len(alphabet)
            for j in range(order):
                key_inverse[i][j] = matrix_solution[j]
        result = ""
        for i in range(0, len(all_cipher), order):
            if i+order > len(all_cipher):
                break
            block = np.array(order * [0])
            id = 0
            for j in range(i, i + order):
                block[id] = letter_to_index[all_cipher[j]]
                id += 1
            block_sol = np.matmul(key_inverse, block) % len(alphabet)
            for j in range(order):
                result+= index_to_letter[block_sol[j]]
        ans = True
        for i in range(len(plain)):
            if result[i] != plain[i]:
                ans = False
        if ans:
            print("Flag ! ")
            print(result)
            return
    print("INVALID")
    
def main():
    # plain = "securinets"
    # alphabet = "{}abcdefghijklmnopqrstuvwxyz_"
    # all_cipher = "bbcbp_zqrafjq}ehowmdw{jifop_y_wo_hqoaoetavcicwdadgoafkatlkuf";

    print("Enter a part of the Plaintext :")
    plain = input()
    print('Enter the whole Ciphertext: ')
    all_cipher = input()
    print('Enter the alphabet :')
    alphabet = input()
    Hill_Cipher_Solver(all_cipher, plain, alphabet)

main()



# Resource : https://www.nku.edu/~christensen/Section%209%20Hill%20cipher%20cryptanalysis%20new%20examples.pdf
