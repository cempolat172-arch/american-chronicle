"""
Seed for Oct 28, 2026: new Google Trends US topics.
- Susan Saint James dies at 80
- Colts trade Quenton Nelson and DeForest Buckner
- Miyoko's plant butter recall (FDA Class II)
- McDonald's holiday menu 2026 (cookie butter drinks, McRib)
Run from the project root:  python3 scratch/seed_october28_trends.py
"""
import sqlite3
import urllib.parse

ARTICLES_E = [
{
"title": "Susan Saint James Dies at 80: 'Kate & Allie' and 'McMillan & Wife' Star",
"slug": "susan-saint-james-dies-at-80-kate-and-allie-mcmillan-and-wife-star",
"seo_description": "Susan Saint James, the Emmy-winning star of McMillan & Wife and Kate & Allie and wife of Dick Ebersol, has died at 80 after a battle with pancreatic cancer.",
"keywords": "Susan Saint James, Susan Saint James death, Susan St. James, Dick Ebersol, Kate and Allie, McMillan and Wife, Susan Saint James cause of death, Teddy Ebersol",
"is_breaking": 1,
"image_prompt": "vintage television set glowing in a dim living room, warm nostalgic light, film grain",
"content": """**Susan Saint James**, the Emmy-winning actress who starred in **McMillan & Wife** and **Kate & Allie**, has died. She was 80. A representative confirmed to People that she died on Monday, October 26, 2026. Her family said she had been diagnosed with pancreatic cancer.

"She never met a stranger," her family said in a statement.

The news sent searches for "Susan Saint James," "Dick Ebersol" and "Kate and Allie" soaring across the United States, as fans remembered one of television's most familiar faces of the 1970s and 1980s.

## An Emmy Winner Early in Her Career

Saint James was born Susan Jane Miller on August 14, 1946, in Los Angeles, and grew up in Rockford, Illinois. She began modeling in Paris as a teenager, and at 20 she signed a seven-year contract with Universal Studios.

Her breakthrough came on **The Name of the Game**, where she played Peggy Maxwell. The role won her an **Emmy Award in 1969**. During those early years she also appeared on It Takes a Thief, Ironside, McCloud and Alias Smith and Jones, and later made a guest appearance on M*A*S*H.

## McMillan & Wife and Kate & Allie

From 1971 to 1976, Saint James starred as **Sally McMillan** opposite Rock Hudson on NBC's **McMillan & Wife**, a role that brought her several more Emmy nominations. She left before the final season in a contract dispute, and the show wrote her character out.

Her second signature role came on CBS. From 1984 to 1989 she played Kate McArdle alongside Jane Curtin on **Kate & Allie**, a comedy about two divorced mothers sharing a New York apartment. It earned her two more Emmy nominations.

On the big screen, her credits included:

* **Outlaw Blues** (1977)
* **Love at First Bite** (1979)
* **How to Beat the High Cost of Living** (1980)
* **Carbon Copy** (1981)

## A Love Story That Began on SNL

In 1981, Saint James hosted **Saturday Night Live**, where she met producer **Dick Ebersol**, who later became chairman of NBC Sports. The two married about six weeks later and had three sons: Charlie, Willie and Teddy.

The family suffered a terrible loss on November 28, 2004, when a private plane carrying Ebersol and two of their sons crashed in Colorado after a Thanksgiving trip. Fourteen-year-old **Teddy Ebersol** was killed, along with members of the flight crew. Dick and Charlie Ebersol survived with serious injuries.

## Life After Hollywood

After Kate & Allie ended, Saint James stepped back from acting to raise her children in Litchfield, Connecticut, though she made occasional guest appearances on shows such as Law & Order: Special Victims Unit and Suits. In 1998 she co-founded a baby gift basket business, and she was a longtime volunteer and board member for the **Special Olympics**. She also had two children, Sunshine and Harmony, from her earlier marriage to makeup artist Tom Lucas.

She is survived by her husband, Dick Ebersol, four children and seven grandchildren.

## Frequently Asked Questions

**How did Susan Saint James die?**
Her family said she had been diagnosed with pancreatic cancer. She died on October 26, 2026, at 80.

**Who was Susan Saint James married to?**
NBC Sports executive Dick Ebersol, whom she married in 1981.

**What shows was Susan Saint James known for?**
McMillan & Wife, Kate & Allie and The Name of the Game, which won her an Emmy."""
},
{
"title": "Colts Trade Quenton Nelson and DeForest Buckner in Fire Sale",
"slug": "colts-trade-quenton-nelson-seahawks-deforest-buckner-49ers",
"seo_description": "The Colts traded Quenton Nelson to the Seahawks and DeForest Buckner to the 49ers for mid-round picks. Here's the full trade return and what comes next.",
"keywords": "Quenton Nelson trade, DeForest Buckner trade, Colts trade, Quenton Nelson Seahawks, DeForest Buckner 49ers, Colts rebuild, Ed Dodds, NFL trade deadline 2026, Jonathan Taylor trade",
"image_prompt": "empty football locker room with a single helmet on a bench, moody blue light",
"content": """The **Indianapolis Colts** have officially entered rebuild mode. On Tuesday, interim general manager **Ed Dodds** traded two franchise cornerstones in a matter of hours: eight-time Pro Bowl guard **Quenton Nelson** to the **Seattle Seahawks** and defensive tackle **DeForest Buckner** to the **San Francisco 49ers**.

The moves sent "Quenton Nelson trade," "DeForest Buckner trade" and "Colts trade" climbing on Google as fans digested the end of an era in Indianapolis.

## The Trade Details

* **Quenton Nelson to Seattle:** The Colts receive a 2027 third-round pick and a 2028 fifth-round pick.
* **DeForest Buckner to San Francisco:** The Colts receive a 2027 fourth-round pick.

Both players were in the final year of their contracts, so neither would have counted against the Colts' 2027 salary cap. Seattle takes on the rest of Nelson's base salary, while Indianapolis absorbs dead money on both deals.

## Quenton Nelson's Colts Career

Nelson, 30, was the sixth overall pick out of Notre Dame in 2018 and quickly became one of the best guards in football. He was a first-team All-Pro in each of his first three seasons, earned second-team honors three more times and made eight Pro Bowls.

In nearly nine seasons, he protected 12 different starting quarterbacks for Indianapolis. He was playing out the final year of the four-year, $80 million extension he signed in 2022. He now joins the defending Super Bowl champion Seahawks, who are 4-3.

## DeForest Buckner Returns to San Francisco

For Buckner, 32, the trade is a homecoming. He spent his first four NFL seasons with the 49ers before Indianapolis acquired him in 2020 for a first-round pick.

With the Colts, Buckner recorded 47 sacks and 415 combined tackles and was a first-team All-Pro in 2020. He had publicly criticized the team's direction after a loss to the Titans earlier this month. He returns to a 49ers team that is 6-1 and leads the NFC West.

## Why the Colts Are Selling

Indianapolis is 2-5. The Colts fired general manager **Chris Ballard** after a 26-20 Week 6 loss to Tennessee, ending a tenure that began in 2017, and handed control of the roster to Dodds for the rest of the season.

The rebuild comes with a painful complication: the Colts do not own their 2027 first-round pick. They sent it to the New York Jets as part of last year's trade for cornerback Sauce Gardner, so that pick will go to New York even if Indianapolis finishes with the worst record in the league.

## What's Next Before the Trade Deadline

The NFL trade deadline is **Tuesday, November 10, at 4 p.m. ET**, and more moves could follow. According to ESPN's Adam Schefter, running back Jonathan Taylor and wide receiver Josh Downs could draw interest, though the team's ownership is reportedly reluctant to move Taylor.

On the field, defensive lineman Adetomiwa Adebawore is expected to take on a bigger role in place of Buckner. The Colts play the Jaguars in Jacksonville this Sunday, their first game without either veteran.

## Frequently Asked Questions

**Where was Quenton Nelson traded?**
To the Seattle Seahawks, for a 2027 third-round pick and a 2028 fifth-round pick.

**Where was DeForest Buckner traded?**
Back to the San Francisco 49ers, for a 2027 fourth-round pick.

**When is the 2026 NFL trade deadline?**
Tuesday, November 10, at 4 p.m. ET."""
},
{
"title": "Butter Recall: Miyoko's Plant Butter Pulled in 10 States Over E. Coli Risk",
"slug": "butter-recall-miyokos-plant-milk-butter-10-states-e-coli-yeast-mold",
"seo_description": "Butter recall: Miyoko's European Style Salted Plant Milk Butter was recalled in 10 states over yeast, mold and possible E. coli. Check the lot code and date.",
"keywords": "butter recall, butter recalled, Miyoko's butter recall, plant-based butter recall, FDA recall October 2026, E. coli recall, Class II recall, Market Basket recall",
"image_prompt": "stick of butter on a kitchen counter next to a refrigerator, soft morning light, clean composition",
"content": """A **butter recall** is trending across the U.S. after the Food and Drug Administration classified a recall of **Miyoko's Creamery European Style Salted Plant Milk Butter**. The vegan butter was pulled from stores in 10 states over concerns about yeast, mold and possible **E. coli** contamination.

Here's what you need to know, including how to check whether the butter in your fridge is affected.

## Which Butter Is Being Recalled?

The recall covers one product:

* **Product:** Miyoko's Creamery European Style Salted Plant Milk Butter, 8 oz.
* **UPC:** 857554005773
* **Lot number:** 07871
* **Best-by date:** 11/5/2026

The recall was initiated on **September 11, 2026**, by **Prosperity Organic Foods Inc.**, the company behind the Miyoko's brand. Products with a different lot number or best-by date are not part of this recall.

## States Where the Butter Was Sold

The recalled butter was distributed in **10 states**:

* Connecticut
* Florida
* Georgia
* Illinois
* Indiana
* Iowa
* Maryland
* New Hampshire
* New Jersey
* Wisconsin

## Why Was the Butter Recalled?

According to the FDA's enforcement report, the recall was issued over concerns about "yeast, mold, and E. coli." The grocery chain **Market Basket** first cited high yeast results on September 3, and on September 17 said the product could potentially contain E. coli.

On **October 23, 2026**, the FDA gave the recall a **Class II** designation. That means the product may cause temporary or medically reversible health problems, while the chance of serious health consequences is considered remote.

No illnesses linked to the product have been reported.

## What the Company Says

Miyoko's said it pulled "a very small number of products." In a comment on Facebook, the company said the affected items had been fully removed from store shelves. As of the latest reports, it had not posted a formal recall notice on its website.

## What Should You Do?

If you bought Miyoko's plant butter in one of the affected states, check the label for the UPC, lot number and best-by date listed above.

* **Don't eat it** if it matches. Throw it away or return it to the store where you bought it.
* **Watch for symptoms** if you already ate it. E. coli symptoms often appear three to four days after exposure and can include stomach cramps, vomiting and bloody diarrhea.
* **Call your doctor** if you develop symptoms of foodborne illness.

Some molds can also trigger allergic or respiratory reactions, so anyone with mold allergies should be especially careful.

## A Busy Year for Butter Recalls

This is not the first time butter has made recall headlines. Major dairy brands, including Cabot Creamery, have faced butter recalls in recent years over bacterial contamination concerns, a reminder to check recall notices regularly, especially before holiday baking season.

## Frequently Asked Questions

**What butter is recalled right now?**
Miyoko's Creamery European Style Salted Plant Milk Butter, 8 oz., lot 07871, best by 11/5/2026.

**Is regular dairy butter part of this recall?**
No. This recall covers only the Miyoko's plant-based product listed above.

**Has anyone gotten sick?**
No illnesses have been reported."""
},
{
"title": "McDonald's New Holiday Menu 2026: Cookie Butter Drinks and McRib",
"slug": "mcdonalds-new-holiday-menu-2026-cookie-butter-drinks-mcrib",
"seo_description": "McDonald's new holiday menu items for 2026: five festive drinks, including Cookie Butter lattes and a Red Bull Frosted Cranberry Energizer, arrive Nov. 3.",
"keywords": "McDonald's new holiday menu items, McDonald's holiday menu 2026, McDonald's cookie butter latte, Red Bull Frosted Cranberry Energizer, McRib 2026, McDonald's holiday drinks, Frosted Cranberry Splash",
"image_prompt": "festive coffee cups with whipped cream and cookie crumbs on a cafe table, holiday lights bokeh, no logos",
"content": """The holidays are coming early to the drive-thru. McDonald's has announced its **new holiday menu items for 2026**, a lineup of five festive drinks arriving next week, and the **McRib** is already back in select cities.

Searches for "McDonald's new holiday menu items" jumped after the Oct. 27 announcement. Here's everything coming to the menu and when you can try it.

## McDonald's Holiday Drinks 2026

The five limited-time drinks arrive on **Monday, November 3**, at participating restaurants across the U.S.

### Cookie Butter Drinks

Three McCafé drinks feature cookie butter flavor, topped with sweet vanilla whipped cream and caramel cookie crumbs:

* **Cookie Butter Latte**
* **Cookie Butter Iced Coffee**
* **Cookie Butter Frappé**

According to Allrecipes, the cookie butter lineup takes the place of last season's Caramel Apple Pie drinks.

### Frosted Cranberry Drinks

Two cranberry drinks round out the menu:

* **Frosted Cranberry Splash with Sprite:** Sprite blended with orange and cranberry flavors, topped with cold foam and cranberry sprinkles.
* **Red Bull Frosted Cranberry Energizer:** Cranberry flavor with Red Bull, cold foam and sprinkles. Customers can choose classic Red Bull or Red Bull Zero.

McDonald's describes the Red Bull drink as "made for packed holiday schedules and festive adventures." It follows the Red Bull Dragonberry Energizer, which launched in August.

The drinks are available only for the holiday season, and availability can vary by restaurant. McDonald's has not announced national pricing.

## The McRib Is Back

The **McRib** returned on **October 27** at select locations, including restaurants in:

* Los Angeles
* Chicago
* Miami
* Atlanta
* Philadelphia
* Dallas

The cult-favorite sandwich features boneless pork in barbecue sauce, topped with onions and pickles on a bun. It left the permanent menu in 2012 and has returned as a limited-time item in many years since, often in late fall. Because the rollout is limited to certain markets, fans should check the McDonald's app to see whether the McRib is available at a restaurant nearby before making the trip.

## How McDonald's Compares to Other Holiday Menus

McDonald's isn't the only chain rolling out seasonal items:

* **Sonic:** Its winter menu, including a Santa Slush Float, arrives November 2, with early access for app users.
* **Starbucks:** Its holiday menu launches November 5, with a new Tiramisu Velvet Latte alongside returning favorites such as the Peppermint Mocha.
* **Arby's:** The Deep Fried Turkey Gobbler returned on October 26.

## Tips for Trying the New Menu

* **Use the app:** McDonald's often runs app-only deals when new items launch.
* **Go early:** Limited-time drinks can sell out at busy locations.
* **Check participation:** Not every restaurant carries every item.

## Frequently Asked Questions

**When does the McDonald's holiday menu come out?**
The five new holiday drinks launch November 3, 2026, at participating U.S. restaurants.

**What are the new McDonald's holiday drinks?**
A Cookie Butter Latte, Cookie Butter Iced Coffee, Cookie Butter Frappé, Frosted Cranberry Splash with Sprite and Red Bull Frosted Cranberry Energizer.

**Is the McRib back in 2026?**
Yes, at select locations starting October 27."""
},
]


def image_url(prompt, seed):
    full = prompt + ", ultra realistic, 4k, editorial photography, dramatic lighting, no text, no faces, no logos"
    return f"https://image.pollinations.ai/prompt/{urllib.parse.quote(full)}?width=1200&height=675&seed={seed}&nologo=true"


def seed_database():
    conn = sqlite3.connect("news.db")
    cur = conn.cursor()
    published = "2026-10-28 13:00:00"  # UTC (16:00 Istanbul)
    for i, a in enumerate(ARTICLES_E):
        wc = len(a["content"].split())
        assert 500 <= wc <= 600, f"{a['slug']}: {wc} words"
        img = image_url(a["image_prompt"], 265000 + i)
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
