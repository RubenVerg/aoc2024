in←•file.Chars "input/8.txt"

P←(¬-˜⊢×·+`»⊸>)⊸⊔
OutOfBounds←∨´(0>⊢)∾≢⊸≤

Parse←>' '⊸<⊸P

Part1←{𝕊grid: ≠¬∘(grid⊸OutOfBounds)¨⊸/⍷∾⥊{(𝕨(≢∧=○(⊑⟜grid)∧'.'≠grid⊑˜⊢)𝕩)/⋈𝕩-˜2×𝕨}⌜˜⥊↕≢ grid}Parse
# ↓ currently not working
Part2←{𝕊grid: ≠¬∘(grid⊸OutOfBounds)¨⊸/⍷∾⥊{(𝕨(≢∧=○(⊑⟜grid)∧'.'≠grid⊑˜⊢)𝕩)/𝕨{m←÷˜´𝕨-𝕩 ⋄ b←-˜´m‿1⊸×𝕨 ⋄ ⌊⊸=∘⊑∘⌽¨⊸/⋈¨⟜(b+m×⊢)↕≠⊏grid}𝕩}⌜˜⥊↕≢ grid}Parse

•Show (Part1⋈Part1•_timed) in
•Show (Part2⋈Part2•_timed) in
