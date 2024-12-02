in←•file.Chars "input/2.txt"

P←(¬-˜⊢×·+`»⊸>)⊸⊔

Parse←(•ParseFloat¨' '⊸≠⊸P)¨' '⊸≤⊸P
Safe←(∧⊸≡∨∨⊸≡)∧(∧´1‿2‿3∊˜·|∘-´˘2↕⊢)
Part1←+´·Safe¨Parse
Part2←+´·(∨´·Safe˘⊢/˜⎉∞‿1≠⌜˜∘↕∘≠)¨Parse

•Show Part1 in
•Show Part2 in
