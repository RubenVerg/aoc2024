in←•file.Chars "input/6.txt"

P←(¬-˜⊢×·+`»⊸>)⊸⊔
FindBoth←{a‿b←⥊𝕨 ⋄ »⎉(=𝕨)⊸∨ (a=𝕩) ∧ «⎉(=𝕨) b=𝕩}
_ne←{0=≠𝕩?𝕩;𝔽𝕩}
_fix←{p←⟨⟩⋄𝔽•_while_{r←¬⊑p∊˜<𝕩⋄p∾↩<𝕩⋄r}𝕩}
PadMat←⊣(⊣∾˘⊢∾˘⊣)⊢(⊣∾⊢∾⊣)˜⊣⥊˜≠∘⊢

Move←{⌽'X'¨⌾((𝕩='.')⊸/)𝕩}
MoveStep←{Move⌾((/⥊∨´FindBoth⟜𝕩¨⟨[".","^"],["X","^"],">.",">X",["v","."],["v","X"],".<","X<"⟩)⊏⥊) 𝕩}
Turn←"^>v<"⊸(⊑⊣⊏˜≠∘⊣|1+⊐)
TurnStep←{{Turn⌾⊑⌾(('#'≠𝕩)⊸/)𝕩}_ne⌾((/⥊∨´FindBoth⟜𝕩¨⟨["#","^"],">#",["v","#"],"#<"⟩)⊏⥊) 𝕩}

Step←TurnStep MoveStep
Traverse←Step _fix
Completes←(0=¬○(+´·⥊·'X'⊸=Traverse)⟜('.'⊸PadMat))

Parse←>' '⊸<⊸P
Part1←{1++´⥊'X'=Traverse Parse𝕩}
Part2←{1-˜+´(Parse𝕩)⊸{¬Completes '#'⌾(𝕩⊸⊑)𝕨}¨⍷⥊⟨0‿0,0‿1,1‿0,0‿¯1,¯1‿0⟩+⌜'X'⊸=⊸/○⥊⟜(↕≢)Traverse Parse𝕩}

•Show Part1 in
•Show Part2 in
