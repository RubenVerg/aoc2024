in←•file.Chars "input/14.txt"

P←(¬-˜⊢×·+`»⊸>)⊸⊔

size←101‿103
its←100

Parse←>·⍉·>·⟨⟨0⟩‿⟨1⟩,⟨2⟩‿⟨3⟩⟩⊸⊑¨·(⌊4÷˜↕∘≠)⊸⊔·•ParseFloat¨∊⟜('-'∾'0'+↕10)⊸P

Part1←its⊸{its𝕊[pos,vel]:×´≠¨(⊐(<⟜⌊∾<⟜⌈)⟜(size÷2)⎉1)⊸⊔ (<⟜⌊≡<⟜⌈)⟜(size÷2)⎉1⊸/ size|⎉1 pos+vel×⎉1 size|its} Parse
Part2←{𝕊[pos,vel]: res←0 ⋄ {
	mat←1¨⌾((<˘size|⎉1 pos+vel×⎉1 size|𝕩)⊸⊑) size⥊0
	∨´⥊mat⍷˜⥊˘20⥊1? res←𝕩 ; ⟨⟩
}¨↕×´size ⋄ res} Parse

•Show (Part1⋈Part1•_timed) in
•Show Part2 in
