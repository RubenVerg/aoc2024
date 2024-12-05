in←•file.Chars "input/5.txt"

P←(¬-˜⊢×·+`»⊸>)⊸⊔
_sort←{(⍒𝔽⌜˜)⊸⊏}

pv‿lv←(>','⊸∊¨)⊸⊔' '⊸≤⊸P in
pairs←>{•ParseFloat¨'|'⊸≠⊸P𝕩}¨pv
lists←{•ParseFloat¨','⊸≠⊸P𝕩}¨lv

sorted←∊⟜pairs∘≍¨_sort¨lists

part1←+´>(2÷˜1-˜≠)⊸⊏¨sorted/˜sorted≡˘lists
part2←+´>(2÷˜1-˜≠)⊸⊏¨sorted/˜sorted≢˘lists

•Show part1
•Show part2
