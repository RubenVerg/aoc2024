in←•file.Chars "input/10.txt"

P←(¬-˜⊢×·+`»⊸>)⊸⊔
AnyWhere←/○⥊⟜(↕≢)
_fix←{𝔽∘⊢⍟≢⟜𝔽_𝕣∘⊢⍟≢⟜𝔽𝕩}
Neighbors←{h‿w𝕊y‿x: {x≠0?⋈⟨y,x-1⟩;⟨⟩}∾{x≠w-1?⋈⟨y,x+1⟩;⟨⟩}∾{y≠0?⋈⟨y-1,x⟩;⟨⟩}∾{y≠h-1?⋈⟨y+1,x⟩;⟨⟩}}

Parse←'0'-˜·>' '⊸<⊸P

Parts←{
	grid←Parse 𝕩
	queue←{⟨⟨𝕩⟩,0⟩}¨AnyWhere 0=grid
	paths←⟨⟩
	Step←{
		0=≠𝕩?𝕩;
		grid𝕊queue:
		path‿depth←⊑queue
		queue↓˜↩1
		pos←⊢´path
		{
			9=depth?queue⊣paths∾↩<path;
			ns←(≢grid)Neighbors pos
			ds←ns⊑grid
			queue⊣ns{𝕩=1+depth?queue∾↩<⟨path∾<𝕨,𝕩⟩;⟨⟩}¨ds
		}
	}
	grid⊸Step _fix queue
	(≠⋈˜·≠·⍷(⊑∾⊢´)¨)paths
}

•Show Parts in
•Show Parts •_timed in
