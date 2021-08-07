# Hacker News Scraper

This python project tracks the latest news from <a href="https://news.ycombinator.com/">Hacker News</a> and emails you top ranked news (with votes >= 100) every day.

The email looks like this:

### Hacker Daily News

Find the latest breaking news here:

1: Apple's plan to “think different” about encryption opens a backdoor to your life, https://www.eff.org/deeplinks/2021/08/apples-plan-think-different-about-encryption-opens-backdoor-your-private-life, 2168\
2: CalyxOS – De-Googled Android Alternative, https://calyxos.org/, 757\
3: Mozilla Common Voice Adds 16 New Languages and 4,600 New Hours of Speech, https://foundation.mozilla.org/en/blog/mozilla-common-voice-adds-16-new-languages-and-4600-new-hours-of-speech/, 700\
4: The Problem with Perceptual Hashes, https://rentafounder.com/the-problem-with-perceptual-hashes/, 479\
5: New UUID Formats – IETF Draft, https://datatracker.ietf.org/doc/html/draft-peabody-dispatch-new-uuid-format, 451\
6: Surveys show Americans want more walkable cities, https://www.governing.com/community/vehicles-still-firmly-in-control-of-city-streets, 393\
7: Reflections on 10k Hours of Programming, https://matt-rickard.com/reflections-on-10-000-hours-of-programming/, 365\
8: LÖVR – An open source framework for rapidly building immersive 3D experiences, https://lovr.org, 364\
9: Launch HN: BlackOakTV (YC S21) – Netflix for black people, item?id=28087309, 353\
10: Apple’s new abuse prevention system: an antritust/competition point of view, https://blog.quintarelli.it/2021/08/apples-child-new-abuse-prevention-system-an-antritustcompetition-point-of-view.html, 323\
11: Dating in Delhi when you're poor, https://www.reuters.com/article/delhi-dating-idUSKBN1DU0NE, 316\
12: An open letter against Apple's new privacy-invasive client-side content scanning, https://github.com/nadimkobeissi/appleprivacyletter, 303\
13: In internal memo, Apple addresses concerns around new Photo scanning features, https://9to5mac.com/2021/08/06/apple-internal-memo-icloud-photo-scanning-concerns/, 300\
14: Swiss Ph.D student’s dismissal spotlights China’s influence, https://www.nzz.ch/english/swiss-phd-students-dismissal-spotlights-chinas-influence-ld.1638771, 272\
15: “People have asked if we'll adopt this system for WhatsApp. The answer is no.”, https://twitter.com/wcathcart/status/1423701473624395784, 258\
16: Atlantic Ocean currents weaken, signalling big weather changes: study, https://www.reuters.com/business/environment/atlantic-ocean-currents-weaken-signalling-big-weather-changes-study-2021-08-05/, 240\
17: Whistleblowers expose corruption in EPA Chemical Safety Office, https://theintercept.com/2021/07/02/epa-chemical-safety-corruption-whistleblowers/, 224\
18: A cocktail of pesticides, parasites and hunger leaves bees down and out, https://www.nature.com/articles/d41586-021-02079-4, 215\
19: Show HN: Open-source A/B testing framework, https://github.com/growthbook/growthbook, 181\
20: Learning APL, https://xpqz.github.io/learnapl/intro.html, 165\
21: Looking into Zig, https://ayende.com/blog/194404-A/looking-into-zig, 160\
22: The CIA’s outsourced torture is lost to history, https://foreverwars.substack.com/p/the-cias-outsourced-torture-is-lost, 156\
23: The Drunken Bishop Algorithm, https://www.jfurness.uk/the-drunken-bishop-algorithm/, 154\
24: Fooling Neural Networks [pdf], https://slazebni.cs.illinois.edu/fall18/lec12_adversarial.pdf, 142\
25: The Emacs Lock-In Effect or the Emacs Sunk Cost Fallacy, https://karl-voit.at/2021/07/23/emacs-lock-in/, 138\
26: Launch YC S21: Meet the Batch, Thread #4, item?id=28073548, 123\
27: Bones hoarded by hyenas over thousands of years, https://www.smithsonianmag.com/smart-news/archaeologists-uncover-extensive-pile-animal-and-human-bones-saudi-arabia-cave-180978375/, 116\
28: Driving 1725km in an electric car in 2 days, https://www.tbray.org/ongoing/When/202x/2021/08/05/Western-Electric, 104\
29: Richard Stallman and the History of Free Software and Open Source (2016), https://www.cmpod.net/all-transcripts/history-open-source-free-software-text/, 100
