in←•file.Chars "input/6.txt"

P←(¬-˜⊢×·+`»⊸>)⊸⊔
PadMat←⊣(⊣∾˘⊢∾˘⊣)⊢(⊣∾⊢∾⊣)˜⊣⥊˜≠∘⊢
AnyWhere←/○⥊⟜(↕≢)
OutOfBounds←∨´(0>⊢)∾≢⊸≤

Parse←>' '⊸<⊸P

Traverse←{
	¬⊑'^'∊⥊𝕩? 0‿2⥊0;
	grid←𝕩
	pos←⊑AnyWhere'^'=grid
	dir←¯1‿0
	continue←1
	visited←0‿2⥊0
	visited_dir←0‿4⥊0
	{𝕊:
	  grid OutOfBounds pos+dir?continue↩0;
		⊑visited_dir∊˜dir∾˜pos+dir?continue↩0;
		'#'=grid⊑˜pos+dir?dir↩1‿¯1×⌽dir;
		pos↩pos+dir ⋄ visited↩visited∾pos ⋄ visited_dir↩visited_dir∾pos∾dir
	}•_while_{𝕊: continue} ⟨⟩
	⍷visited
}
Completes←(0=¬○(≠Traverse)⟜('.'⊸PadMat))

Part1←{1+≠Traverse Parse𝕩}
Part2←{
	grid←Parse𝕩
	check←⍷⥊⟨0‿0,0‿1,1‿0,0‿¯1,¯1‿0⟩+⌜ <˘Traverse grid
	1-˜+´{¬Completes '#'⌾(𝕩⊸⊑)grid}⎊0¨ check
}

•Show Part1 in
•Show Part2 in

