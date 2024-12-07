in←•file.Chars "input/7.txt"

P←(¬-˜⊢×·+`»⊸>)⊸⊔

Parse←>·{a‿bs←':'⊸≠⊸P 𝕩⋄⟨•ParseFloat a, ⌽•ParseFloat¨' '⊸≠⊸P bs⟩}¨' '⊸≤⊸P

Check1←{
	·𝕊⟨⟩: 0;
	target𝕊⟨i⟩: i=target;
	target𝕊ints:
	i←⊑ints
	is←1↓ints
	{0=i|target?(is Check1˜target-i)∨(is Check1˜target÷i);is Check1˜target-i}
}
Part1←+´·⊑˘·Check1´˘⊸/Parse

Check2←{
	·𝕊⟨⟩: 0;
	target𝕊⟨i⟩: i=target;
	target𝕊ints:
	i←⊑ints
	is←1↓ints
	check_prod←0=i|target
	str_i←•Fmt i
	check_catenation←str_i≡(-≠str_i)↑•Fmt target
	{
		check_prod∧check_catenation?(is Check2˜target-i)∨(is Check2˜target÷i)∨(is Check2˜⌊target÷10⋆≠str_i);
		check_prod?(is Check2˜target-i)∨(is Check2˜target÷i);
		check_catenation?(is Check2˜target-i)∨(is Check2˜⌊target÷10⋆≠str_i);
		is Check2˜target-i
	}
}
Part2←+´·⊑˘·Check2´˘⊸/Parse

•Show Part1 in
•Show Part2 in
