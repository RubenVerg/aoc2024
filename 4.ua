# Experimental!

In ← &fras "input/4.txt"

S  ← "XMAS"
Sd ← ⨬@\W∘ ⊸(⊞=.) S

Part₁ ← /+♭[
  ⊃(⌕ S
  | ⌕ ⇌S
  | ⌕ S⍉
  | ⌕ ⇌S⍉
  | ⌕ Sd
  | ⌕ Sd⇌⍉
  | ⌕ Sd⇌⍉⇌⍉
  | ⌕ Sd⍉⇌
  )]⊜∘⊸≠@\n

C ← ["M\WS" "\WA\W" "M\WS"]

Part₂ ← /+♭[
  ⊃(⌕ C
  | ⌕ ⇌⍉C
  | ⌕ ⇌⍉⇌⍉C
  | ⌕ ⍉⇌C
  )]⊜∘⊸≠@\n

$₁ Part₁ In
$₂ Part₂ In