"""
Seed for Oct 26, 2026 (afternoon): new Google Trends US topics.
- Eric Bauza dies at 46 (trend: "eric bauza", 200K+)
- Undefeated NFL teams 2026 (trends: "undefeated nfl teams", "trey smack", "nfc north standings")
- Adds trending query "la liga standings" to the El Clasico article keywords.
Run from the project root:  python3 scratch/seed_october26b_trends.py
On deploy, app/db_sync.py copies new/changed bundled articles into Supabase.
"""
import sqlite3
import urllib.parse

ARTICLES_B = [
{
"title": "Eric Bauza Dies at 46: Voice of Bugs Bunny and Daffy Duck",
"slug": "eric-bauza-dies-at-46-voice-of-bugs-bunny-daffy-duck-looney-tunes",
"seo_description": "Eric Bauza, the Emmy-winning voice of Bugs Bunny and Daffy Duck in today's Looney Tunes, has died at 46. A look at his life, career and legacy.",
"keywords": "Eric Bauza, Eric Bauza death, Bugs Bunny voice actor, Looney Tunes voice actor, Daffy Duck voice, Eric Bauza cause of death, Looney Tunes Cartoons, Mel Blanc successor",
"is_breaking": 1,
"image_prompt": "empty vintage recording studio microphone under a warm spotlight, soft dust in the air",
"content": """**Eric Bauza**, the voice actor who gave Bugs Bunny and Daffy Duck their voices for a new generation of Looney Tunes fans, has died. He was 46. His family announced the news on his Instagram account on Sunday night, writing that he "has passed away suddenly."

Bauza died at a home in Los Angeles County on Sunday, October 25, 2026. The Los Angeles County Medical Examiner listed the cause of death as hypertensive cardiovascular disease and the manner of death as natural.

The news sent searches for "Eric Bauza" and "Bugs Bunny voice actor" climbing across the United States on Monday, as fans looked back on a career that reached millions of children and families.

## A Shock to the Animation World

His manager, **Judy Coppage**, described Bauza as a "unique and versatile voice actor" and said his sudden passing was "a shock to all of us." The family said more details would be shared later.

## The Modern Voice of Looney Tunes

Bauza joined the Looney Tunes franchise in 2011, first voicing **Marvin the Martian**. Over the following years he took on many of the franchise's most famous characters, eventually becoming the modern voice of both **Bugs Bunny** and **Daffy Duck**.

His Looney Tunes characters included:

* **Bugs Bunny** and **Daffy Duck**
* **Porky Pig** and **Tweety**
* **Elmer Fudd** and **Marvin the Martian**
* **Foghorn Leghorn**, **Sylvester** and **Speedy Gonzales**

He was widely seen as a modern successor to **Mel Blanc**, the legendary performer who originated many of those voices. Bauza voiced the characters in the series **Looney Tunes Cartoons** (2020-2024), voiced Daffy Duck in **Space Jam: A New Legacy** (2021), and played Bugs, Daffy and Marvin in the video game **MultiVersus**.

One of his final performances came in **Coyote vs. Acme**, the long-shelved Looney Tunes film that was finally released this year, in which he had about a dozen credits.

## Emmy Awards and Other Roles

Bauza won three Children's and Family Emmy Awards in a row:

* **2022** for Looney Tunes Cartoons
* **2023** for Bugs Bunny Builders
* **2024** for Teen Titans Go!

Beyond Looney Tunes, his voice appeared in a long list of shows, including Puss in Boots in **The Adventures of Puss in Boots**, Baby Fozzie in **Muppet Babies**, Buster Bunny in **Tiny Toons Looniversity**, and characters in **Invincible** and **Bob's Burgers**.

## From Toronto to Hollywood

Bauza was born on December 7, 1979, in Scarborough, Ontario, a suburb of Toronto, and was of Filipino descent. He began his career around 2000, interning at the animation studio Spümcø while still in college, and landed his first voice role on **The Ripping Friends**.

Over more than two decades, he became one of the most recognizable voices in animation, even if most audiences never saw his face.

## Frequently Asked Questions

**How did Eric Bauza die?**
The Los Angeles County Medical Examiner listed the cause as hypertensive cardiovascular disease, and the manner of death as natural.

**How old was Eric Bauza?**
He was 46 years old.

**Which Looney Tunes characters did Eric Bauza voice?**
He voiced Bugs Bunny, Daffy Duck, Porky Pig, Tweety, Elmer Fudd, Marvin the Martian and several others."""
},
{
"title": "Undefeated NFL Teams 2026: Vikings Are the Last Unbeaten Team",
"slug": "undefeated-nfl-teams-2026-vikings-last-unbeaten-team-week-7",
"seo_description": "Undefeated NFL teams 2026: after the Chiefs and 49ers lost in Week 7, the 6-0 Minnesota Vikings are the league's only unbeaten team. Here's what's next.",
"keywords": "undefeated NFL teams, Vikings undefeated, Vikings 6-0, NFL standings Week 7, NFC North standings, Chiefs first loss, 49ers lose to Falcons, Trey Smack",
"is_breaking": 0,
"image_prompt": "american football resting on a frosty stadium field at dusk, purple sky, empty stands",
"content": """After a chaotic Week 7, the list of **undefeated NFL teams** is down to one. The **Minnesota Vikings** are the last unbeaten team in the league at 6-0, after both the Kansas City Chiefs and the San Francisco 49ers suffered their first losses of the 2026 season on Sunday.

Searches for "undefeated NFL teams" and "NFL standings" spiked overnight as fans tried to keep up with a weekend that reshaped the playoff picture.

## How the Vikings Stayed Perfect

Minnesota did not make it easy. The Vikings came from behind to beat the **Indianapolis Colts 16-10** at home, leaning on a defense that held Indianapolis to just 218 total yards. The offense managed only 275 yards, but kicker **Will Reichard** has yet to miss a kick this season.

The win extends Minnesota's streak to 11 straight victories, dating back to last season.

Coach **Kevin O'Connell** said it is still early enough in the season that his team is "catching our stride," and that it will keep improving.

## Chiefs and 49ers Fall From the Unbeaten Ranks

Two contenders lost their perfect records on the same day:

* **Kansas City Chiefs (5-1):** Lost 20-3 at Seattle on Sunday Night Football. Patrick Mahomes failed to get the Chiefs into the red zone, a first in his career.
* **San Francisco 49ers (6-1):** Lost 29-20 at Atlanta after leading 14-3. The Falcons forced four turnovers, including two Brock Purdy interceptions, while San Francisco played without its top five receivers.

"It starts with me at quarterback," Purdy said after the loss.

## Lions Edge Packers as Trey Smack Struggles

The **Detroit Lions** beat the **Green Bay Packers 20-17** on a field goal as time expired. Green Bay rookie kicker **Trey Smack** missed two field goals in the loss, which sent his name trending on Google.

The result adds intrigue to the **NFC North standings**. For the first time in NFL history, two divisions will enter Week 8 with all four teams above .500, and the NFC North is one of them.

## Around the League

Elsewhere, the **Denver Broncos** (5-2) beat Arizona 30-16 to take the lead in the AFC West, helped by a 62-yard touchdown run from Bo Nix. The **Cleveland Browns** (5-2) moved back to the top of the AFC North with a 27-24 win at Tennessee.

## The Last Winless Team

At the other end of the table, the **Los Angeles Chargers** are now the only winless team after the Miami Dolphins beat the New York Jets 28-25.

## What's Next for the Vikings

Minnesota's perfect season faces a tough test right away. The upcoming schedule includes:

* At the **Detroit Lions** (4-2)
* Home against the **Buffalo Bills** (5-1)
* At the **Green Bay Packers**, followed by a trip to **San Francisco**

With three division rivals above .500, staying unbeaten will not be simple.

## Frequently Asked Questions

**Which NFL teams are still undefeated?**
Only the Minnesota Vikings, who are 6-0 after Week 7 of the 2026 season.

**Who did the Vikings beat in Week 7?**
They rallied to beat the Indianapolis Colts 16-10.

**Who is the last winless NFL team?**
The Los Angeles Chargers, after the Dolphins beat the Jets."""
},
]


def image_url(prompt, seed):
    full = prompt + ", ultra realistic, 4k, editorial photography, dramatic lighting, no text, no faces, no logos"
    return f"https://image.pollinations.ai/prompt/{urllib.parse.quote(full)}?width=800&height=500&seed={seed}&nologo=true"


def seed_database():
    conn = sqlite3.connect("news.db")
    cur = conn.cursor()
    published = "2026-10-26 14:15:00"  # UTC (17:15 Istanbul)
    for i, a in enumerate(ARTICLES_B):
        wc = len(a["content"].split())
        assert 500 <= wc <= 600, f"{a['slug']}: {wc} words"
        img = image_url(a["image_prompt"], 262000 + i)
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
                         a["seo_description"], a["keywords"], a["is_breaking"], published, published, img))
            print("inserted", wc, "words", a["slug"])

    cur.execute("""UPDATE news_articles SET keywords = keywords || ', la liga standings'
                   WHERE slug LIKE 'el-clasico-2026-mbappe%' AND keywords NOT LIKE '%la liga standings%'""")
    conn.commit()
    conn.close()


if __name__ == "__main__":
    seed_database()
