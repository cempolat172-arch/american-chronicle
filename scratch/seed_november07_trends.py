"""
Seed for Nov 7, 2026: new Google Trends US topics (long-form, keyword-rich).
- Stephen Miller replaces Susie Wiles as White House chief of staff
- Tesla Cybertruck discontinued (production ends 2027)
- Polar vortex November 2026 and the CPC heavy snow map
- Blue Angels remove Maj. Scott Laux
Run from the project root:  python3 scratch/seed_november07_trends.py
"""
import sqlite3
import urllib.parse

ARTICLES_H = [
{
"title": "Stephen Miller Replaces Susie Wiles as White House Chief of Staff",
"slug": "stephen-miller-replaces-susie-wiles-white-house-chief-of-staff",
"seo_description": "Stephen Miller will replace Susie Wiles as White House chief of staff after the midterms. Who is Stephen Miller, why Wiles is out and how both parties reacted.",
"keywords": "Stephen Miller, Stephen Miller chief of staff, Susie Wiles, Susie Wiles out, White House chief of staff, Trump chief of staff, who is Stephen Miller, midterm elections 2026, Hakeem Jeffries, Chuck Schumer",
"is_breaking": 1,
"image_prompt": "White House exterior at dusk with dramatic clouds, American flag on the roof, cinematic wide shot, no people",
"content": """**Stephen Miller** is the new **White House chief of staff**. President Donald Trump announced on Friday, November 6, 2026, that **Susie Wiles** is leaving the job and that Miller, his longtime adviser, will replace her. Miller takes over on Monday.

The shake-up made "Stephen Miller" the top political search in the United States, with more than 200,000 searches in a day, along with "Susie Wiles" and "who is Stephen Miller." It comes just days after the **2026 midterm elections**, in which, according to NPR, Republicans were swept out of power in Congress.

## What Trump Said

Trump made the announcement on his platform, Truth Social, and later spoke to reporters about the change.

"Stephen's been with me since the beginning. He gets it," Trump said.

According to NPR, Trump said Wiles will continue to work for him on political operations, so she is not leaving his orbit entirely.

## Susie Wiles' Statement

Wiles, the first woman ever to serve as White House chief of staff, responded in a statement on X.

"I'm so proud to have been a part of what we've accomplished together from securing our border and cutting taxes to strengthening our economy and putting America First," she wrote. "While my role may be changing, my commitment to the President and the mission never will."

## Why Is Susie Wiles Out?

Trump has not given a detailed public explanation. Several news outlets, including CNN, reported, citing sources, that the president had grown frustrated after the midterm results. NPR described the move as a "defiant note" from Trump following his party's losses.

The timing matters. With Democrats taking control of Congress, the second half of Trump's term is likely to involve more investigations, more vetoes and tougher negotiations over spending. Picking Miller, one of his most loyal and combative aides, signals that the president does not plan to soften his approach.

## Who Is Susie Wiles?

Susie Wiles is a veteran Republican strategist from Florida. She worked on Trump's 2020 campaign in Florida, helped lead his 2024 campaign and served as chief of staff from the first day of his second term.

She built a reputation as a disciplined, low-profile manager. NPR noted that she was credited with reducing the staff turnover and press leaks that marked Trump's first term. Earlier this year, Wiles was diagnosed with breast cancer, and this fall it was announced that she was cancer-free.

## Who Is Stephen Miller?

Stephen Miller has been one of Trump's closest advisers since the 2016 campaign. Key facts:

* **Current roles:** White House deputy chief of staff and homeland security adviser.
* **Focus:** He is best known as the architect of Trump's hard-line **immigration policies**, from the first term to the current administration.
* **Speechwriter:** He has written many of Trump's major speeches and is known for his combative style.
* **Foreign policy:** According to NPR, he has also been involved in advising on military operations in the Middle East.

As chief of staff, Miller will control who gets time with the president and what information reaches him, making him one of the most powerful people in Washington.

## What Does a White House Chief of Staff Do?

The chief of staff runs the White House staff, manages the president's schedule and acts as a gatekeeper.

David Cohen, a political science professor at the University of Akron who studies the role, told NPR the chief of staff is a "very important gatekeeper of the president's time." Ideally, he said, the chief of staff serves as a neutral broker, but "oftentimes, though, the chief of staff is the last person talking to the president."

## How Democrats Reacted

Democratic leaders strongly criticized the choice.

* **Hakeem Jeffries**, the House Democratic leader who is widely expected to become speaker, called Miller "a dangerous xenophobe and reckless extremist" and urged Trump to fire him.
* **Chuck Schumer**, the Senate Democratic leader, said Trump "learned nothing from his historic defeat" and that "Our Democratic majorities will fight him every step of the way."

## How Republicans See Miller

Miller's supporters see him as one of the most effective figures in Trump's circle. Earlier this year, when a few Republicans questioned his influence, a group of GOP senators rushed to defend him. Sen. Lindsey Graham said Miller would be "proven right" on immigration, and Sen. Tom Cotton said he highly valued Miller's counsel.

Supporters credit Miller with delivering on Trump's border promises, which remain popular with the president's base. Critics, including some Republicans, have argued that aggressive immigration enforcement hurt the party with swing voters. NPR reported that data from this week's election suggest voters backed Democrats in part because of those enforcement tactics.

## What Happens Next

Miller officially starts as chief of staff on Monday. The big questions now are who will take over his immigration and homeland security portfolio, how the White House will work with a Democratic-controlled Congress, and whether more staff changes are coming after the midterms.

## Frequently Asked Questions

**Who is the new White House chief of staff?**
Stephen Miller, who replaces Susie Wiles starting Monday, November 9, 2026.

**Why did Susie Wiles leave?**
Trump did not give a detailed reason. Media reports said he was frustrated after the midterm elections. Wiles will continue working on political operations.

**What was Stephen Miller's previous job?**
He served as White House deputy chief of staff and homeland security adviser."""
},
{
"title": "Tesla Cybertruck Discontinued: Production Ends in 2027",
"slug": "tesla-cybertruck-discontinued-production-ends-2027-cybercab",
"seo_description": "Tesla Cybertruck discontinued: Elon Musk says production will wind down in 2027 to build more Cybercabs. Sales, prices and what it means for owners.",
"keywords": "Cybertruck discontinued, Tesla Cybertruck discontinued, Cybertruck production ending, Tesla Cybertruck 2027, Cybercab, Elon Musk Cybertruck, Cybertruck sales, Cybertruck resale value, Giga Texas",
"image_prompt": "angular stainless steel electric pickup truck silhouette in an empty factory hall, cold industrial lighting, no logos",
"content": """The **Tesla Cybertruck** is being **discontinued**. Elon Musk announced on X on November 6, 2026, that Tesla will wind down Cybertruck production at its Texas factory next year, in order to free up space to build more **Cybercab** robotaxis.

"Cybertruck discontinued" jumped on Google Trends as owners, fans and critics reacted to the end of one of the most talked-about vehicles of the decade. Here's what we know about why Tesla is ending the Cybertruck, how sales performed and what it means if you own one.

## When Will Cybertruck Production End?

Musk said production will end "next year." According to Electrek, the wind-down is expected around **mid-2027**, about three and a half years after the first deliveries in late 2023.

Tesla has not announced an exact final production date or how long remaining inventory will be sold.

## Why Is Tesla Ending the Cybertruck?

Musk's stated reason is simple: Tesla wants the factory space for the **Cybercab**, its two-seat robotaxi with no steering wheel or pedals.

The decision fits Tesla's broader shift toward artificial intelligence and robotics:

* **Model S and Model X:** Production ended earlier in 2026, and the Fremont factory space was repurposed for **Optimus** humanoid robots.
* **Cybertruck:** Now set to end in 2027 to make room for Cybercabs.
* **Robotaxi rollout:** According to TechCrunch, Cybercabs have operated on Austin streets for about two months, and Tesla plans to expand to Dallas. Tesla also runs Model Y robotaxis in several cities in Texas and Florida.

## Cybertruck Sales: Far Below Expectations

The bigger story is that the Cybertruck never came close to its sales goals.

* **The plan:** When deliveries began in late 2023, Musk predicted about **250,000 sales per year**, and the production line was built for that volume.
* **The reality:** Electrek estimates current sales at about **30,000 per year**, roughly 12% of the original plan, and about **70,000 trucks delivered** in three years.
* **Falling sales:** Cox Automotive estimated U.S. sales of 3,519 in the first quarter of 2026 and 3,744 in the second quarter, compared with 14,416 in the third quarter of 2024.
* **Company buyers:** S&P Global Mobility data showed SpaceX bought 1,279 Cybertrucks in the fourth quarter of 2025.

## Promises vs. Reality

At its 2019 reveal, Tesla said the Cybertruck would start **under $40,000** and offer up to **500 miles of range**. It delivered neither.

* The launch was delayed about two years, partly because of COVID-19.
* At launch in late 2023, the base price was about $60,000, and the top range was more than 100 miles lower than promised.
* A cheaper rear-wheel-drive version arrived in 2025 and was dropped months later.
* After a $5,000 price increase in August 2026, the dual-motor trim starts at **$74,990**.

The truck also faced challenges beyond price. Its polarizing stainless-steel design did not appeal to many buyers, and Musk's political activity made it a target for protests in 2024 and 2025. Tesla also canceled Cybertruck sales in Australia and New Zealand in October 2026, and it was never sold in Europe.

## What It Means for Cybertruck Owners

If you own a Cybertruck, you probably have questions. Musk's post did not address parts, service or warranty coverage for existing owners. However, automakers in the U.S. generally continue to provide parts and service for discontinued vehicles for years, and existing warranties remain in effect.

Practical tips for owners:

* **Keep your warranty paperwork** and service records organized.
* **Watch for official Tesla updates** about service and parts support.
* **Software updates:** Tesla vehicles receive over-the-air updates, so watch for any announcements on future support.

## Will Cybertruck Resale Values Go Up or Down?

This is one of the most-asked questions. Some buyers expect a discontinued vehicle to become a collector's item, especially one as distinctive as the Cybertruck. Others worry that uncertainty about long-term support could push prices down. Used EV marketplaces have already started analyzing the question, but it's too early to say how prices will move.

## What Is the Tesla Cybercab?

The Cybercab is a small, two-seat electric robotaxi designed to drive itself, with no steering wheel or pedals. Tesla built a separate production line for it, using what it calls an "unboxed" manufacturing process. According to Electrek, about 463 Cybercabs were registered in Texas as of late October 2026. Musk sees robotaxis as Tesla's biggest future business, which explains why the company is willing to give up a vehicle as famous as the Cybertruck to make room for it.

## Will There Be a Cybertruck 2?

Tesla has given no sign of a successor. Its focus is now on autonomous vehicles and robots rather than new consumer pickup trucks.

## Frequently Asked Questions

**Is the Tesla Cybertruck discontinued?**
Yes. Elon Musk said Tesla will wind down Cybertruck production next year, expected around mid-2027.

**Why is Tesla discontinuing the Cybertruck?**
To use the factory space for more Cybercab robotaxis. Sales have also been far below Tesla's original expectations.

**How many Cybertrucks has Tesla sold?**
Electrek estimates about 70,000 have been delivered since late 2023."""
},
{
"title": "Polar Vortex November 2026: Heavy Snow Map and Winter Forecast",
"slug": "polar-vortex-november-2026-heavy-snow-map-winter-forecast",
"seo_description": "Polar vortex November 2026: a rare early disruption could send Arctic air south. See the CPC heavy snow map for Nov. 13-15 and what it means for winter.",
"keywords": "polar vortex November 2026, polar vortex, Climate Prediction Center heavy snow map, sudden stratospheric warming, winter forecast 2026, Arctic blast, Sierra Nevada snow, El Nino winter 2026-27, cold snap",
"image_prompt": "snow-covered mountain highway with pine trees during a heavy snowstorm, blue winter light, no cars",
"content": """Winter weather is starting to make headlines across the United States. Searches for **"polar vortex November 2026"** and the **"Climate Prediction Center heavy snow map"** jumped this week after forecasters flagged a rare early disruption of the polar vortex and a moderate risk of heavy snow in the West.

Here's what the polar vortex is, what the latest NOAA maps show, and what it could mean for your weather later this month and into December.

## What Is the Polar Vortex?

The **polar vortex** is a band of strong westerly winds about 10 to 30 miles above the North Pole, in a layer of the atmosphere called the stratosphere. In winter, it normally works like a fence, keeping the coldest air locked near the Arctic.

When the vortex weakens or gets disrupted, that cold Arctic air can break away and move south into North America, Europe or Asia. According to NOAA, in some cases it can push cold air as far south as Florida.

## The Rare November Disruption

The NWS Climate Prediction Center (CPC) said forecast models "indicate the potential for a stratospheric polar vortex disruption." That could develop into a **sudden stratospheric warming (SSW)**, which the CPC called "very rare" for November.

* **What happens:** During an SSW, the air high above the Arctic heats up quickly, sometimes by 40 to 50 degrees Celsius within days, and the polar winds weaken or even reverse.
* **The data:** According to The Watchers, polar vortex winds at 60 degrees north dropped from about 22 to about 5 meters per second in eight days.
* **How long it lasts:** Effects of an SSW can last up to two months.

## When Could the Cold Arrive?

The impacts are not immediate. Surface weather usually changes weeks after a stratospheric disruption, so **late November and December** are the periods to watch.

The CPC said there is "some potential for troughing to settle over the Southeast by the end of the month," which could bring cooler conditions to parts of the Southeast. But forecasters stress that the exact placement and strength of any cold pattern remain uncertain.

**Important:** A polar vortex disruption does not guarantee a major cold snap or a widespread Arctic outbreak. It increases the chances, but it is not a certainty.

## CPC Heavy Snow Map: November 13-15

Separately, the CPC's week-two hazards outlook, released November 5, shows a **moderate risk of heavy snow** from Friday, November 13, through Sunday, November 15.

* **Where:** The mountains of southern Oregon and California's Sierra Nevada and Klamath Mountains.
* **Rain at lower elevations:** Snow levels are expected to stay high, so most precipitation at lower elevations should fall as rain.
* **Heavy precipitation:** Extends north into Washington.
* **High winds:** A moderate risk along the coasts of Washington, Oregon and California from November 13 to 15.
* **More mountain snow:** A slight risk of heavy high-elevation snow through November 17 for the Cascades, the Central and Northern Rockies and parts of the Great Basin.

According to Autoblog, CPC forecaster Thomas Collow said the chance of three-day snow totals topping six inches had declined since the previous outlook.

## Travel Impact

Drivers heading over the Sierra should be ready. **Interstate 80 over Donner Summit** and **U.S. 50 over Echo Summit** are in the heavy snow zone, so chain controls are likely near the summits from November 13 to 15. Check Caltrans road conditions before you leave and carry chains.

## What About the Rest of the Country?

For now, most of the Lower 48 leans warmer than normal. Parts of the Middle Mississippi Valley, Ohio Valley and Mid-Atlantic may see near-freezing nights, but first freezes are running two to three weeks later than usual in some areas.

## El Niño and the Winter Forecast

The bigger winter picture is shaped by **El Niño**. The CPC expects El Niño to remain the dominant climate influence this winter. In a typical El Niño winter, the southern U.S. tends to be wetter and the northern tier milder than normal. The polar vortex disruption is the wild card that could upend that pattern, especially in the eastern U.S.

## How to Prepare for a Cold Snap

* **Check your heating system** and replace furnace filters.
* **Protect pipes** by insulating those in unheated spaces.
* **Build a winter car kit** with blankets, a flashlight, an ice scraper and snacks.
* **Follow local forecasts** from the National Weather Service for updates.

## Frequently Asked Questions

**Is a polar vortex coming in November 2026?**
Forecasters are watching a rare early disruption. Any cold impacts would most likely arrive in late November or December, but a major cold snap is not guaranteed.

**Where will it snow heavily next week?**
The CPC shows a moderate risk of heavy snow in southern Oregon and California's Sierra Nevada and Klamath Mountains from November 13 to 15.

**What is a sudden stratospheric warming?**
A rapid warming of the air high above the Arctic that weakens the polar vortex and can send cold air south weeks later."""
},
{
"title": "Blue Angels Remove Pilot Maj. Scott Laux Before Homecoming Airshow",
"slug": "blue-angels-remove-pilot-scott-laux-homecoming-airshow-pensacola",
"seo_description": "The Blue Angels removed No. 6 pilot Maj. Scott Laux for failing to uphold squadron standards, days before the Pensacola homecoming airshow. What we know.",
"keywords": "Scott Laux, Blue Angels pilot removed, Scott Laux Blue Angels, Blue Angels homecoming airshow 2026, Blue Angels No. 6, NAS Pensacola airshow, Navy Flight Demonstration Squadron, Blue Angels news",
"image_prompt": "formation of blue and yellow jets flying over the ocean coastline at sunset, dramatic sky, distant view, no markings",
"content": """The **Blue Angels** have removed one of their pilots just days before the team's biggest show of the year. The Navy announced on November 6, 2026, that **Marine Corps Maj. Scott Laux**, the squadron's No. 6 opposing solo pilot, was removed for "failing to uphold the standards expected of members of the Navy Flight Demonstration Squadron."

Searches for "Scott Laux" and "Blue Angels pilot removed" surged after the news broke, as fans tried to find out what happened ahead of the **homecoming airshow** in Pensacola.

## What the Navy Said

The statement came from Naval Air Training Command (CNATRA) public affairs, which oversees the Blue Angels. It said Laux was removed for failing to uphold the standards expected of squadron members.

So far, officials have not said:

* When the decision was made.
* Whether it is connected to a disciplinary matter or an investigation.
* Who will fly the No. 6 position in the future.

Laux's photo and biography were also removed from the Blue Angels' official website.

## Who Is Scott Laux?

Before joining the Blue Angels, Laux built a long career as a Marine Corps fighter pilot.

* **Hometown:** Chantilly, Virginia.
* **Education:** Graduated from the U.S. Naval Academy in 2012 with a degree in Chinese.
* **Flight career:** Earned his wings in 2015 and flew the F/A-18 Hornet with Marine fighter-attack squadrons, including at Marine Corps Air Station Miramar and on deployment aboard the aircraft carrier USS Nimitz.
* **Experience:** His team biography listed more than 1,300 flight hours and 169 carrier landings.

## His Time With the Blue Angels

Laux's path through the squadron was typical of how the team develops its pilots:

* **2024:** Joined the Blue Angels as a pilot.
* **2025:** Served as the team's narrator.
* **2026:** Moved into the No. 6 jet, the **opposing solo** position, which flies many of the show's most dramatic head-on passes.

He also flew during this fall's San Francisco Fleet Week performances.

## The Homecoming Airshow

The removal came right before the **Blue Angels Homecoming Air Show** at **Naval Air Station Pensacola**, Florida, held November 6 and 7, 2026. The homecoming show is the season's final performance and a major event for the team's home base.

According to the Pensacola News Journal, which first reported the removal, the team flew the first day of the show with only **five jets** instead of the usual six. A six-jet demonstration depends on precise timing between the diamond formation and the two solo pilots, so losing one jet changes the routine.

## What Does the No. 6 Pilot Do?

The Blue Angels fly six jets in their demonstration. Jets No. 1 through 4 fly in the famous tight **diamond formation**, led by the commanding officer in the No. 1 jet. Jets No. 5 and No. 6 are the **solo pilots**. The No. 5 lead solo and the No. 6 opposing solo perform high-speed maneuvers, including passes that appear to come head-on toward each other at show center. These are some of the most demanding and crowd-pleasing parts of any Blue Angels show.

The team, founded in 1946 and based at NAS Pensacola, flies the Boeing F/A-18 Super Hornet.

## How Rare Is This?

Blue Angels pilots are selected from among the best aviators in the Navy and Marine Corps, and the squadron is known for strict standards both in the air and on the ground. Removals in the middle of a season are uncommon, which is why this one has drawn so much attention. The team has replaced members for performance or conduct concerns in the past, but the Navy rarely shares details.

## What Happens Next for the Blue Angels

With the 2026 season ending in Pensacola, the team now moves into its winter training period. New team members typically rotate in each year, and the squadron trains over the winter before the next season begins in the spring. The Navy has not said who will fill the No. 6 slot for 2027.

## Where to Find Updates

Because the Navy has given only a brief statement, more details may come out in the coming days. The best sources for official information are the Blue Angels' website and the Navy's public affairs offices. Be careful with rumors on social media, since no official explanation beyond the standards statement has been released.

## Frequently Asked Questions

**Why was Scott Laux removed from the Blue Angels?**
The Navy said he was removed for "failing to uphold the standards expected" of squadron members. It has not shared further details.

**What position did Scott Laux fly?**
He flew the No. 6 jet, the opposing solo, during the 2026 season.

**Did the Blue Angels still perform at the homecoming airshow?**
Yes. The team flew the first day of the Pensacola homecoming show with five jets."""
},
]


def image_url(prompt, seed):
    full = prompt + ", ultra realistic, 4k, editorial photography, dramatic lighting, no text, no faces, no logos"
    return f"https://image.pollinations.ai/prompt/{urllib.parse.quote(full)}?width=1200&height=675&seed={seed}&nologo=true"


def seed_database():
    conn = sqlite3.connect("news.db")
    cur = conn.cursor()
    published = "2026-11-07 13:30:00"  # UTC (16:30 Istanbul)
    for i, a in enumerate(ARTICLES_H):
        wc = len(a["content"].split())
        assert 800 <= wc <= 1150, f"{a['slug']}: {wc} words"
        img = image_url(a["image_prompt"], 268000 + i)
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
