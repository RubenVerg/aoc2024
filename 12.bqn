# thanks @dzaima for help in a couple spots

in←•file.Chars "input/12.txt"

P←(¬-˜⊢×·+`»⊸>)⊸⊔
AnyWhere←/○⥊⟜(↕≢)
OutOfBounds←∨´(0>⊢)∾≢⊸≤
InBounds←¬OutOfBounds

Parse←>' '⊸<⊸P

Flood←{
  start𝕊grid:
  result←(<start)≡¨↕≢grid
  {
    𝕊last:
    (⊢⊣{𝕊⟨⟩:result;result(1¨⌾(𝕩⊸⊑))↩})⍷⊑⟜grid¨⊸/(¬⊑⟜result)¨⊸/result⊸InBounds¨⊸/⥊⟨¯1‿0,1‿0,0‿¯1,0‿1⟩+⌜last
  }•_while_(0≠≠)⋈start
  result
}
Regions←0¨⊸{∧´⥊0≠𝕨?𝕨;idx←⊑AnyWhere 0=𝕨⋄𝕩𝕊˜𝕨+(1+⌈´⥊𝕨)×(idx Flood idx⊸⊑⊸=𝕩)}

Part1←{+´(≠¨⊔˜𝕩)×+´¨𝕩⊔+´⟨«,»,«˘,»˘⟩{𝕩≠𝕎𝕩}¨<𝕩}·Regions Parse

•Show (Part1⋈Part1•_timed) in