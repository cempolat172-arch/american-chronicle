"""
Seed for Oct 31, 2026: new Google Trends US topics (long-form, 800-1000 words).
- Halloween 2026 food deals and freebies
- Poland constitutional court crisis
- Warriors vs Lakers: Curry leads historic comeback
- McRib class action lawsuit moves forward
- Samsung News app discontinued
Run from the project root:  python3 scratch/seed_october31_trends.py
"""
import sqlite3
import urllib.parse

ARTICLES_G = [
{
"title": "Halloween 2026 Food Deals: Free Meals, Freebies and Kids Eat Free",
"slug": "halloween-2026-food-deals-freebies-kids-eat-free-restaurants",
"seo_description": "Halloween 2026 food deals: free Krispy Kreme doughnuts, Chipotle's $6 Boorito, kids eat free at Denny's and Applebee's, and more Oct. 31 freebies.",
"keywords": "Halloween 2026 food deals, Halloween freebies, kids eat free Halloween, Chipotle Boorito 2026, Krispy Kreme Halloween free doughnut, Halloween restaurant deals, Halloween 2026, Sonic corn dogs Halloween",
"image_prompt": "carved jack-o-lantern pumpkins and candy bowl on a porch at dusk, warm orange glow, autumn leaves",
"content": """**Halloween 2026** falls on a Saturday, which means more families than usual will be out trick-or-treating, hosting parties and grabbing dinner on the go. The good news: restaurants across the country are rolling out **Halloween food deals**, from free doughnuts and kids' meals to $6 burritos for anyone who shows up in costume.

Here is a complete guide to the best Halloween freebies and discounts for October 31, 2026, organized so you can plan the whole day. Offers vary by location, so it's always smart to confirm with your local restaurant before you go.

## Best Halloween Freebies (Wear a Costume)

Several chains reward customers who dress up. These are the easiest free treats to grab:

* **Krispy Kreme:** Wear a costume to a participating U.S. shop on Oct. 30 or 31 and get one free Original Glazed or Classic Ring doughnut. No purchase is needed, limit one per guest.
* **Chipotle Boorito:** Chipotle Rewards members who visit a restaurant in costume from **3 p.m. to close** on Halloween can get an entrée for **$6**. Scan your rewards card at checkout. It's limited to one per member and is in-restaurant only.
* **Harry Potter Shop (Chicago Butterbeer Bar):** Free pumpkin-shaped sugar cookie for guests in costume, Oct. 29 to 31.
* **Rainbow Cone:** Kids 12 and under in costume get a free single scoop with any purchase.

## Kids Eat Free on Halloween

Feeding a group of hungry trick-or-treaters gets expensive fast. These **kids eat free Halloween** deals can help:

* **Applebee's:** A free kids' meal for children 12 and under in costume when an adult buys an entrée, at select locations on Oct. 31.
* **Denny's:** A free kids' meal with an adult entrée purchase, dine-in only. The limit is one kids' meal per adult entrée and two per ticket.
* **Outback Steakhouse:** A free kids' meal with an adult entrée, dine-in or online with code **SPOOKYFREE**.
* **Red Lobster:** From Oct. 30 to Nov. 1, costumed kids can get up to two free kids' meals per table when dining in with a full-price adult dinner entrée. For takeout, use code **SPOOKY26** online for one free kids' meal per adult entrée.
* **MOD Pizza:** Kids 12 and under in costume eat free with the purchase of a regular pizza or salad, in-restaurant only.
* **Red Robin:** A free kids' sundae with a kids' meal purchase for children under 11 in costume, Oct. 30 to Nov. 1, dine-in only.
* **Chick-fil-A:** Some franchises offer a free kids' meal or treat to costumed children. Offers vary, so check with your local restaurant.

## Halloween Dinner Deals

If you need a quick family dinner between trick-or-treating stops, these deals are worth a look:

* **Sonic:** 50-cent corn dogs all day on Oct. 31 at participating drive-ins. No app or code needed.
* **Shake Shack:** A free ShackBurger with an order of $10 or more through Oct. 31, using code **SCARYGOOD** online or in the app.
* **KFC:** 50 nuggets for $20 on Halloween. Check the app or your local restaurant.
* **Papa Johns:** The Jack-O'-Lantern pizza is $11.99, down from $16.99, through Oct. 31.
* **Pizza Hut:** The My Haunt Box, a personal Fang Pizza with fries or four boneless wings, is $6.99 through the end of October.
* **Qdoba:** Rewards members who buy an entrée and a drink get a second entrée free on Oct. 31 and Nov. 1.
* **Burger King:** Royal Perks members can get a buy-one, get-one Whopper Jr. digital coupon on Oct. 31.
* **Noodles & Company:** Rewards members get 50% off regular-size ramen with the purchase of a regular entrée.
* **Long John Silver's:** A Chicken & Mac Party Pack with nine pieces of chicken and family-size mac and cheese is $15, Oct. 30 to Nov. 1.
* **White Castle:** Craver Nation Rewards members can get five Original Sliders for $3 through Oct. 31.

## Sweet Treats and Dessert Deals

* **Baskin-Robbins:** Rewards members get 31% off scoops on Oct. 31.
* **Wendy's Boo! Book:** For $1, get five free Jr. Frosty coupons, valid through Dec. 31, plus a $1.99 kids' meal coupon. The books are sold through Nov. 1.
* **Jamba:** 31% off eligible orders on Oct. 31 with code **SPOOKY**. Catering is excluded.
* **Dairy Queen:** A $4 Blizzard Buddy plush keychain with any order, with a chance to find a rare plush that comes with free Blizzards for a year.
* **Raising Cane's:** A 32-ounce Halloween collectible cup for $1.49 with any combo or 32-ounce drink, while supplies last.

## McDonald's Boo Buckets

McDonald's is bringing back its popular **Boo Buckets** with Happy Meals through Oct. 31, this year featuring Disney villains: Maleficent, Ursula, Cruella de Vil, Jafar and Scar. They are available only while supplies last, so earlier is better.

## Tips to Get the Most Out of Halloween Deals

* **Download the apps first.** Many of the best offers, including Chipotle, Qdoba and Burger King, require a rewards account. Sign up before you leave the house.
* **Wear the costume.** Several deals depend on it, and staff usually make the call at the counter.
* **Read the fine print.** Many deals are dine-in only, limited to one per guest or require an adult entrée.
* **Go early or late.** Halloween evening is one of the busiest nights of the year for restaurants, especially in neighborhoods with heavy trick-or-treat traffic.
* **Call ahead.** Franchise locations may opt out of national promotions.

## Halloween Safety Reminder

With Halloween on a Saturday, expect heavier foot traffic and more kids out after dark. Drivers should slow down in residential areas, and families should add reflective tape or a flashlight to costumes so children are easy to see.

## Frequently Asked Questions

**What restaurants give free food on Halloween 2026?**
Krispy Kreme gives a free doughnut to anyone in costume, and kids can eat free at Applebee's, Denny's, Outback, Red Lobster and MOD Pizza with qualifying purchases.

**What time is the Chipotle Boorito deal?**
From 3 p.m. to closing on Oct. 31, for Chipotle Rewards members in costume.

**Do I need a costume for the Krispy Kreme Halloween deal?**
Yes. Wear a costume to a participating shop on Oct. 30 or 31 for one free doughnut, no purchase necessary."""
},
{
"title": "Poland Court Crisis: Constitutional Tribunal Chief Suspended, Protests Erupt",
"slug": "poland-constitutional-tribunal-chief-suspended-protests-tusk-nawrocki",
"seo_description": "Poland's Constitutional Tribunal chief Bogdan Swieczkowski was suspended, sparking protests and a clash between Donald Tusk's government and President Nawrocki.",
"keywords": "Poland, Poland constitutional court, Constitutional Tribunal Poland, Bogdan Swieczkowski, Donald Tusk, Karol Nawrocki, Law and Justice PiS, Poland rule of law, Poland protests",
"image_prompt": "classical European courthouse facade at night with police barriers in front, dramatic blue light, no people",
"content": """**Poland** is in the middle of its deepest constitutional showdown in years. On Friday, October 30, the head of the country's top court, the **Constitutional Tribunal**, was suspended, riot police were deployed outside the court in Warsaw, and President **Karol Nawrocki** turned his plane around mid-flight to return home.

The crisis made "Poland" one of the top searches in the United States, with more than 100,000 searches in a day, as Americans tried to understand what is happening in one of NATO's most important eastern members.

## What Happened in Warsaw

The Constitutional Tribunal announced that its president, **Bogdan Swieczkowski**, had been suspended. The suspension was announced by fellow judge **Anna Korwin-Piotrowska**, who has now been placed in charge of the tribunal.

The move followed a request from Justice Minister **Waldemar Zurek**, who also serves as attorney general, to lift the immunity of Swieczkowski and his deputy, Bartlomiej Sochanski. Zurek accused them of failing to perform their duties.

According to Al Jazeera, Swieczkowski had allegedly used his position over the past six months to block judges elected by the current parliamentary majority from taking up their duties, which had effectively paralyzed the court.

## The Court Calls It a "Coup"

The tribunal's official account on X rejected the suspension, calling the situation a "coup d'etat" and insisting that Swieczkowski remained in office. The court also argued that Korwin-Piotrowska could not become interim chief because the president had never sworn her in. By Friday evening, the court's official website was inaccessible.

## Protests and Police

Supporters of the opposition **Law and Justice (PiS)** party gathered at the court gates. According to an AFP journalist, some chanted "Tusk traitor," while others prayed with rosaries and religious images.

Police said they entered the court premises after incidents in which objects were thrown at officers. Three people were detained.

## What Each Side Says

**The government:** Prime Minister **Donald Tusk**, who leads the centrist Civic Coalition, defended the move on X. He said restoring the rule of law is the government's duty, calling it "a difficult process, sometimes painful," that requires decisive action.

**The opposition:** PiS, now Poland's largest opposition party, condemned the suspension. Former Justice Minister **Zbigniew Ziobro** called it a "blatant, criminal attack on the constitutional order."

**The president:** Nawrocki, a right-wing independent allied with PiS, called off an official trip to a sporting event in Senegal, saying the president must be in Poland at such a time.

## Why Poland's Top Court Is So Contested

The fight over the Constitutional Tribunal goes back nearly a decade.

* **2015 to 2023:** PiS governed Poland. Critics in Poland and across the European Union accused the party of gaining political control over the court by appointing friendly judges. During this period the court ruled more than once that Polish law took precedence over EU law, deepening a long rule-of-law dispute with Brussels.
* **2023:** Tusk's coalition won the election, promising to restore judicial independence and repair relations with the EU.
* **Since then:** Two government attempts to overhaul the courts were vetoed by PiS-aligned presidents, including Nawrocki.
* **Judge appointments:** Since his election in mid-2025, Nawrocki has refused to swear in three of the six judges nominated by parliament, citing alleged flaws in how they were selected. Korwin-Piotrowska is one of them.

## Two Very Different Readings

Supporters of the government argue that judges installed under PiS were appointed improperly and that the court has been used to block reforms passed by an elected majority. In their view, action against the court's leadership is necessary to restore a functioning, independent judiciary.

Critics argue that the government is using prosecutorial power to remove a sitting court chief without a clear legal basis, and that sidelining judges this way is itself a threat to the separation of powers. They say disputes over judicial appointments should be settled through the constitution, not through suspensions and police deployments.

With each side refusing to recognize judges chosen by the other, Poland now faces competing claims over who legitimately leads its top court.

## Why It Matters Beyond Poland

Poland is the largest economy in Central Europe, a key NATO ally and a major hub for military aid flowing to Ukraine. Political instability in Warsaw draws close attention in Brussels and Washington. The EU has tied rule-of-law issues to Poland's access to EU funds in the past, and any decision by EU institutions will be watched closely.

## What Comes Next

The immediate questions are whether Swieczkowski's immunity will be lifted, whether courts and state institutions will recognize Korwin-Piotrowska's leadership, and how President Nawrocki responds after returning to Warsaw. With both sides claiming to defend the constitution, the standoff is unlikely to end quickly.

## Frequently Asked Questions

**Why is Poland trending?**
Poland's Constitutional Tribunal chief was suspended on Oct. 30, 2026, sparking protests and a political standoff.

**Who is Bogdan Swieczkowski?**
The president of Poland's Constitutional Tribunal, appointed during the period when the Law and Justice party governed.

**Who are Donald Tusk and Karol Nawrocki?**
Tusk is Poland's prime minister, leading a centrist coalition. Nawrocki is the president, a right-wing independent allied with the opposition Law and Justice party."""
},
{
"title": "Warriors vs Lakers: Curry's 31 Points Spark Historic 112-95 Comeback",
"slug": "lakers-vs-warriors-curry-31-points-historic-comeback-112-95-nba-cup",
"seo_description": "Lakers vs Warriors recap: Stephen Curry scored 31 as Golden State erased a 23-point first-quarter deficit to beat Luka Doncic and the Lakers 112-95.",
"keywords": "Lakers vs Warriors, Warriors vs Lakers, Stephen Curry, Luka Doncic, Warriors comeback, NBA Cup, Curry passes Dominique Wilkins, Brandin Podziemski, Lakers score",
"image_prompt": "basketball resting on an empty glossy arena court under bright lights, golden hour reflections",
"content": """The **Golden State Warriors** pulled off one of the most remarkable comebacks in NBA history on Friday night. After falling behind by 23 points in the first quarter, Golden State stormed back to beat the **Los Angeles Lakers 112-95** at Chase Center, led by 31 points from **Stephen Curry**.

"Lakers vs Warriors" was the most-searched term in the United States on Friday night, with more than 500,000 searches, as the NBA Cup matchup turned into an instant classic.

## Lakers vs Warriors Final Score

* **Final:** Warriors 112, Lakers 95
* **After the first quarter:** Lakers 38, Warriors 15
* **Halftime:** 53-53
* **Competition:** NBA Cup group play (Group C)

## A Nightmare First Quarter

The game could not have started worse for Golden State. **Luka Doncic** was unstoppable early, scoring 21 points in the first quarter on 7-of-12 shooting, including five 3-pointers. The Warriors made it easy for him by committing 10 turnovers in the opening 12 minutes alone, and Los Angeles raced to a 38-15 lead.

At that point, the game looked like a repeat of the season opener, when the Lakers beat the Warriors by 22 points.

## The Second-Quarter Turnaround

Golden State answered with a perfect mirror image. The Warriors won the second quarter **38-15**, the exact score the Lakers had posted in the first, and the teams went to halftime tied 53-53.

The bench played a huge role in the turnaround. **De'Anthony Melton** finished with 16 points and **Georges Niang** added 11, giving the Warriors energy and spacing while the starters regrouped.

## Curry Takes Over

In the second half, Curry took control. At the 6:22 mark of the third quarter, he buried a 3-pointer right over Doncic. Doncic answered with a 3 of his own moments later, but Golden State never gave back the momentum.

Curry finished with **31 points, 6 assists and 4 rebounds**. Along the way, he passed **Dominique Wilkins** (26,668 points) for **18th place on the NBA's all-time scoring list**.

**Brandin Podziemski** added 21 points, six assists and five rebounds, giving Golden State a reliable second scorer.

## Doncic's Big Night Falls Short

Doncic finished with **37 points, 7 rebounds and 5 assists**, but he scored just 16 points after his scorching first quarter. Frustration showed late: Doncic picked up a technical foul in the third quarter, and teammate Matisse Thybulle was hit with one in the fourth.

The Lakers did take advantage of Golden State's mistakes. The Warriors finished with 17 turnovers, and Los Angeles turned them into 25 points. But after the first quarter, the Lakers could not find a consistent second scoring option to support Doncic.

## A Comeback for the Record Books

According to the Associated Press, the Warriors' win set two notable marks:

* **Largest margin of victory** in the shot-clock era for a team that trailed by 20 or more points after one quarter. The previous best was also a Warriors game: a 124-110 win over the Chicago Bulls on March 4, 1976, after trailing 41-18.
* **First team in the shot-clock era**, including the playoffs, to trail by 23 or more after the first quarter and be tied or ahead at halftime.

## Key Stats

| Player | Team | Points | Other |
|---|---|---|---|
| Luka Doncic | LAL | 37 | 7 reb, 5 ast |
| Stephen Curry | GSW | 31 | 6 ast, 4 reb |
| Brandin Podziemski | GSW | 21 | 6 ast, 5 reb |
| De'Anthony Melton | GSW | 16 | Off the bench |
| Georges Niang | GSW | 11 | Off the bench |

## What It Means in the NBA Cup

The NBA Cup is the league's in-season tournament, and group-play games count both toward the regular-season standings and the race for a spot in the knockout rounds. Group C also includes the San Antonio Spurs, Portland Trail Blazers and Sacramento Kings, so every win matters. For Golden State, beating a Western Conference rival after such a poor start could prove valuable when tiebreakers come into play.

## Curry Climbs the All-Time List

Passing Wilkins is another milestone in a career that has already rewritten the record books. Curry is the NBA's all-time leader in 3-pointers made, and his climb up the overall scoring list shows how much his game has expanded beyond long-range shooting. Each passing week this season could move him closer to the top 15.

## What's Next

Both teams play again on Sunday night. The Lakers host the **Toronto Raptors**, while the Warriors host the **LA Clippers**.

## Frequently Asked Questions

**Who won Lakers vs Warriors?**
The Golden State Warriors won 112-95 on Oct. 30, 2026.

**How many points did Stephen Curry score?**
Curry scored 31 points and passed Dominique Wilkins for 18th on the NBA's all-time scoring list.

**How big was the Warriors' comeback?**
Golden State trailed by 23 points after the first quarter and still won by 17."""
},
{
"title": "McRib Lawsuit: Judge Says McDonald's Must Face Class Action",
"slug": "mcdonalds-mcrib-class-action-lawsuit-judge-rules-rib-meat",
"seo_description": "McDonald's McRib class action lawsuit can move forward. A Chicago judge says shoppers may reasonably expect rib meat. Here's what the case claims and what's next.",
"keywords": "McDonald's McRib class action lawsuit, McRib lawsuit, McRib rib meat, McDonald's lawsuit 2026, Judge April Perry, McRib ingredients, is there rib meat in the McRib, McRib 2026",
"image_prompt": "barbecue pork sandwich on a wooden board with pickles and onions, dark moody background, no branding",
"content": """The **McRib** is back on menus this fall, and so is a legal fight over what's inside it. A federal judge in Chicago has ruled that **McDonald's** must face a proposed **class action lawsuit** claiming the chain misleads customers into thinking the sandwich contains pork rib meat.

"McDonald's McRib class action lawsuit" became a top search in the U.S. after the Oct. 30 ruling, as fans of the cult-favorite sandwich asked a simple question: is there actually rib meat in the McRib?

## What the McRib Lawsuit Claims

The lawsuit, filed in December 2025, was brought by consumers who say they bought McRibs believing the sandwich contained pork rib meat. Their main arguments:

* **The name and shape:** McDonald's allegedly shapes the McRib patty with ridges designed to look like a rack of pork ribs, and the name itself suggests ribs.
* **The meat:** The plaintiffs say the patty is made from restructured pork, including lower-grade cuts such as pork shoulder. The original complaint also alleged it could contain heart, tripe and scalded stomach.
* **The price:** They argue the sandwich's relatively high price, about $7, and its limited-time availability make it look like a premium product, so customers overpaid.

## What McDonald's Says

McDonald's strongly disputes the claims. The company says the McRib is made with **100% pork** sourced from U.S. farmers and suppliers, and it denies that the sandwich contains hearts, tripe or scalded stomach. It has called the lawsuit meritless.

In court, McDonald's argued that distinctive product names do not mislead reasonable consumers, and that the plaintiffs' preference for a particular cut of pork does not turn truthful marketing into fraud.

## What the Judge Ruled

U.S. District Judge **April Perry** dismissed some of the plaintiffs' claims but allowed the central deceptive-marketing allegations to move forward. Her key points:

* **It's too early to decide.** Perry said she could not conclude at this stage that no reasonable consumer would expect the McRib to contain pork rib meat.
* **The name is not "fanciful."** "Plaintiffs' proffered understanding of 'McRib' is not unreasonable or fanciful," she wrote.
* **Customers don't have to investigate.** She noted that McDonald's website describes the sandwich only as containing pork, and said consumers should not be expected to research the ingredients of a $7 sandwich before buying it.
* **The shape matters.** Perry said advertising that highlights the rib-like shape of the patty could support the claim that McDonald's intended to create a particular impression, though the plaintiffs will need more proof.

The plaintiffs' lawyer, Thiago Coelho, said they will keep pursuing accountability for what they describe as deceptive marketing.

## What This Ruling Does and Doesn't Mean

It's important to understand what happened here. The judge did **not** find that McDonald's did anything wrong. A ruling on a motion to dismiss only decides whether the claims are strong enough on paper to continue.

From here, the case moves into discovery, where both sides exchange evidence. The plaintiffs must still prove their allegations, and the court must also decide whether to certify a class, which would allow the case to proceed on behalf of a larger group of McRib buyers. Many cases like this are settled before trial, but there is no sign yet of a settlement.

## A Familiar Kind of Food Lawsuit

The McRib case is part of a wave of **food labeling lawsuits** in the United States. Over the past decade, consumers have sued food companies over everything from the size of fast-food burgers in ads to whether "vanilla" products contain real vanilla. Many of these cases are dismissed early, which is why rulings that let a case continue tend to draw attention.

## The McRib's Cult Following

The McRib has spent decades building a devoted fan base, in part because it appears only for limited runs. McDonald's took it off the permanent menu in 2012, and it has since returned in many years as a limited-time item, often in late fall. This year it returned on Oct. 27 at select locations, including Los Angeles, Chicago, Miami, Atlanta, Philadelphia and Dallas.

## Should You Still Buy a McRib?

The lawsuit is about how the sandwich is marketed, not about food safety. No one has claimed the McRib is unsafe to eat. If you enjoy it, the ruling doesn't change anything about the sandwich itself. Customers who care about which cut of pork they're eating can check McDonald's nutrition and ingredient information before ordering.

## Frequently Asked Questions

**Is there rib meat in the McRib?**
McDonald's says the McRib is made with 100% pork. The lawsuit alleges it does not contain pork rib meat and is made from restructured pork such as shoulder.

**Did McDonald's lose the McRib lawsuit?**
No. A judge only ruled that the core claims can move forward. The case has not been decided.

**Who is the judge in the McRib case?**
U.S. District Judge April Perry in Chicago."""
},
{
"title": "Samsung News App Discontinued: Shutdown Date and What to Use Instead",
"slug": "samsung-news-app-discontinued-2026-shutdown-date-alternatives",
"seo_description": "Samsung News is being discontinued on Dec. 21, 2026. Here's what is shutting down on Galaxy phones, what happens to your data and the best alternatives.",
"keywords": "Samsung News app discontinued 2026, Samsung News shutting down, Samsung News shutdown date, Samsung News alternative, Google Discover Galaxy, Samsung Free, Galaxy news widget, One UI",
"image_prompt": "modern smartphone lying on a desk showing a blank glowing screen, soft blue light, minimalist workspace",
"content": """Samsung is pulling the plug on one of the built-in features on Galaxy phones and tablets. The **Samsung News** app is being **discontinued**, and the service will stop working in December 2026.

"Samsung News app discontinued 2026" jumped on Google Trends as Galaxy owners noticed shutdown notices and wondered what will happen to their news feed. Here's everything you need to know.

## When Is Samsung News Shutting Down?

According to an in-app notice first seen by users in India and South Korea, **Samsung News will shut down at 12:00 a.m. UTC on December 21, 2026**. That works out to 7 p.m. Eastern time on December 20 in the United States.

After that date:

* The **Samsung News app** stops delivering content.
* The **Samsung News widget** stops receiving updates.
* The **home screen news feed** and the dedicated media page go away.

The notice has so far appeared in India and South Korea. Tech sites expect the change to reach other markets too, but Samsung has not officially confirmed the timeline for the U.S.

## What Happens to Your Data?

Samsung says it will **delete user data**, including profiles and personalization information, after the shutdown. The exception is data that local laws require it to keep, which will be retained only for the legally required period. Samsung also recommends removing the Samsung News widget from your home screen.

If you've saved articles inside the app, consider opening them in a browser and bookmarking anything you want to keep before the December deadline.

## Why Is Samsung Ending Samsung News?

Samsung has not given a specific reason. Tech observers see it as part of a broader effort to trim redundant services, especially those that overlap with Google apps already built into Android. Android Headlines noted that Samsung had stopped adding new content partners about two years ago, a sign the service was being wound down.

Samsung is also shutting down **Daily+** on its TVs and smart monitors, another sign the company is narrowing its in-house content offerings.

## A Short History of Samsung's News Feed

Samsung News is the latest in a long line of Samsung news and content feeds:

* **Bixby Home** (2017): The original swipe-left feed on Galaxy phones.
* **Samsung Daily** (2019): Replaced Bixby Home.
* **Samsung Free:** Followed Samsung Daily, mixing news, games and free TV.
* **Samsung News** (2023): Replaced Samsung Free and focused on news.

Each change reshaped the leftmost home screen panel on Galaxy devices, and the December shutdown will likely change it again.

## What Will Replace Samsung News?

Samsung has not named an official replacement. However, Android Authority reports that the leftmost One UI home screen panel will likely default to **Google Discover**, which is already available on supported Galaxy phones and tablets.

Not everyone is happy. Some longtime users said they preferred Samsung News because it felt lighter, with fewer ads and less clutter. Others admitted they never used it at all and already rely on Google or an RSS reader.

## Best Samsung News Alternatives

If you used Samsung News every day, here are some options to consider:

* **Google Discover:** Built into most Android phones and personalized to your interests.
* **Google News:** A free app with "For you," headlines and local news sections.
* **MSN:** Microsoft's news aggregator, with customizable topics.
* **RSS readers:** Apps such as Feedly or Inoreader let you follow specific websites directly, with no algorithm deciding what you see.
* **Publisher apps and newsletters:** Following trusted outlets directly is often the best way to get reliable news.

## Does This Affect Other Galaxy Features?

No. The shutdown applies only to Samsung News and its widget, feed and media page. Your phone's other Samsung apps and services, including the Galaxy Store, Samsung Health and Samsung Wallet, are not part of this announcement. Your phone will keep receiving its normal One UI software updates, and you don't need to do anything to keep using your device as usual. The only change most people will notice is a different feed on the leftmost home screen panel.

## How to Prepare Your Galaxy Phone

1. **Remove the Samsung News widget** from your home screen.
2. **Pick a new news app** and set up your interests before December.
3. **Check your leftmost home screen panel** in your home screen settings to choose what appears there.
4. **Save any articles** you want to keep before December 21.

## Frequently Asked Questions

**When will Samsung News stop working?**
At 12:00 a.m. UTC on December 21, 2026, according to Samsung's in-app notice.

**Is Samsung News shutting down in the U.S.?**
The notice has appeared in India and South Korea. Wider rollout is expected, but Samsung hasn't confirmed U.S. timing.

**What replaces Samsung News on Galaxy phones?**
Samsung hasn't announced a replacement, but Google Discover is expected to become the default home screen feed."""
},
]


def image_url(prompt, seed):
    full = prompt + ", ultra realistic, 4k, editorial photography, dramatic lighting, no text, no faces, no logos"
    return f"https://image.pollinations.ai/prompt/{urllib.parse.quote(full)}?width=1200&height=675&seed={seed}&nologo=true"


def seed_database():
    conn = sqlite3.connect("news.db")
    cur = conn.cursor()
    published = "2026-10-31 07:00:00"  # UTC (10:00 Istanbul)
    for i, a in enumerate(ARTICLES_G):
        wc = len(a["content"].split())
        assert 800 <= wc <= 1100, f"{a['slug']}: {wc} words"
        img = image_url(a["image_prompt"], 267000 + i)
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
