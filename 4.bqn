in←•file.Chars "input/4.txt"

P←(¬-˜⊢×·+`»⊸>)⊸⊔
Diag←>≠↑¨(+⌜´↕¨∘≢)⊸⊔

Part1←{+´(+´·⥊"XMAS"⊸⍷)¨⟨⊢,⌽˘,⍉,⌽˘⍉,Diag,⌽˘Diag,Diag⌽,⌽˘·Diag⌽⟩{𝕎𝕩}¨<>' '⊸<⊸P 𝕩}
Part2←{+´∊⟜["MMASS","MSAMS","SSAMM","SMASM"]˘∾˝⟨0‿0,0‿2,1‿1,2‿0,2‿2⟩⊸⊑⎉2 3‿3↕>' '⊸<⊸P 𝕩}

•Show Part1 in
•Show Part2 in
