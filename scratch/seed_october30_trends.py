"""
Seed for Oct 30, 2026: new Google Trends US topics.
- Patrick Stewart dies at 86
- Who won the World Series 2026: Brewers win first title (replaces Oct 28 Game 4 article)
- Binance hack: $6.3 billion stolen
- Bears trade for Jeffery Simmons
- Packers vs Panthers: Packers win 27-19 on Thursday Night Football
Run from the project root:  python3 scratch/seed_october30_trends.py
"""
import sqlite3
import urllib.parse

# The Oct 28 "Rays walk off Brewers / Game 5" article was never published and is now outdated.
OUTDATED_SLUGS = ["who-won-the-world-series-2026-rays-walk-off-brewers-game-4-game-5"]

ARTICLES_F = [
{
"title": "Patrick Stewart Dies at 86: Star Trek and X-Men Legend",
"slug": "patrick-stewart-dies-at-86-star-trek-picard-x-men-professor-x",
"seo_description": "Sir Patrick Stewart, Star Trek's Captain Picard and X-Men's Professor X, has died at 86 after a short illness with Alzheimer's and Lewy body dementia.",
"keywords": "Patrick Stewart, Patrick Stewart death, Sir Patrick Stewart, Patrick Stewart cause of death, Captain Picard, Star Trek The Next Generation, Professor X, Avengers Doomsday, Sunny Ozell",
"is_breaking": 1,
"image_prompt": "empty theater stage with a single spotlight and red velvet curtain, starfield projected on the backdrop",
"content": """**Sir Patrick Stewart**, the classically trained actor who became a global star as Captain Jean-Luc Picard in **Star Trek: The Next Generation** and Professor Charles Xavier in the **X-Men** films, has died. He was 86.

His representative, Kelly Bush Novak, announced on October 29, 2026, that Stewart died "in the loving care of his beloved wife Sunny" after a short illness with **Alzheimer's disease and Lewy body dementia**.

The news made "Patrick Stewart" the most-searched term in the United States, with more than 5 million searches in a single day.

## From Yorkshire to the Royal Shakespeare Company

Stewart was born on July 13, 1940, in Mirfield, West Yorkshire, England. Long before Hollywood, he built his reputation on the stage. He joined the **Royal Shakespeare Company** in 1966 and remained with it until 1982, becoming one of Britain's most respected Shakespearean actors.

That theatrical foundation stayed with him for the rest of his career. Even at the height of his screen fame, he returned to the stage again and again, appearing in productions on Broadway and in London's West End well into his later years.

## Captain Jean-Luc Picard

In 1987, Stewart took command of the USS Enterprise in **Star Trek: The Next Generation**. Over seven seasons, from 1987 to 1994, his calm, thoughtful and principled Captain Picard became one of the most beloved characters in television history. Lines like "Make it so" and "Engage" became part of pop culture.

He also played Picard in four feature films and returned to the role decades later in **Star Trek: Picard**.

## Professor X in the X-Men Films

In 2000, Stewart began a second iconic role as **Professor Charles Xavier**, the wise leader of the mutant X-Men. He appeared as the character in eight films over more than two decades, including an acclaimed, emotional performance in **Logan** (2017).

He was set to return as Xavier once more in **Avengers: Doomsday**, which is due in theaters on December 18, 2026, making it one of his final screen appearances.

## Honors and Activism

Stewart's long list of honors included:

* **Knighthood** for services to drama
* A **star on the Hollywood Walk of Fame** in 1996
* A **handprint and footprint ceremony** at the TCL Chinese Theatre in 2020

Away from acting, he was a passionate advocate on issues including domestic violence, human rights, refugees, LGBTQ+ equality, veterans' mental health and animal welfare.

## Tributes Pour In

Tributes came quickly from across Hollywood. Ian McKellen, his longtime friend and X-Men co-star, along with William Shatner and Hugh Jackman, were among the many stars who paid tribute.

Stewart is survived by his wife, singer-songwriter **Sunny Ozell**, and his two children from his first marriage, Daniel Stewart and Sophie Alexandra Stewart.

## Frequently Asked Questions

**How did Patrick Stewart die?**
His representative said he died after a short illness with Alzheimer's disease and Lewy body dementia.

**How old was Patrick Stewart?**
He was 86.

**Will Patrick Stewart appear in Avengers: Doomsday?**
Yes. He was set to return as Professor X in the film, due December 18, 2026."""
},
{
"title": "Who Won the World Series 2026? Brewers Win First Title in History",
"slug": "who-won-the-world-series-2026-brewers-win-first-title-beat-rays",
"seo_description": "Who won the World Series 2026? The Milwaukee Brewers beat the Rays 4-1 in Game 5 for their first title. William Contreras was named World Series MVP.",
"keywords": "who won the world series 2026, Brewers World Series champions, Brewers win World Series, World Series MVP William Contreras, Brewers parade, Brewers vs Rays Game 5, Jacob Misiorowski, Cooper Pratt",
"is_breaking": 1,
"image_prompt": "baseball stadium at night with fireworks and confetti over the infield, celebration atmosphere, no people",
"content": """The answer to the most-searched sports question in America is finally in: the **Milwaukee Brewers** won the **2026 World Series**. Milwaukee beat the **Tampa Bay Rays 4-1** in Game 5 on Wednesday night at Tropicana Field, winning the series 4-1 and capturing the first championship in the franchise's 57-year history.

Searches for "who won the World Series 2026" and "Brewers parade" exploded as Milwaukee celebrated.

## How the Brewers Won Game 5

After the Rays stayed alive with a 12-inning walk-off in Game 4, Milwaukee left no doubt in the clincher.

* **2nd inning:** Rookie **Cooper Pratt** singled off Rays starter Drew Rasmussen to drive in the first run.
* **5th inning:** Pratt singled again and scored on a hit by David Hamilton.
* **6th inning:** **William Contreras** lined an RBI double and Pratt added a sacrifice fly.
* **9th inning:** Closer **Trevor Megill**, who pitched the final two innings, gave up a run-scoring double to Chandler Simpson, then got Richie Palacios to ground out to Brice Turang to end the series.

On the mound, 24-year-old **Jacob Misiorowski** held the Rays scoreless into the sixth inning before leaving with a right calf cramp. He finished the World Series 2-0 with a 0.84 ERA.

## William Contreras Named World Series MVP

Catcher **William Contreras** was named **World Series MVP**. He posted an .863 OPS, threw out three would-be base stealers and won 10 of his 13 challenges under the automated ball-strike system. Milwaukee's pitchers held Tampa Bay to a .182 batting average for the series.

Other standouts set records along the way:

* **Cooper Pratt** became the first player since David Ortiz in 2013 to get a hit in six straight World Series at-bats.
* **Jackson Chourio** set a five-game World Series record with 11 hits.
* **Aaron Ashby** threw 18 consecutive scoreless innings, a single-postseason record for a reliever.

## A Historic Season

The Brewers led the majors with **103 regular-season wins** and went **11-2 in the postseason**, beating the Padres in the NLDS, sweeping the Dodgers in the NLCS and finishing off the Rays.

The franchise began as the Seattle Pilots in 1969 and moved to Milwaukee in 1970. Its only previous World Series trip came in 1982, when the Brewers lost to the St. Louis Cardinals in seven games.

"We were relentless," said manager **Pat Murphy**, the two-time reigning NL Manager of the Year, who survived a heart attack in 2020.

## Brewers World Series Parade

Milwaukee celebrated with a championship parade on **Friday, October 30**. The route began at North 4th Street and West Wisconsin Avenue and wound through downtown to **Henry Maier Festival Park**, the Summerfest grounds, where a rally was held. Several school districts, including Milwaukee Public Schools, closed for the day.

## What's Next for Baseball

The celebration comes with uncertainty. Baseball's labor agreement expires soon, and a lockout could begin as early as December 2, putting the 2027 season at risk.

## Frequently Asked Questions

**Who won the World Series 2026?**
The Milwaukee Brewers, who beat the Tampa Bay Rays four games to one.

**Who was the 2026 World Series MVP?**
Brewers catcher William Contreras.

**Is this the Brewers' first World Series title?**
Yes. It is the first championship in franchise history."""
},
{
"title": "Binance Hack: $6.3 Billion Stolen in Biggest Crypto Heist Ever",
"slug": "binance-hack-6-3-billion-stolen-biggest-crypto-heist-north-korea",
"seo_description": "Binance hack explained: about $6.3 billion in crypto was stolen in the largest heist on record. Here's what happened, who is suspected and if funds are safe.",
"keywords": "Binance hack, Binance hacked, Binance withdrawals paused, biggest crypto hack, Binance $6.3 billion, North Korea Lazarus Group, bitcoin price, Changpeng Zhao, crypto security",
"is_breaking": 1,
"image_prompt": "glowing digital padlock broken apart on a dark circuit board background, red warning light",
"content": """**Binance**, the world's largest cryptocurrency exchange, has been hit by what appears to be the **biggest crypto hack in history**. The exchange said about **$6.3 billion** was stolen in a "security incident" on Thursday, October 29, sending shockwaves through the crypto market.

"Binance hack," "bitcoin price" and "Binance" were among the top searches in the United States as users rushed to find out whether their money was safe.

## What Happened at Binance

Trouble began on Thursday when users reported funds being drained from the exchange's **hot wallets**, the internet-connected wallets used to process withdrawals. Binance founder **Changpeng Zhao**, who no longer runs the company but remains its largest shareholder, posted on X that the exchange had likely been hacked. Binance confirmed the incident hours later.

According to an initial investigation reported by Al Jazeera, the attacker made unauthorized transactions after gaining access through an engineer's **compromised laptop**.

## Who Is Behind the Binance Hack?

Blockchain intelligence firm **TRM Labs** said it assessed "with high confidence" that the attack was carried out by **TraderTraitor**, a North Korean hacking unit that investigators link to the notorious **Lazarus Group**.

If confirmed, the theft would be roughly four times larger than the previous record: the 2025 hack of the exchange Bybit, which was also blamed on North Korea and topped $1.4 billion.

## Are Binance User Funds Safe?

Binance says yes. The exchange said user funds are "safe" and that it will cover all losses. It also took several emergency steps:

* **Suspended deposits and withdrawals** while it investigated.
* **Worked with law enforcement** to trace the stolen funds.
* **Promised a detailed technical post-mortem** once the investigation is complete.

Binance also warned users to watch out for scams. Fraudsters often impersonate exchanges after major incidents, so users should only trust announcements from Binance's official website and verified accounts.

## Billions Frozen by Stablecoin Issuers

Part of the stolen money has already been locked down. Stablecoin issuer **Tether** said it froze about $1.56 billion linked to the hack, and **Circle** also froze funds as they moved through its networks. Al Jazeera reported that around $3 billion in total had been frozen.

## Bitcoin Price Reaction

The crypto market fell on the news. **Bitcoin dropped about 5%**, slipping below **$77,000**. Analysts warned that a blow to confidence in the biggest exchange could weigh on prices and push some traders toward decentralized platforms.

## What Binance Users Should Do Now

* **Don't panic-sell** based on rumors. Check Binance's official channels for updates on withdrawals.
* **Beware of phishing** emails, texts and fake support accounts.
* **Turn on two-factor authentication** and review your account security settings.
* **Consider self-custody** for long-term holdings.

## Frequently Asked Questions

**How much was stolen in the Binance hack?**
Binance said about $6.3 billion, which would make it the largest crypto theft on record.

**Who hacked Binance?**
TRM Labs believes North Korea's TraderTraitor unit, linked to the Lazarus Group, was responsible.

**Will Binance users get their money back?**
Binance says user funds are safe and that it will cover all losses."""
},
{
"title": "Bears Trade for Jeffery Simmons: Two First-Round Picks to Titans",
"slug": "bears-trade-jeffery-simmons-titans-two-first-round-picks",
"seo_description": "The Bears acquired All-Pro DT Jeffery Simmons from the Titans for 2027 and 2028 first-round picks. Here are the full trade terms, contract and impact.",
"keywords": "Jeffery Simmons, Jeffery Simmons trade, Bears trade, Jeffery Simmons Bears, Titans trade, Jeffery Simmons contract, Ryan Poles, NFL trade deadline 2026, Bears defense",
"image_prompt": "american football on a frosty field at a lakefront stadium at dusk, cold blue light, empty stands",
"content": """The **Chicago Bears** have made their boldest move in years. On Thursday, Chicago acquired All-Pro defensive tackle **Jeffery Simmons** from the **Tennessee Titans** in a blockbuster deal that costs the Bears two first-round picks.

"Jeffery Simmons" and "Jeffery Simmons trade" shot up Google Trends, with more than 200,000 searches as the news broke.

## Jeffery Simmons Trade Details

* **Bears receive:** DT Jeffery Simmons and a 2028 fifth-round pick
* **Titans receive:** A 2027 first-round pick, a 2028 first-round pick and a 2027 fourth-round pick

With the deal, Bears general manager **Ryan Poles** became the first GM to trade two first-round picks for a defensive tackle. It is Chicago's biggest trade since the 2018 deal for Khalil Mack.

Titans GM Mike Borgonzi, who once worked alongside Poles in the Kansas City Chiefs' front office, accepted the offer on Thursday morning after consulting coach Robert Saleh and owner Amy Adams Strunk.

"There are few people like Jeff Simmons," Strunk said, praising his impact on and off the field.

## Who Is Jeffery Simmons?

Simmons, 29, is one of the NFL's most disruptive interior defenders:

* **Four-time Pro Bowler** and first-team All-Pro in 2025
* **46.5 career sacks** in eight seasons, including a career-high 11 last year
* **28 pressures** entering Week 8, the most among defensive tackles according to Next Gen Stats

At 6-foot-4 and 305 pounds, he has played 87% of Tennessee's defensive snaps this season.

## Jeffery Simmons Contract

In June, the Titans signed Simmons to a three-year, $105.8 million extension that included $100 million guaranteed. Tennessee already paid $20 million of his signing bonus, and the Bears owe him about $7.9 million for the rest of this season. His cap hits rise to $22.5 million in 2027, $30.9 million in 2028 and $29.1 million in 2029.

## Why the Bears Made the Move

At 5-2, Chicago is in the thick of the NFC race despite starting three different quarterbacks this season. The pass rush, however, needed help. Edge rusher Montez Sweat is suspended and Dayo Odeyingbo is on injured reserve.

Simmons will line up next to Grady Jarrett, giving the Bears one of the league's most dangerous interior duos. The risk is real, though: without first-round picks in 2027 and 2028, Chicago will have fewer chances to add young defensive ends or cornerbacks through the draft.

## The Titans Start Over

For Tennessee, which is 1-6, the trade is a clear signal of a rebuild. The Titans now hold extra first-round picks to build around, giving the front office more flexibility to reshape the roster in the next two drafts.

## What's Next

Simmons could make his Bears debut on **Monday Night Football** against the defending Super Bowl champion **Seattle Seahawks**. The NFL trade deadline is Tuesday, November 10.

## Frequently Asked Questions

**What did the Bears give up for Jeffery Simmons?**
2027 and 2028 first-round picks and a 2027 fourth-round pick. Chicago also gets back a 2028 fifth-round pick.

**How old is Jeffery Simmons?**
He is 29.

**How much is Jeffery Simmons' contract?**
Three years and $105.8 million, with $100 million guaranteed."""
},
{
"title": "Packers vs Panthers: Jordan Love Throws 3 TDs in 27-19 Win",
"slug": "packers-vs-panthers-jordan-love-3-touchdowns-27-19-thursday-night-football",
"seo_description": "Packers vs Panthers recap: Jordan Love threw three touchdowns as Green Bay held on to beat Carolina 27-19 on Thursday Night Football at Lambeau Field.",
"keywords": "Packers vs Panthers, Panthers vs Packers, Packers score, Thursday Night Football, Jordan Love, Christian Watson injury, Bryce Young, Josh Jacobs, Packers 5-3",
"image_prompt": "snowy football stadium at night under bright lights, green and gold atmosphere, empty field",
"content": """The **Green Bay Packers** built a big lead and then held on. Jordan Love threw three touchdown passes as Green Bay beat the **Carolina Panthers 27-19** on **Thursday Night Football** at Lambeau Field.

"Packers vs Panthers" was among the most-searched terms in the U.S., with more than 500,000 searches as fans followed the game and a scary injury to Christian Watson.

## Packers vs Panthers Final Score

* **Final:** Packers 27, Panthers 19
* **Halftime:** Packers 20, Panthers 10
* **Records:** Green Bay improves to 5-3; Carolina falls to 3-4

The Packers led 27-10 midway through the third quarter before the Panthers rallied. Carolina outgained Green Bay 109-32 in the fourth quarter, but the comeback came up short.

## Jordan Love Leads the Way

**Jordan Love** completed 30 of 41 passes for 288 yards with three touchdowns and one interception. His scoring throws went to:

* **Tucker Kraft:** 12 yards
* **Matthew Golden:** 24 yards
* **Josh Jacobs:** 4 yards

Jacobs also ran in a 1-yard touchdown. He was held to 39 yards on 21 carries, but he scored twice.

## Christian Watson Injury Update

The night's scariest moment came with 9:11 left in the first half, when receiver **Christian Watson** left the field in an ambulance with a **chest injury**. Doctors examined him at a local hospital and cleared him, and he returned to Lambeau Field and back into the game.

Watson finished with 8 catches for 113 yards. His 7-yard catch on third-and-2 with 2:33 left sealed the win by letting Green Bay run out the clock. He did lose a fumble in the first half.

## Panthers Fall Short

Carolina quarterback **Bryce Young** went 23 of 41 for 209 yards with one touchdown and one interception, and he was sacked six times. Running back **Chuba Hubbard** led the Panthers with 81 rushing yards and a touchdown, while rookie receiver Tetairoa McMillan caught six passes for 58 yards.

Carolina's best chance ended with 2:41 left, when Young threw incomplete on fourth-and-5 near midfield. Kicker Ryan Fitzgerald added field goals of 39 and 50 yards for the Panthers, who finished with 258 total yards to Green Bay's 354.

## Mistakes on Both Sides

The game was far from clean:

* Carolina's Coleman Owen fumbled the opening kickoff.
* Green Bay kicker Trey Smack missed an extra point, adding to a rough stretch for the rookie.

## What It Means

The win keeps Green Bay in the hunt in a crowded **NFC North**, and the defense finished strong, with rookie Dani Dennis-Sutton recording a sack with four seconds left. Carolina, meanwhile, drops below .500 and must find answers on its offensive line after allowing six sacks and nine quarterback hits. The Panthers showed fight late, but early turnovers and a slow start were too much to overcome on the road.

## Frequently Asked Questions

**Who won Packers vs Panthers?**
The Packers won 27-19 on Thursday Night Football.

**Is Christian Watson OK?**
He was taken to a hospital with a chest injury but was cleared and returned to the game.

**What is the Packers' record?**
Green Bay is 5-3 after the win."""
},
]


