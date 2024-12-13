in←•file.Chars "input/13.txt"

P←(¬-˜⊢×·+`»⊸>)⊸⊔

Parse←(⌊6÷˜↕∘≠)⊸⊔·•ParseFloat¨∊⟜('0'+↕10)⊸P

Solve←{𝕊xa‿ya‿xb‿yb‿xg‿yg: det←(xa×yb)-(xb×ya) ⋄ { 0=det? 0; ab←det÷˜⟨(yb×xg)-(xb×yg),(xa×yg)-(ya×xg)⟩ ⋄ { ⌊⊸≡ab? +´3‿1×ab ; 0 } }}

Part1←+´·Solve¨Parse
Part2←+´·(Solve +⟜0‿0‿0‿0‿10000000000000‿10000000000000)¨Parse

•Show (Part1⋈Part1•_timed) in
•Show (Part2⋈Part2•_timed) in