in←•file.Chars "input/1.txt"

P←(¬-˜⊢×·+`»⊸>)⊸⊔

Parse←⍉·•ParseFloat¨∘‿2⥊' '⊸<⊸P
Part1←+´·|·-˝·∧˘Parse
Part2←+´·(⊣×·+˝=⌜˜)˝Parse

•Show Part1 in
•Show Part2 in