def image_url(prompt, seed):
    full = prompt + ", ultra realistic, 4k, editorial photography, dramatic lighting, no text, no faces, no logos"
    return f"https://image.pollinations.ai/prompt/{urllib.parse.quote(full)}?width=1200&height=675&seed={seed}&nologo=true"


def seed_database():
    conn = sqlite3.connect("news.db")
    cur = conn.cursor()
    for slug in OUTDATED_SLUGS:
        cur.execute("DELETE FROM news_articles WHERE slug = ?", (slug,))
        if cur.rowcount:
            print("removed outdated", slug)
    published = "2026-10-30 19:30:00"  # UTC (22:30 Istanbul)
    for i, a in enumerate(ARTICLES_F):
        wc = len(a["content"].split())
        assert 500 <= wc <= 600, f"{a['slug']}: {wc} words"
        img = image_url(a["image_prompt"], 266000 + i)
        cur.execute("SELECT id FROM news_articles WHERE slug = ?", (a["slug"],))
        row = cur.fetchone()
        if row:
            cur.execute("""UPDATE news_articles SET title=?, content=?, seo_description=?, keywords=?, image_url=?
                           WHERE id=?""", (a["title"], a["content"], a["seo_description"], a["keywords"], img, row[0]))
            print("updated", a["slug"])
        else:
            cur.execute("""INSERT INTO news_articles (title, slug, content, original_url, seo_description, keywords,
                           is_bizarre, is_breaking, published_at, created_at, image_url)
                           VALUES (?, ?, ?, ?, ?, ?, 0, ?, ?, ?, ?)""",
                        (a["title"], a["slug"], a["content"], f"https://trends.google.com/trending?geo=US#{a['slug']}",
                         a["seo_description"], a["keywords"], a.get("is_breaking", 0), published, published, img))
            print("inserted", wc, "words", a["slug"])

    conn.commit()
    conn.close()


if __name__ == "__main__":
    seed_database()
