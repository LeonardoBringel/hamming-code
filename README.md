# Hamming Code


## :pushpin: About


### What is Hamming Code?
Developed by Richard W. Hamming, the Hamming Code is used to detect and correct errors that may occur when data is moved from the sender to the reciever.


### Parity Bits
The way that Hamming Code ensures that no bits were lost during the data transfer is by generating and adding Parity Bits.

Those bits are placed at certain positions that cover an array of the data bits. The position is determined by the power of 2 (1, 2, 4, 8...).

    (e.g.) determining the position of the parity bits for: "1 0 1 1"
    
    "_ _ 1 _ 0 1 1" (bits 1, 2, 4)


### Encode
The Parity Bit is determined by the sum of the checked bits. The Parity Bit is 0 if the result of the sum is an even number, and is 1 otherwise.

The position of the Parity Bit determines the sequence of bits that it alternatively checks and skips.

    (e.g.) following our same example: "_ _ 1 _ 0 1 1"
    
    parity 1 (bit 1) = starting by itself, checks 1 bit, skips 1, and so on 
    parity 2 (bit 2) = starting by itself, checks 2 bits, skips 2, and so on 
    parity 3 (bit 4) = starting by itself, checks 4 bits, skips 4, and so on
    
    parity 1 = 0 + 1 + 0 + 1 = 2 (even)
    parity 2 = 0 + 1 + 1 + 1 = 3 (odd)
    parity 3 = 0 + 0 + 1 + 1 = 2 (even)
    
    hamming code: "0 1 1 0 0 1 1"
Note: The parity itself assumes value 0 when being calculated.


### Decode
The way that the receiver will decode the word is very similar to the way of the sender's encoding.

The first thing to do is to locate the parity bits and recalculate them, comparing the result with the received word.

    (e.g.) received word: "0 1 1 0 1 1 1"
    
    recalculating parity
    parity 1 (bit 1) = 3 (odd) = 1
    parity 2 (bit 2) = 3 (odd) = 1
    parity 3 (bit 4) = 3 (odd) = 1

If any difference is found, it means that our data has been corrupted.
To locate the corrupted bit, simply sum the position of the parity bits that are different from the received and the result will be the position of the corrupted bit.
    
    (e.g.) received word: "0 1 1 0 1 1 1", calculated word: "1 1 1 1 1 1 1"
    
    location = 1 + 4 = 5
    
    inverting bit 5 in the received word: "0 1 1 0 0 1 1"


After correcting the bit, we can recalculate to ensure that the data is no longer corrupted and then remove the parity bits.

    (e.g.) received word: "0 1 1 0 1 1 1"
    
    original word: "1 0 1 1"


## :sparkles: Main Features

* Calculate Hamming Code
* Single-bit error correction
* Decode Hamming Code
