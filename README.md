# mmoc
mmoc - find similarities in binary files

WARNING: Not pythonic at all

## What it does:
Let's say you have two binary files you believa are compromised by the same bad code.
With mmoc you can easily compare the two files and find out similarities.

You can also specify a data-chunk size in order to avoid false posivies and have a better understaning of the malicious code.

## how it works

  $ python mmoc.py -f1 fileone.exe -f2 filetwo.exe -cs 32

##### Results:

  DeleteCriticalSe 44656c657465437269746963616c5365
  
  MultiByteToWideC 4d756c746942797465546f5769646543
  
  zeCriticalSectio 7a65437269746963616c53656374696f
  
  etUnhandledExcep 6574556e68616e646c65644578636570
  
  eaveCriticalSect 65617665437269746963616c53656374
  
  eCharToMultiByte 6543686172546f4d756c746942797465
