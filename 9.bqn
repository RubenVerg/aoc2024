in←•file.Chars "input/9.txt"
# in←"2333133121414131402"

Part1←{
	xs←∾↕∘≠⊸({2|𝕨?('0'-˜𝕩)/⥊¯1;('0'-˜𝕩)/⥊𝕨÷2}¨)𝕩
	{𝕊: xs (¯1↓(⊢´xs)⌾((⊑xs⊐¯1)⊸⊑))↩ }•_while_{𝕊: ⊑¯1∊xs} ⟨⟩
	+´↕∘≠⊸×xs
}

Part2←{
	lens←'0'-˜𝕩
	vals←⌊⊸=⊸(×+¯1×¬∘⊣)÷⟜2↕≠𝕩
	result←0
	index←0
	{𝕊:
		l←⊑lens
		lens↓˜↩1
		v←⊑vals
		vals↓˜↩1
		{
			¯1≠v?
				result+↩+´v×index+↕l
				index+↩l;
			possible←/(¯1≠vals)∧(l≥lens)
			0≠≠possible? {
				selected←⊢´possible
				result+↩(selected⊑vals)×+´index+↕selected⊑lens
				index+↩selected⊑lens
				vals ¯1⌾(selected⊸⊑)↩
				l>selected⊑lens?
					vals∾˜↩¯1
					lens∾˜↩l-selected⊑lens
				; ⟨⟩
			}; index+↩l
		}
	}•_while_{𝕊:0≠≠vals} ⟨⟩
	result
}

•Show (Part1⋈Part1•_timed) in
•Show (Part2⋈Part2•_timed) in
