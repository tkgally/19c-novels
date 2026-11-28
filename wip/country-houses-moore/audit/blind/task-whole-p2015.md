You are transcribing one scanned page of a novel printed in English before 1914, for an accurate public edition.

## Reading rules

- Transcribe EXACTLY the words, spelling, capitals, and punctuation marks that are printed. Do not correct, modernize, regularize, translate, summarize, or omit anything: old, dialect, and inconsistent spellings (`shew`, `to-day`, `connexion`, `chuse`, `neophite`, `honour`, `parlour`), archaic contractions, proper names, and apparent misprints all stay exactly as printed. Read proper names, dialect, and foreign words letter by letter; never replace an unusual spelling with a more familiar or modern form.
- Spacing is the one thing that is modernized: no space before `;` `:` `!` `?` or inside quotation marks, even where the print has one; contractions printed with a space are closed up (`do n't` → `don't`); dashes are closed up to the words on both sides.
- Rejoin words hyphenated across line ends (`inter-` / `national` → `international`), but keep a hyphen that belongs to the word (`to-` / `day` → `to-day`, `drawing-` / `room` → `drawing-room`, `twenty-` / `third` → `twenty-third`). If the LAST word on the page is broken by a hyphen, keep the trailing hyphen exactly as printed.
- Typographic characters as printed: curly quotes “ ” ‘ ’, em dash —, accented letters, £, ½, °. Ligatures as plain letters (fi, fl, æ and œ stay as æ, œ). Long s (ſ) is written s.
- Italics: mark every italic run with `<i>…</i>` (foreign words, titles, emphasis, stage directions), with punctuation, parentheses, or brackets inside the tag ONLY if those marks themselves are printed in italic (`(<i>aside</i>)`, NOT `<i>(aside)</i>`).
- Small capitals: wrap in `<sc>…</sc>` and type them in lower case, with a capital only where the print has a visibly taller full capital (`<sc>London</sc>`, a chapter's opening words `T<sc>he</sc>`). Text in full-size capitals stays as plain capitals, without the tag.
- OMIT: running heads and feet, the page number, printers' signature marks at the foot of the page (`B 2`, `VOL. I. C`), catchwords, the “To face p. N” line printed under a plate, library stamps, and pencil marks.
- Quotation marks repeated at the start of each printed line of a quotation (common in 18th-century printing): type only the quotation's own opening mark and its closing mark, not the repeats.


## Your task now: PROOFREAD a transcription against the scan (do not transcribe)

Below is a transcription of one page, made under the rules above and shown as plain text: italics, small
capitals, footnotes, and their marks have been removed on purpose — do not report them. It may begin or end in
the middle of a sentence.

Compare it with the scan word by word and letter by letter, and report EVERY place where the transcription
does not say what the print says:
- a wrong letter or word; a spelling that has been modernized or "corrected" (the printed spelling always wins,
  even an obvious misprint — look hard at every word that looks modern: `show` for printed `shew`,
  `today` for `to-day`, `connection` for `connexion`), and at every proper name and foreign word;
- a wrong capital or lower-case initial; a missing or added word; a missing line or sentence; words that are not
  on the page; a wrong punctuation mark; a wrong paragraph break.
Do NOT report the conventions of the transcription: ligatures written as plain letters, modern spacing around
punctuation and inside quotation marks, words rejoined across line ends, omitted running heads, page numbers,
and signature marks, straight or curly quotes, dash length, tables left out.

The transcription reads fluently even where it is wrong, so do not read it for sense: check it against the
shapes on the scan. Open the page image `/tmp/novels/country-houses-moore/pages/p2015.jpg` with `view_file` first.
CRITICAL: Inspect ONLY the scan image `/tmp/novels/country-houses-moore/pages/p2015.jpg` and this task file; NEVER read any other directory (`_secret/`, `pages/`, `draft/`, `verify/`, `judge/`).

Write one JSON object per difference, one per line, and nothing else, to `/home/antigravity/tkgally/19c-novels/wip/country-houses-moore/audit/whole/p2015.txt`:
{"given": "4 to 8 consecutive words copied exactly from the transcription, including the wrong part", "print": "the same words exactly as the scan prints them", "sure": "high" | "medium" | "low"}
If you find no difference, write the single word NONE to `/home/antigravity/tkgally/19c-novels/wip/country-houses-moore/audit/whole/p2015.txt`.

<transcription>
every four hours: you will see it properly administered.”

“Most assuredly, sir, but would you not like to take something? a little egg wine, and a morsel of seed cake?”

“I thank you, madam, your seed cake is always so good, and I am likely to have so long a ride, I will not refuse your kindness.”

“If Mr. Watkins had made a donble charge for his visits that day, they would have been well worth it: for he carried at least half a crown’s worth news.”

Mrs. Dalby had hardly received his instructions how to manage her baby; who had a slight fever, than she said, “What news, Mr. Watkins?”

“Why, really, ma’am, not much, except the arrival of the foreigners at the castle. I have been called to attend one of the ladies, on rather the lady’s woman, who had suffered from her voyage.”

“Do tell me,” cried the impatient lady, “who is it that all this preparation has been made for?”

“Why, ma’am, they call her the Comtesse Rosenberg: a very young, and, as I hear, a very beautiful, lady; a ward of Lord Dunster’s, and a great heiress.”

“But where does she come from?”
</transcription>
