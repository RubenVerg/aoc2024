in←•file.Chars "input/11.txt"

P←(¬-˜⊢×·+`»⊸>)⊸⊔

Parse←'0'-˜·>' '⊸<⊸P
D←1+·⌊10⋆⁼⊢

Step←{(⊑∘⊑⋈1⊑+´)¨(⊐⊑¨)⊸⊔∾{𝕊k‿v:{0=k?⋈⟨1,v⟩;2|D k?⋈⟨k×2024,v⟩;⟨⟨⌊k÷10⋆2÷˜D k,v⟩,⟨k|˜10⋆2÷˜D k,v⟩⟩}}¨𝕩}

Part1←{+´¯1⊸⊑¨Step⍟25 ⋈⟜1¨•ParseFloat¨' '⊸≠⊸P 𝕩}
Part2←{+´¯1⊸⊑¨Step⍟75 ⋈⟜1¨•ParseFloat¨' '⊸≠⊸P 𝕩}

•Show (Part1⋈Part1•_timed) in
•Show (Part2⋈Part2•_timed) in
