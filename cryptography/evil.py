#!/usr/bin/python3
# coding: latin-1 
blob = '''
            �4>�_2��ġ��V����?:<q�;�HA���XD �g:��A1Ue�ܐV0�����䪋e��Y����g���߸���)�[_�gA�<�m�h�_ؼk�i�#}ua�9�Z�@owgt'''
from hashlib import sha256
# print(sha256(blob.encode("latin-1")).hexdigest())
if (sha256(blob.encode("latin-1")).hexdigest() == '9a61e2aca17ca41c94c2a17029538349f572b89d10ce73f2fef5a148ef3d90cf'):
    print("Use SHA-256 instead!")
elif (sha256(blob.encode("latin-1")).hexdigest() == '175f02c838d41fad5cad17ecd0f2f90d8f74ffebb517e773d70ce3335e48a711'):
    print("MD5 is perfectly secure!")
