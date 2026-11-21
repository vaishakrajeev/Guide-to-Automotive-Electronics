# Updating the Latest News chapter

The page (`latest-news.html`) gets all of its content from `news/news.json`. An update only changes that JSON file.

## Source
Gmail, from `googlealerts-noreply@google.com`. There are two daily alerts: **automotive electronics** and **automotive technology**. Read every alert received since the `updated` date in `news.json`.

## Rules for each run
1. **Unwrap links.** Google Alert links look like `https://www.google.com/url?...&url=<REAL>&ct=ga...`. Store only the decoded `<REAL>` URL, with tracking params such as `?next=1` removed.
2. **Filter for relevance.** Keep stories about vehicle electronics, ECUs, sensors, semiconductors, power electronics, SDV/software, connectivity, cybersecurity, EV/hybrid powertrains, standards, and major supplier moves. Drop the following:
   - stock-quote pages
   - used-car buying advice
   - general manufacturing or robotics stories with no electronics angle
   - student or event fluff
   - recycled articles (an ET Auto ID far lower than current ones usually means an old story)
3. **Deduplicate.** If several outlets cover the same event, keep the most original or technical source.
4. **Summarise in your own words.** Write one or two sentences per item. Never paste the alert snippet. Mark promotional market reports as such.
   Add a `keywords` array of 3–5 short technical terms for each item (for example "Camera modules", "ADAS", "ECU"). Use title case and include company names only when they are central to the story.
5. **Group into trends.** Add each item to an existing trend when it fits. Create a new trend (`id`, `chip`, `title`, `summary`) when at least two items share a new theme. Refresh a trend's `summary` when the new items change what it says.
6. **Trim.** Keep about the last 30 days. Drop items older than that, and drop any trend left with no items. Aim for 4–6 trends and at most 8 items per trend.
7. Set `updated` to today's date (Asia/Kolkata). Make sure the file is valid JSON, then commit with the message `news: update YYYY-MM-DD`.

## Audio scripts (about 3 minutes each)
Each item also needs a `script` field: a spoken overview of 400–450 words (about 3 minutes). Structure it like this:
1. About 80–100 words on what happened. Use only facts from the source article: fetch it, and if it can't be fetched, use only the alert snippet. Never invent figures, names or dates.
2. About 250–300 words of technical background, explaining the technology behind the story (how it works and the standards involved) for engineers and students.
3. One or two sentences on why it matters or what to study next. End with "The full report from <source> is linked on this page."
Write for the ear: short sentences, no bullet points, symbols or URLs. Write numbers in words where they would be misread (for example "eight hundred volt"), and spell acronyms with spaces ("E C U", "I S O twenty six two six two"). Write the script in your own words and never paraphrase the article closely.

## Audio overviews
Each item's `audio` field points to an MP3 in `news/audio/`. The GitHub Action `.github/workflows/news-audio.yml` generates these with Piper TTS (voice `en_GB-northern_english_male-medium`, natural pitch) after every change to `news.json`. Never add, edit or remove `audio`/`audio_sec` fields or MP3 files by hand: keep the existing fields as they are, and leave them out of new items. The Action fills them in.
