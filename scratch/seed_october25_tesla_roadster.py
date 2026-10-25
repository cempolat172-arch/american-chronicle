import sqlite3
import datetime
import urllib.parse

# Trend: Tesla Roadster "flying car" reveal (Oct 15, 2026) back in the spotlight
# after Ferrari CEO Benedetto Vigna rated the launch "10 out of 10" (Oct 20, 2026).
# Sources: Edmunds, Fox Business (Reuters), INDmoney, Motor1.

SLUG = "tesla-roadster-flying-car-price-specs-release-date-ferrari-ceo-10-out-of-10-2026"

IMAGE_PROMPT = (
    "futuristic low wedge shaped electric hypercar with scissor doors hovering above desert test site "
    "at dusk, rocket thruster glow, dust cloud, ultra realistic, 4k, editorial photography, "
    "dramatic lighting, no text, no faces, no logos"
)
IMAGE_URL = (
    "https://image.pollinations.ai/prompt/" + urllib.parse.quote(IMAGE_PROMPT)
    + "?width=800&height=500&seed=251026&nologo=true"
)

ARTICLE = {
    "title": "TESLA ROADSTER TAKES FLIGHT: Price, Specs, 2028 Release Date and Why Ferrari's CEO Gave It a 10 Out of 10",
    "slug": SLUG,
    "seo_description": "Tesla Roadster explained: 0-60 in 0.81 sec, 620-mile range, $50K and $250K reservations, flying Thrust model, 2028 production and Ferrari CEO's praise.",
    "is_bizarre": 0,
    "is_breaking": 1,
    "image_url": IMAGE_URL,
    "content": """Ten days after Elon Musk rolled a long, low, scissor-doored electric hypercar onto a SpaceX test site in Texas and sent it into the air, the **Tesla Roadster** is still one of the most searched car names in America. The reason it refuses to fade is simple: the reveal was not just another fast EV launch. Tesla claimed a 0-60 mph time under one second, a 620-mile range, and a version that can lift off the ground with cold-gas thrusters. Then, this week, the internet got an unexpected twist when Ferrari CEO Benedetto Vigna publicly rated the launch "10 out of 10."

Searches for **Tesla Roadster price**, **Tesla Roadster flying car**, **Tesla Roadster release date**, and **Tesla Roadster specs** have surged again as buyers, investors, and car fans try to separate the spectacle from the facts. Here is everything we actually know, what remains unproven, and what it means for the supercar world.

## What Happened at the Tesla Roadster Reveal?

Tesla unveiled the production-intent Roadster on Thursday, October 15, 2026, at SpaceX's facility in McGregor, Texas. The demonstration included stunts and airborne maneuvers, with the car reportedly lifting off the ground and performing a midair flip using thruster hardware developed alongside SpaceX.

The design looks very different from the concept Tesla first showed in 2017. The new car is a long, low wedge with a large rear wing and scissor doors, a shape Edmunds compared to 1980s Lamborghinis. Inside, it has white seats, a large touchscreen that handles most controls, and a yoke-style steering wheel.

## Tesla Roadster Specs: The Claimed Numbers

Tesla shared headline figures but very few mechanical details. Battery size, for example, was not disclosed. Here is what the company did claim:

* **0-60 mph:** Initially quoted at 1.0 second, then a video showed a 0.81-second run, which would make it the quickest-accelerating road car ever shown.
* **Top speed:** More than 230 mph, with Musk saying he wants the final car to reach "half the speed of sound," roughly 383 mph.
* **Range:** Up to 620 miles on a charge, which would beat nearly every EV on sale today.
* **Cornering:** More than 2 g of lateral grip, aided by a fan system that Musk says can "suck the car down at low speed."
* **Active aerodynamics:** Selectable "high-downforce" and "low-drag" modes.
* **Drive-by-wire controls:** Electronic steering, braking, and throttle.

For context, the fastest production EVs today, such as the Rimac Nevera, run 0-60 in under two seconds. If Tesla delivers anything close to these claims, the Roadster would rewrite the performance record books.

## Can the Tesla Roadster Really Fly?

This is the question driving most of the search traffic. Tesla describes a "multi-mode suction system" plus perimeter **cold-gas thrusters** that support forward and upward acceleration and rotation. Cold-gas thrusters push pressurized gas through nozzles and do not burn fuel, a technology common in spacecraft maneuvering.

However, the details matter. According to Edmunds, which attended the event, the flying demonstration was **remotely controlled with no one inside**, and the car bounced on landing as if it had no suspension. Tesla's own booking page restricts the full flight feature to a special configuration and notes it is not available in every region. No aviation regulator has publicly signed off on a street car that flies, and where such a feature could legally be used remains an open question.

In other words, the Roadster has shown that it can hop. Whether owners will ever "fly" on a public road is a very different matter.

## Tesla Roadster Price and Versions Explained

Tesla opened reservations for three versions. It has not announced a final purchase price, so these figures are reservation payments rather than sticker prices:

* **Roadster Performance:** The road-legal model with no thrusters. $5,000 deposit plus $45,000 due within 10 days, for a total of **$50,000**.
* **Roadster Thrust:** A limited run fitted with thrusters. $5,000 deposit plus $245,000 within 10 days, totaling **$250,000**, limited to one per customer and subject to local laws.
* **Roadster Rocket:** An invitation-only, single-seat version with a "full flight system."

Buyers should read the fine print. Under Tesla's standard agreement, a reservation can be cancelled and refunded before a purchase agreement is signed, but Tesla pays no interest on the money and does not hold it in a separate escrow account. The booking page also states that "refunds for modifications will not be issued."

## Tesla Roadster Release Date: When Does Production Start?

Musk says production will begin in **2028**, adding that the timeline is "actually, for real." Skeptics have a reason to be cautious: when the first Roadster prototype appeared in 2017, Tesla promised deliveries in 2020. That date passed without a single customer car. A 2028 start would mean a wait of roughly two more years from today, and more for the thruster-equipped models.

## Why Ferrari's CEO Gave It a 10 Out of 10

The story found a second wind on Tuesday, October 20, when Ferrari CEO Benedetto Vigna spoke at an auto conference organized by the Italian magazine Quattroruote. He rated the launch 10 out of 10 for technology and 10 out of 10 for presentation.

"It certainly shows that also in the automotive world there's still a lot to be done. We have to keep dreaming," Vigna said. "As a European, thank you for showing us how that, even in an old world, you can still innovate and dare."

The praise stood out because Ferrari is in the middle of its own electric transition. The company unveiled its first fully electric car, the **Ferrari Luce**, in May, developed with former Apple design chief Jony Ive's LoveFrom studio. Vigna added that Ferrari "wouldn't have done what we did" if it had worked alone, a nod to the growing role of outside tech partners in supercar design.

### What the Roadster Means for the Supercar Market

The Roadster arrives at a moment when legacy automakers are cutting costs and rethinking EV plans. A $50,000 reservation for a car claiming hypercar numbers puts pressure on brands that charge seven figures for similar performance. At the same time, the gap between a stage demo and a car that passes safety rules, crash tests, and emissions-free road certification is enormous.

## How Investors Reacted

Tesla shares rose roughly 5% in premarket trading the day after the reveal. Analysts were quick to caution, though, that Roadster revenue is years away and the event has not yet changed the company's earnings outlook. Reservation money counts as a customer deposit on Tesla's books, not as earned revenue, until cars are actually delivered.

## Frequently Asked Questions About the Tesla Roadster

**How much does the Tesla Roadster cost?**
Tesla has not announced a final price. Reservations total $50,000 for the Performance model and $250,000 for the Thrust model. The Rocket version is invite-only.

**When will the Tesla Roadster be released?**
Elon Musk says production is planned for 2028.

**Is the Tesla Roadster a real flying car?**
Only the thruster-equipped versions have any lift capability, and the public demo was remotely piloted with no driver inside. The standard Performance model does not fly.

**How fast is the new Tesla Roadster?**
Tesla claims 0-60 mph in as little as 0.81 seconds and a top speed above 230 mph. These figures have not been independently tested.

**What is the Tesla Roadster's range?**
Tesla claims up to 620 miles per charge.

## The Bottom Line

The new Tesla Roadster is the most talked-about car in America right now because it promises things no road car has ever done. The design is striking, the numbers are staggering, and even Ferrari's boss is applauding. But every headline claim, from the 0.81-second sprint to the flight system, is still unverified, and the delivery date is two years out on a car that has already missed one deadline. For now, the Roadster is the most exciting reservation in the auto world, and the most important one to read the fine print on."""
}


