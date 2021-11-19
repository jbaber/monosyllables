#!/usr/bin/env python3

from itertools import groupby

VOWELS = [ "AA", "AA0", "AA1", "AA2", "AE", "AE0", "AE1", "AE2", "AH",
"AH0","AH1", "AH2", "AO", "AO0", "AO1", "AO2", "AW", "AW0", "AW1", "AW2",
"AY","AY0", "AY1", "AY2", "EH", "EH0", "EH1", "EH2", "ER", "ER0", "ER1",
"ER2","EY", "EY0", "EY1", "EY2", "IH", "IH0", "IH1", "IH2", "IY", "IY0",
"IY1","IY2", "OW", "OW0", "OW1", "OW2", "OY", "OY0", "OY1", "OY2","UH", "UH0",
"UH1", "UH2", "UW", "UW0", "UW1", "UW2",]

CONSONANTS = ["B", "CH", "D", "DH","F", "G", "HH","JH", "K", "L", "M", "N",
"NG","P", "R", "S", "SH", "T", "TH","V", "W", "Y", "Z", "ZH", ]


def good_line(line):
  return (
    not line.startswith(";;;")
    and line.split("  ")[0].isalpha()
  )


def main():
    with open("cmudict-0.7b", encoding="ISO-8859-1") as f:
        counter = 0
        for line in f:
            if good_line(line):
                word, pronunciation = line.split("  ")
                pronunciation = pronunciation.strip()

                pieces = pronunciation.split()
                states = []
                for piece in pieces:
                    if piece in VOWELS:
                        states.append("vowel")
                    elif piece in CONSONANTS:
                        states.append("consonant")
                    else:
                        print(f"What is '{pieces[0]}'?")
                        break

                # Group duplicates together
                states = [i[0] for i in groupby(states)]

                if len(states) > 3:
                    continue

                if states == ["vowel", "consonant", "vowel",]:
                    continue

                # print(f"{word} ({pronunciation}): {states}")
                print(word.capitalize())


if __name__ == "__main__":
    main()
