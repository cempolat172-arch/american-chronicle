"""
Seed for Oct 27, 2026 (morning): new Google Trends US topics.
- Alexia Putellas wins 2026 Ballon d'Or Feminin (trend: "alexia putellas", 200K+)
- Texas Roadhouse steak complaint / Kenneth Card (200K+)
- AT&T data breach settlement payout (50K+)
Run from the project root:  python3 scratch/seed_october27_trends.py
"""
import sqlite3
import urllib.parse

ARTICLES_C = [
{
"title": "Alexia Putellas Wins 2026 Ballon d'Or Féminin, Her Third Title",
"slug": "alexia-putellas-wins-2026-ballon-dor-feminin-third-title",
"seo_description": "Alexia Putellas wins the 2026 Ballon d'Or Féminin in London, her third title, completing a comeback from a torn ACL after leading Barcelona to a quadruple.",
"keywords": "Alexia Putellas, Ballon d'Or Féminin 2026, who won the Ballon d'Or 2026, quién ganó el Balón de Oro 2026, women's Ballon d'Or, Barcelona Femení, Putellas ACL comeback, London City Lionesses",
"image_prompt": "golden football trophy on a dark theater stage under a single spotlight, red curtain",
"content": """**Alexia Putellas** has won the **2026 Ballon d'Or Féminin**, completing one of the most remarkable comebacks in modern soccer. The Barcelona captain collected the award on Monday night at the London Palladium, the first Ballon d'Or ceremony ever held outside Paris, on the same night England's Harry Kane won the men's prize.

The win sent searches for "Alexia Putellas" and "who won the Ballon d'Or 2026" climbing across the United States, including the Spanish-language query "quién ganó el Balón de Oro 2026."

## A Third Ballon d'Or for Putellas

This is the third Ballon d'Or of Putellas' career, after back-to-back wins in 2021 and 2022. It ties her with Spain and Barcelona teammate **Aitana Bonmatí** for the most women's Ballon d'Or titles in history.

Bonmatí, who won the award three years in a row after Putellas' last victory, was not eligible this year after missing close to six months of last season through injury.

The award has been dominated by a very small group. Since 2019, only three players have won it: Putellas, Bonmatí and the United States' Megan Rapinoe, who took the 2019 prize. Putellas' latest win came four years after her last.

## The Comeback From a Torn ACL

Putellas' road back began with a devastating setback. She tore her anterior cruciate ligament on the eve of the 2022 European Championship in England, missed most of the following season with Barcelona and played only a peripheral role as Spain won the 2023 World Cup.

"My first goal after the injury was to compete again at the highest level," Putellas said. She has described how the injury changed her mentality, saying she now tries to enjoy everything "as it was the last."

## A Quadruple-Winning Season With Barcelona

The voting period covered the 2025-26 season, and Putellas delivered on every front as captain of **Barcelona**:

* **Quadruple:** Barcelona won four trophies, including a seventh straight Liga F title.
* **Champions League:** Barcelona beat OL Lyonnes 4-0 in the final in Oslo, the club's third European title in four seasons.
* **Liga F:** 9 goals and 7 assists.
* **Champions League:** 8 goals and 6 assists.

She also remains a central figure for Spain, currently ranked first in the FIFA world rankings.

## Strong Competition for the Award

Putellas beat a strong field. Manchester City striker **Khadija Shaw** made a powerful case after scoring 21 league goals as City won the league title and the FA Cup, while Barcelona midfielder **Patri Guijarro** also drew strong support.

## What's Next for Alexia Putellas

At 32, Putellas has started a new chapter. With her Barcelona contract at an end, she has signed with **London City Lionesses** in England, a club owned by Michele Kang, who also owns OL Lyonnes.

## Frequently Asked Questions

**Who won the 2026 Ballon d'Or Féminin?**
Alexia Putellas won the award on October 26, 2026, at the London Palladium.

**How many Ballon d'Or awards has Alexia Putellas won?**
Three: in 2021, 2022 and 2026, tying Aitana Bonmatí's record.

**Who won the men's Ballon d'Or 2026?**
England captain Harry Kane won the men's award at the same ceremony."""
},
{
"title": "Texas Roadhouse Steak Complaint: Man Says He Got Sirloin, Not Filet",
"slug": "texas-roadhouse-steak-complaint-kenneth-card-sirloin-instead-of-filet",
"seo_description": "Texas Roadhouse steak complaint goes viral: Kenneth Card says he was served a $19 sirloin instead of a $30 filet three times. Here's how the chain responded.",
"keywords": "Texas Roadhouse steak complaint, Kenneth Card, Texas Roadhouse filet mignon, Texas Roadhouse sirloin, Texas Roadhouse Forsyth Illinois, Texas Roadhouse TikTok, Dallas Filet price",
"image_prompt": "two raw steaks side by side on a wooden butcher board in a restaurant kitchen, warm light",
"content": """A **Texas Roadhouse steak complaint** has become one of the most-searched food stories in the country. Illinois diner **Kenneth Card** says the restaurant served him a cheaper sirloin instead of the filet he ordered, not once but three times, and his video about it has sent the chain's name trending on Google.

## What Happened at Texas Roadhouse

Card was a regular at the **Texas Roadhouse in Forsyth, Illinois**, visiting about once a week for more than a year and getting to know the staff. On three separate visits, he says, he ordered the eight-ounce **Dallas Filet** and was instead served an eight-ounce **sirloin**.

According to reporting on the incident, the two steaks are priced very differently:

* **Dallas Filet (8 oz):** about $29.99
* **Sirloin (8 oz):** about $19.49
* **Difference:** roughly $10.50 per meal

## How He Says He Knew

Card says his past work in hotel and restaurant kitchens, where he prepared and cut steaks, taught him to tell the two cuts apart. He described the filet as melt-in-your-mouth tender, and the sirloin he received as grittier and chewier.

Here is how he describes the three visits:

* **First visit:** He told staff he believed he had the wrong steak, and they brought him a filet.
* **Second visit:** He ate the steak without complaining, assuming it was another honest mix-up.
* **Third visit:** He asked to speak with a manager. The restaurant took the steak back to check it, and staff told him it was not what he had ordered.

Card waited for a replacement, asked for it to go and posted a warning on TikTok in early October. The video has drawn more than 30,000 views.

## Texas Roadhouse Responds

Texas Roadhouse has confirmed that a mix-up happened, but not that it happened three times. A company spokesperson said the chain had "not been able to track that this occurred on three occasions," but confirmed one incident at the Forsyth location, which management corrected on site by serving a filet.

The spokesperson said management "quickly made it right," and that team members double-check food for quality and accuracy before it leaves the kitchen. The company encouraged any customer who receives the wrong steak, or is overcharged, to tell their server right away.

## Why the Story Struck a Nerve

The video has split viewers. Some commenters believe the problem was specific to one location, while others admitted they would not be able to tell a filet from a sirloin. Card's claims about the second and third visits have not been independently confirmed.

For his part, Card says he is finished with that restaurant. "I think I'm done going in there," he said.

## Frequently Asked Questions

**What is the Texas Roadhouse steak complaint about?**
Customer Kenneth Card says he ordered a filet but was served a cheaper sirloin on three visits to the Forsyth, Illinois, location.

**Did Texas Roadhouse respond?**
Yes. The chain confirmed one mix-up, which it says was corrected on site, but said it could not verify that it happened three times.

**What should you do if you get the wrong steak?**
Texas Roadhouse says customers should tell their server immediately so the order can be fixed."""
},
{
"title": "AT&T Data Breach Settlement Payout: When Checks Could Arrive",
"slug": "att-data-breach-settlement-payout-date-when-checks-arrive-2026",
"seo_description": "AT&T data breach settlement payout update: the $177M deal won final approval Oct. 2. Payments could start in December 2026 if no appeal is filed.",
"keywords": "AT&T data breach settlement, AT&T settlement payout date, AT&T settlement December payout, AT&T settlement check amount, telecomdatasettlement.com, AT&T settlement appeal, AT&T 2024 data breach",
"image_prompt": "stack of envelopes and a smartphone on an office desk with soft daylight, shallow depth of field",
"content": """Millions of customers are asking the same question: when will the **AT&T data breach settlement** pay out? The $177 million settlement received final court approval on October 2, 2026, and payments could begin as early as **December 2026**, but only if no one appeals.

Here is what is confirmed, what is still uncertain, and how much claimants can expect.

## What the AT&T Settlement Covers

The settlement resolves claims over two separate data breaches:

* **AT&T 1 ($149 million):** Data on about 73 million current and former customers, including names, addresses, dates of birth and, for many people, Social Security numbers, surfaced on the dark web in March 2024.
* **AT&T 2 ($28 million):** In April 2024, an attacker accessed AT&T's third-party Snowflake cloud workspace and took call and text records for about 110 million customers. The content of calls was not taken.

AT&T denies wrongdoing. Senior U.S. District Judge **Sidney A. Fitzwater** of the Northern District of Texas granted final approval.

## AT&T Settlement Payout Date

No official payout date has been announced. The timeline depends on appeals:

* **Appeal deadline:** About November 2, 2026.
* **If there is no appeal:** The settlement's Effective Date would fall around mid-November. The settlement administrator has 60 days from that date to pay claimants, which means checks could start arriving in late December 2026, with most expected by mid-January 2027.
* **If there is an appeal:** Payments would be paused until the U.S. Court of Appeals for the Fifth Circuit rules, which can take many months or more than a year.

Around 45 objectors opposed the settlement, so an appeal remains possible. A court status conference is scheduled for November 20, 2026.

## How Much Will You Get?

Most claimants will receive a modest cash payment. Estimates from the settlement administrator are:

* **AT&T 1, Social Security number exposed:** about $39-$40
* **AT&T 1, no SSN exposed:** about $7.50-$8.10
* **AT&T 2 account owners:** about $6.50-$7.10

Claimants who documented actual losses could receive up to **$5,000** under AT&T 1 and up to **$2,500** under AT&T 2, for a combined maximum of $7,500, instead of a flat payment. Payments can be sent electronically or by paper check.

## Can You Still File a Claim?

No. The deadline to file a claim was December 18, 2025, and the opt-out and objection window closed in November 2025.

## How to Avoid Settlement Scams

The official settlement website is **telecomdatasettlement.com**, run by Kroll Settlement Administration, and its phone line is (833) 890-4930. Legitimate emails come from attsettlement@e.emailksa.com. No one should ask you for an upfront payment or card details to release your money, and it is safest to type the website address yourself rather than clicking email links.

## Frequently Asked Questions

**When will AT&T settlement checks be sent?**
No official date exists. If no appeal is filed by early November, payments could begin in late December 2026 and finish by mid-January 2027.

**How much is the AT&T settlement payout?**
Most people will get about $6.50 to $40. Documented losses can be reimbursed up to $7,500.

**Is it too late to file a claim?**
Yes. The claim deadline was December 18, 2025."""
},
]


def image_url(prompt, seed):
    full = prompt + ", ultra realistic, 4k, editorial photography, dramatic lighting, no text, no faces, no logos"
    return f"https://image.pollinations.ai/prompt/{urllib.parse.quote(full)}?width=1200&height=675&seed={seed}&nologo=true"


def seed_database():
    conn = sqlite3.connect("news.db")
    cur = conn.cursor()
    published = "2026-10-27 08:30:00"  # UTC (11:30 Istanbul)
    for i, a in enumerate(ARTICLES_C):
        wc = len(a["content"].split())
        assert 500 <= wc <= 600, f"{a['slug']}: {wc} words"
        img = image_url(a["image_prompt"], 263000 + i)
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