def word_count(text):
    return len(text.split())


def seed_database():
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()
    now = datetime.datetime(2026, 10, 25, 16, 10, 0)

    art = ARTICLE
    wc = word_count(art["content"])
    assert wc >= 1000, f"Article too short: {wc} words"
    print(f"'{art['title'][:50]}...' -> {wc} words")

    cursor.execute("SELECT id FROM news_articles WHERE slug = ?", (art["slug"],))
    existing = cursor.fetchone()
    if existing:
        cursor.execute(
            """UPDATE news_articles SET title=?, content=?, seo_description=?, is_bizarre=?,
               is_breaking=?, published_at=?, image_url=? WHERE id=?""",
            (art["title"], art["content"], art["seo_description"], art["is_bizarre"],
             art["is_breaking"], now, art["image_url"], existing[0]),
        )
        print(f"Updated article ID {existing[0]}")
    else:
        orig_url = f"https://trends.google.com/trends/explore?date=now%207-d&geo=US&q=tesla%20roadster"
        cursor.execute(
            """INSERT INTO news_articles (title, slug, content, original_url, seo_description,
               is_bizarre, is_breaking, published_at, created_at, image_url)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (art["title"], art["slug"], art["content"], orig_url, art["seo_description"],
             art["is_bizarre"], art["is_breaking"], now, now, art["image_url"]),
        )
        print(f"Inserted new article: {art['slug']}")

    conn.commit()
    conn.close()


if __name__ == "__main__":
    seed_database()
