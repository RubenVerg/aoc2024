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
	log_i←1+⌊10⋆⁼i
	pow_i←10⋆log_i
	check_catenation←i=pow_i|target
	{
		check_prod∧check_catenation?(is Check2˜target-i)∨(is Check2˜target÷i)∨(is Check2˜⌊target÷pow_i);
		check_prod?(is Check2˜target-i)∨(is Check2˜target÷i);
		check_catenation?(is Check2˜target-i)∨(is Check2˜⌊target÷pow_i);
		is Check2˜target-i
	}
}
Part2←+´·⊑˘·Check2´˘⊸/Parse

•Show (Part1⋈Part1•_timed) in
•Show (Part2⋈Part2•_timed) in
