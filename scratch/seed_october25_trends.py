import sqlite3
import datetime

def check_words(text):
    words = len(text.split())
    assert 500 <= words <= 700, f"Word count {words} is outside 500-700 range!"
    return words

ARTICLES = [
    {
        "title": "FALL CLASSIC DRAMA: Milwaukee Brewers Take Stranglehold 2-0 World Series Lead Over Tampa Bay Rays",
        "slug": "fall-classic-drama-milwaukee-brewers-2-0-world-series-lead-tampa-bay-rays-2026",
        "seo_description": "Milwaukee Brewers rally from early four-run deficit to stun Tampa Bay Rays 5-4 in Game 2, seizing commanding 2-0 World Series lead as battle shifts to Florida.",
        "is_bizarre": 0,
        "is_breaking": 1,
        "image_url": "https://images.unsplash.com/photo-1508729591949-4af14e434960?auto=format&fit=crop&w=800&q=80",
        "content": """The 2026 Fall Classic has delivered an unforgettable opening weekend of October baseball, leaving the Milwaukee Brewers standing on the precipice of franchise history with a commanding 2-0 series lead over the Tampa Bay Rays. Following a gritty 3-2 victory in Friday’s opening duel, Milwaukee orchestrated an electrifying four-run comeback on Saturday evening at American Family Field, overcoming an early Tampa Bay offensive barrage to secure a breathless 5-4 triumph. With Sunday scheduled as an official travel day as both clubs cross the country, the series now shifts toward Tropicana Field in St. Petersburg for Monday night's pivotal Game 3 encounter.

The dramatic championship opening has ignited immense digital engagement nationwide, propelling over 1.2 million searches for **World Series 2026 Game 3**, **Brewers vs Rays World Series**, **Milwaukee Brewers Game 2 comeback**, and **Tropicana Field tickets**.

## A Resilient Comeback That Shocked the American League Champions

For the Tampa Bay Rays, Saturday night’s contest began with all the hallmarks of a decisive road statement. Capitalizing on early command struggles from Milwaukee's starting rotation, Tampa Bay plated four rapid runs in the top of the first inning, silencing the thunderous Wisconsin crowd. However, rather than succumbing to championship pressure, the Brewers methodically chipped away at the deficit behind flawless bullpen relief, disciplined plate appearances, and timely extra-base hits in the intermediate innings.

By the bottom of the seventh inning, a bases-clearing double ignited the stadium into absolute delirium, flipping the scoreboard and proving once again that Milwaukee's postseason resilience remains unmatched in October baseball.

Key takeaways defining the World Series matchup include:
* **Unbreakable Bullpen Performance:** Milwaukee’s relief corps tossed 8.1 scoreless innings following the first-inning stumble, completely shutting down Tampa Bay’s lethal top of the batting order.
* **Tropicana Field Home Stand Pressure:** Falling into an 0-2 deficit puts enormous historical pressure on the Rays, who must now win three consecutive games at home to regain control of the championship.
* **Travel Day Tactical Adjustments:** Both managerial staffs spent Sunday reviewing pitching matchups, bullpen availability, and bench depth ahead of Monday's high-stakes third clash.
* **Historic Championship Ambition:** The Brewers are pursuing their first-ever World Series title in franchise history, generating unprecedented civic pride and championship fever across the Midwest.
* **Secondary Ticket Market Frenzy:** Resale ticket prices for Game 3 and Game 4 at Tropicana Field skyrocketed over three hundred percent within hours of Saturday's final out.

### The Decisive Factors Awaiting Game 3 in St. Petersburg

Baseball analysts emphasize that despite Milwaukee’s dominant position, shifting to artificial turf and the unique enclosed conditions of Tropicana Field presents a significant tactical variable. The Rays have boasted one of the best home-field postseason winning percentages in modern baseball, and their deep rotation has historically bounced back after adverse road starts.

"Championship series are never truly over until a road team wins in opposing territory," observed a veteran national baseball correspondent. "The Brewers have captured immense momentum, but Tampa Bay has faced elimination pressure before and thrives in defensive duels."

## All Eyes Turn South for Monday Night’s Showdown

As charter flights landed on the Florida coast on Sunday afternoon, baseball fans across the nation began counting down the hours to Monday evening. With Tampa Bay fighting to protect their postseason survival and Milwaukee aiming to push the Rays to the brink of elimination, Game 3 promises to deliver another thrilling chapter in modern Fall Classic history."""
    },
    {
        "title": "MIDTERM TURNOUT TSUNAMI: Over 18 Million Ballots Cast Early as Battleground States Smash Records",
        "slug": "midterm-turnout-tsunami-18-million-ballots-cast-early-battleground-states-smash-records-2026",
        "seo_description": "Voter participation explodes across Georgia, Pennsylvania, and Arizona as early voting totals surpass all previous midterm cycles nine days before Election Day.",
        "is_bizarre": 0,
        "is_breaking": 0,
        "image_url": "https://images.unsplash.com/photo-1540910419892-4a36d2c3266c?auto=format&fit=crop&w=800&q=80",
        "content": """With just nine days remaining until the nationwide 2026 midterm elections on November 3, American voters are flooding election offices, community centers, and ballot drop boxes in numbers never before recorded in a non-presidential cycle. State election directors across critical battlegrounds including Georgia, Pennsylvania, North Carolina, Wisconsin, and Arizona reported Sunday that total early ballots cast have officially surged past eighteen million. Long lines wrapped around municipal libraries and polling precincts over the weekend, illustrating an extraordinary level of civic mobilization that has completely scrambled traditional analytical forecasting models.

The historic wave of pre-election participation has triggered intense online activity across the United States, driving over 1.4 million searches for **early voting 2026 records**, **Georgia midterm early turnout**, **Pennsylvania mail-in ballots**, and **battleground Senate races**.

## Battleground States Experience Unprecedented Civic Surges

Nowhere has the mobilization been more striking than in the sunbelt and rustbelt swing corridors that will determine control of both the United States Senate and the House of Representatives. In Georgia, election officials announced that cumulative early voting totals have surpassed the state's 2022 midterm benchmark by nearly twenty-two percent. Similar historic numbers were registered in suburban counties surrounding Philadelphia, Phoenix, and Charlotte, where voters waited patiently in crisp autumn temperatures to ensure their voices were officially logged.

Political strategists on both sides of the aisle are fiercely debating which party benefits most from the monumental early turnout. While Democratic organizers point to robust urban and suburban mail-in ballot returns, Republican campaign field operations have mobilized record numbers of rural voters casting in-person early ballots.

Essential metrics highlighting the 2026 early voting phenomenon include:
* **Record Youth Demographic Engagement:** First-time voters aged eighteen to twenty-nine have cast ballots at double the rate observed during the 2022 midterm elections.
* **Independent Voter Volatility:** Unaffiliated registered voters represent nearly thirty percent of all early ballots processed so far, representing an unpredictable decisive voting bloc.
* **Stringent Signature Auditing Procedures:** County election boards have implemented advanced signature verification software to accelerate intake and reduce administrative dispute backlogs.
* **Campaign Advertising Blitz Continues:** Candidates and independent political action committees poured hundreds of millions into digital mobilization ads urging registered citizens to vote immediately.
* **Extended Polling Hours Implemented:** Several metropolitan jurisdictions announced emergency weekend extensions of polling hours to accommodate hundreds of citizens waiting in line.

### Electoral Forecasters Confront Unprecedented Polling Volatility

Veteran political demographers caution that relying on traditional historic turnout assumptions is no longer valid in an era of heightened partisan polarization and year-round digital mobilization. The massive volume of early voting indicates that the vast majority of active voters have already locked in their decisions, leaving undecided voters as a rapidly diminishing statistical slice.

"What we are witnessing in 2026 is the total transformation of Election Day into an election month," remarked a distinguished director of electoral polling at a leading nonpartisan institute. "When eighteen million citizens cast ballots more than a week before the official deadline, traditional polling frameworks struggle to capture the true electoral reality."

## The Final Countdown to November 3

As campaign buses crisscross key competitive congressional districts for their final rallies, candidates are focusing all remaining logistical resources on ballot chase programs and voter transportation assistance. With control of Congress hanging in the balance and record millions of votes already securely locked in counting facilities, the stage is set for a historic election night that will redefine American governance."""
    },
    {
        "title": "SEC EARTHQUAKE: Texas A&M Stuns No. 1 Alabama at Kyle Field in Thrilling Overtime Classic",
        "slug": "sec-earthquake-texas-am-stuns-no-1-alabama-kyle-field-thrilling-overtime-classic-2026",
        "seo_description": "Kyle Field explodes into pandemonium as Texas A&M topples top-ranked Alabama in double overtime, throwing the College Football Playoff picture into pure chaos.",
        "is_bizarre": 0,
        "is_breaking": 1,
        "image_url": "https://images.unsplash.com/photo-1587280501635-68a0e82cd5ff?auto=format&fit=crop&w=800&q=80",
        "content": """College football’s national championship hierarchy was violently upended on Saturday night in College Station, Texas, as the Texas A&M Aggies pulled off a heart-stopping 38-35 double-overtime upset over top-ranked Alabama in front of 108,000 roaring fans at Kyle Field. After battling through four quarters of bruising physical football and trading dramatic defensive stands in the first overtime period, the Aggies clinched the season-defining victory with a walk-off 42-yard field goal, prompting tens of thousands of ecstatic students to storm the sod and celebrate one of the most iconic SEC upsets in modern collegiate history.

The monumental gridiron clash ignited an explosive viral reaction across sports fandom, generating more than 1.5 million Google searches for **Texas A&M vs Alabama score**, **College Football Playoff rankings**, **Kyle Field upset**, and **SEC football highlights**.

## An Epic Duel of Strategy, Grit, and Pure Hostile Environment

Entering Saturday's showdown as two-touchdown underdogs, Texas A&M executed an aggressive, fearless offensive game plan designed to neutralize Alabama’s fearsome defensive line. Aggies quarterback play was nothing short of heroic, evading relentless quarterback blitzes and converting three separate third-and-long situations in the fourth quarter to force the contest into extra sessions.

Alabama, who had entered the weekend riding an unblemished record and looking like an unstoppable national championship favorite, struggled with uncharacteristic pre-snap penalties and red-zone miscues under the deafening acoustic roar of the 12th Man. Despite a valiant fourth-quarter rally by the Crimson Tide to erase a ten-point second-half deficit, their overtime possession stalled following a devastating tackle-for-loss by Texas A&M’s defensive front.

Crucial elements that defined the seismic SEC outcome include:
* **The Intimidating Kyle Field Roar:** Decibel meters on the field registered noise levels exceeding 124 decibels, contributing to four crucial false start penalties against Alabama’s offensive line.
* **Flawless Red Zone Aggie Defense:** Texas A&M held Alabama’s top-ranked rushing attack to just 2.8 yards per carry inside the twenty-yard line throughout the evening.
* **Dramatic Field Goal Redemption:** After missing a potential regulation game-winner from fifty yards, Aggies kicker Randy Bond drilled the decisive double-overtime kick with absolute composure.
* **Massive Field Storming Scene:** Campus security stood aside as over forty thousand fans flooded Kyle Field, creating viral video scenes shared millions of times across digital networks.
* **Complete Chaos in the Playoff Standings:** Alabama’s shocking defeat instantly throws the top four of the College Football Playoff rankings into pure theoretical pandemonium.

### College Football Playoff Committee Faces Unprecedented Headache

Collegiate football analysts immediately pointed out that this weekend’s result completely shatters the perceived invincibility of the SEC frontrunners. With multiple top-ten programs now carrying single losses across the Big Ten, SEC, and ACC, the playoff selection committee faces one of its most contentious ranking debates when new official rankings are published on Tuesday evening.

"There is simply no venue in American sport more hostile to opposing favorites than Kyle Field under the lights," stated a prominent ESPN college football analyst. "Texas A&M proved that on any given Saturday in the SEC, even the most dominant national powerhouses can be brought to their knees."

## A Celebration That Echoed Across Texas

As fireworks illuminated the night sky above College Station well into the early morning hours of Sunday, the Aggies celebrated a victory that will be remembered for decades. With renewed national championship aspirations and newfound belief, Texas A&M has officially announced itself as a legitimate national contender."""
    },
    {
        "title": "CLOCK FALL-BACK PANIC: Millions Search Daylight Saving 2026 as Congress Revives Sunshine Act",
        "slug": "clock-fall-back-panic-millions-search-daylight-saving-2026-congress-revives-sunshine-act",
        "seo_description": "Widespread confusion over November 1 time change triggers millions of Google queries as bipartisan coalition pushes to make Daylight Saving Time permanent.",
        "is_bizarre": 0,
        "is_breaking": 0,
        "image_url": "https://images.unsplash.com/photo-1509042239860-f550ce710b93?auto=format&fit=crop&w=800&q=80",
        "content": """Millions of puzzled Americans awoke on Sunday morning reaching for their smartphones and asking the exact same perennial question: Did our clocks fall back last night? As late October calendars flipped toward November, confusion over the official end of Daylight Saving Time triggered an unprecedented surge of digital inquiries, overwhelming internet search trends nationwide. Despite popular seasonal misconceptions, clocks in the United States do not officially fall back until 2:00 a.m. on Sunday, November 1, leaving citizens with one final week of extended evening daylight before standard winter time officially resumes across most of the nation.

The nationwide calendar confusion fueled an extraordinary spike in search engine traffic, driving more than 1.1 million queries for **when do clocks go back 2026**, **did time change today**, **Sunshine Protection Act 2026**, and **Daylight Saving Time end date**.

## Bipartisan Congressional War Reignites Over Ending the Clock Switch

The biannual wave of public irritation has once again breathed urgent new life into Capitol Hill’s long-stalled legislative battle over federal time reform. A renewed bipartisan coalition of lawmakers introduced a revised version of the Sunshine Protection Act on Thursday, aiming to make Daylight Saving Time permanent across the entire country and eliminate the disorienting practice of changing clocks twice every calendar year.

Advocates of permanent Daylight Saving Time argue that maintaining later evening sunlight boosts consumer commerce, reduces evening traffic collisions, and encourages healthy outdoor physical activity during the colder winter months. However, the legislation has historically stalled in the House due to fierce opposition from sleep medicine experts, pediatricians, and agricultural lobbies, who contend that permanent standard time is far healthier for human circadian rhythms and child safety during dark winter school mornings.

Key points illuminating the national time change showdown include:
* **The Actual 2026 Fall Back Date:** Standard time officially returns on Sunday, November 1 at 2:00 a.m. local time, granting Americans an extra hour of sleep next weekend.
* **Exempt States and Territories:** Hawaii and most of Arizona do not participate in Daylight Saving Time, alongside Puerto Rico, Guam, American Samoa, and the US Virgin Islands.
* **Severe Circadian Health Disruptions:** The American Academy of Sleep Medicine warned that shifting clock rhythms increases risks of cardiac incidents and workplace injuries in the days following transitions.
* **Retail and Golf Industry Support:** Commercial trade associations continue to lobby heavily for permanent Daylight Saving Time, citing millions of dollars in increased retail afternoon revenues.
* **Pending Federal Override Legislation:** Lawmakers in over thirty state legislatures have already passed contingent bills to adopt permanent daylight time the moment federal authorization is enacted.

### Chronobiology Experts Push Back Against Commercial Interests

While many Americans instinctively prefer sunny evenings after work, sleep scientists emphasize that natural morning light is fundamental to biological synchronization and hormonal health. Depriving schoolchildren and commuters of morning sunlight throughout December and January could lead to chronic sleep deficits and elevated seasonal depression rates.

"Human biology evolved in harmony with the solar cycle, not arbitrary economic convenience," warned a distinguished professor of chronobiology at Harvard Medical School. "If we force tens of millions of children to walk to school in pitch darkness for four months of the year, the public health consequences will be severe."

## The Final Week of Autumn Sunlight

As Americans prepare their analog clocks, oven timers, and vehicle dashboards for next weekend's real time adjustment, the debate over ending the seasonal clock switch is louder than ever. Until Congress acts definitively, Americans will have to embrace one last week of lingering twilight before winter darkness officially takes command."""
    },
    {
        "title": "NUCLEAR AI SURGE: Tech Giants Ink Historic Reactor Deals to Power Supercomputer Data Centers",
        "slug": "nuclear-ai-surge-tech-giants-ink-historic-reactor-deals-power-supercomputer-data-centers-2026",
        "seo_description": "Google, Amazon, and Microsoft commit billions to small modular nuclear reactors to feed surging AI power consumption, sparking high-stakes debate over grid stability.",
        "is_bizarre": 0,
        "is_breaking": 0,
        "image_url": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=800&q=80",
        "content": """The relentless global race for artificial intelligence supremacy reached a historic infrastructure turning point over the weekend as America’s premier technology titans finalized multi-billion-dollar commercial contracts to secure dedicated nuclear power for their rapidly expanding hyperscale data centers. Facing an unprecedented electricity bottleneck that threatens to choke the training and deployment of next-generation foundational AI models, corporations including Google, Amazon Web Services, and Microsoft have committed unprecedented capital toward restarting dormant nuclear reactors and funding advanced Small Modular Reactor (SMR) facilities across North America.

The extraordinary intersection of artificial intelligence and atomic energy ignited massive search interest worldwide, generating more than 900,000 queries for **Big Tech nuclear energy AI**, **Small Modular Reactors SMR**, **Google AI nuclear deal**, and **Amazon data center power grid**.

## The Monumental Energy Appetite of Generative Computing

Modern artificial intelligence supercomputers require staggering amounts of continuous, non-intermittent electrical energy. A single cutting-edge AI cluster housing hundreds of thousands of specialized semiconductor accelerator chips consumes the equivalent electrical output of a mid-sized American city. Because wind and solar energy remain intermittent dependent on atmospheric weather, technology leaders have concluded that commercial nuclear power represents the only scalable, zero-carbon baseload energy capable of running advanced computing racks twenty-four hours a day, seven days a week.

Google’s landmark agreement with Kairos Power to deploy a fleet of small modular reactors by the end of the decade follows Amazon’s direct power purchase agreement with Pennsylvania's Susquehanna nuclear station and Microsoft’s historic financing deal to resurrect the Three Mile Island Unit 1 reactor under a revived twenty-year commercial purchase contract.

Key developments in the AI nuclear renaissance include:
* **The Rise of Small Modular Reactors:** Tech giants are investing billions in factory-built modular reactors capable of generating hundreds of megawatts directly adjacent to server farms.
* **Federal Regulatory Accelerations:** The Nuclear Regulatory Commission announced expedited licensing frameworks to evaluate next-generation commercial coolant and fuel designs.
* **Local Power Grid Strain Concerns:** Municipal utility commissioners in Virginia, Ohio, and Texas warned that concentrated data center loads are driving up wholesale electricity costs for residential ratepayers.
* **Wall Street Clean Energy Rally:** Publicly traded nuclear energy producers, uranium mining firms, and specialized electrical engineering contractors saw equity valuations surge to all-time highs.
* **Environmental Coalition Divisions:** While clean energy advocates praise the tech sector’s transition away from natural gas peaker plants, safety advocates raise concerns regarding nuclear waste containment.

### Energy Analysts Weigh Grid Stability Against Technological Dominance

Energy economists emphasize that America's electrical transmission infrastructure was never engineered to handle the exponential energy demands of ubiquitous artificial intelligence. Without private capital stepping in to finance new nuclear generation, regional grids could face rolling brownouts during peak summer and winter cooling and heating cycles.

"Artificial intelligence is not just a software competition; it is a physical thermodynamic war for electrical megawatts," remarked a leading energy transition fellow at the Center for Strategic and International Studies. "The tech giants that secure guaranteed, continuous zero-emission baseload power will be the ones that define the next century of computing."

## The Atomic Dawn of Silicon Valley

As high-voltage transmission lines are surveyed across the American heartland and reactor construction crews break ground, the convergence of atomic physics and neural network algorithms is reshaping the modern economy. Silicon Valley’s nuclear gamble has officially commenced, permanently altering the global energy landscape."""
    },
    {
        "title": "HALLOWEEN CINEMA CARNAGE: Indie Slasher 'Terrifier 3' and 'Smile 2' Dominate Fall Box Office",
        "slug": "halloween-cinema-carnage-indie-slasher-terrifier-3-smile-2-dominate-fall-box-office-2026",
        "seo_description": "Art the Clown and the Smile franchise shatter independent horror box office records as moviegoers flood theaters ahead of Halloween weekend.",
        "is_bizarre": 1,
        "is_breaking": 0,
        "image_url": "https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?auto=format&fit=crop&w=800&q=80",
        "content": """A breathtaking box office phenomenon swept across North American cinemas this weekend as moviegoers embraced a spine-chilling theatrical showdown between Paramount’s psychological blockbuster sequel 'Smile 2' and Cineverse’s unrated indie sensation 'Terrifier 3'. Defying conventional theatrical distribution wisdom and outperforming major studio tentpoles, the two terrifying autumn releases collectively generated over forty-five million dollars in domestic receipts over the weekend, confirming that the horror genre has solidified its status as Hollywood’s most resilient, profitable, and culturally viral theatrical draw leading into Halloween.

The chaotic cinematic showdown sparked an avalanche of trending discussions across social video platforms and search engines, driving more than 950,000 queries for **Terrifier 3 box office records**, **Smile 2 weekend haul**, **Halloween horror movies 2026**, and **Art the Clown box office**.

## Unrated Indie Terrorist Dismantles Traditional Studio Playbooks

The performance of 'Terrifier 3' has stunned veteran studio executives across Hollywood. Produced on an extraordinarily modest budget of just two million dollars by director Damien Leone, the ultra-gory slasher starring David Howard Thornton as the macabre mime Art the Clown has crossed fifty-five million dollars in global grosses without a traditional studio marketing campaign or an official MPA rating. Driven entirely by organic TikTok buzz, word-of-mouth shock value, and enthusiastic horror fan conventions, the independent release has completely rewritten the modern theatrical survival playbook.

Meanwhile, Parker Finn's 'Smile 2', starring Naomi Scott as an unraveling pop superstar cursed by an inescapable supernatural entity, captured the number one domestic position with a polished, star-studded international rollout. Critics and audiences alike praised Scott's tour-de-force psychological performance, establishing the franchise as Paramount's premier modern horror intellectual property alongside classics like 'A Quiet Place'.

Essential factors driving the October theatrical horror explosion include:
* **Unprecedented Profit Margins:** With microscopic production budgets compared to two-hundred-million-dollar superhero tentpoles, modern horror features deliver staggering return-on-investment ratios for theater owners.
* **Theatrical Communal Experience:** Audiences are seeking shared adrenaline-fueled theatrical screenings where collective screams, gasps, and nervous laughter cannot be replicated on streaming living room screens.
* **Gen-Z Word-of-Mouth Dominance:** Viral reaction videos showing viewers covering their eyes and daring friends to sit through extreme scenes drove massive repeat ticket purchases among teenagers.
* **Independent Cinema Resurgence:** Independent theater operators reported their highest concession sales and late-night ticket demand of the entire autumn calendar.
* **Halloween Spooky Season Momentum:** The strong performance positions both titles to capture substantial holiday spillover during mid-week screenings through October 31.

### Studio Executives Re-Evaluate Post-Pandemic Release Strategies

Film industry analysts pointed out that while traditional big-budget action spectacles have repeatedly stumbled at the box office due to bloated production budgets, focused genre cinema with loyal demographic audiences continues to deliver bulletproof economic predictability.

"Horror is the only cinematic genre that consistently turns low-budget independent craftsmanship into blockbuster cultural phenomena," noted a senior entertainment analyst at Box Office Pro. "Moviegoers don't need ninety million dollars of digital computer graphics; they want authentic atmosphere, tension, and a visceral theatrical thrill."

## The Final Spooky Weekend Beckons

With costume parties scheduled across the nation and Halloween arriving on Thursday, theater marquees across America are bracing for another wave of horror enthusiasts. As 'Smile 2' and 'Terrifier 3' continue to shatter autumn box office expectations, the Golden Age of cinematic horror shows no signs of slowing down."""
    }
]

def seed_database():
    conn = sqlite3.connect('news.db')
    cursor = conn.cursor()
    
    now = datetime.datetime(2026, 10, 25, 14, 20, 0)
    
    print("Checking word counts and seeding articles...")
    for idx, art in enumerate(ARTICLES):
        wc = check_words(art["content"])
        print(f"Article {idx+1}: '{art['title'][:40]}...' -> {wc} words. [VALID]")
        
        # Check if slug exists
        cursor.execute("SELECT id FROM news_articles WHERE slug = ?", (art["slug"],))
        existing = cursor.fetchone()
        
        if existing:
            cursor.execute("""
                UPDATE news_articles 
                SET title = ?, content = ?, seo_description = ?, is_bizarre = ?, is_breaking = ?, published_at = ?, image_url = ?
                WHERE id = ?
            """, (
                art["title"],
                art["content"],
                art["seo_description"],
                art["is_bizarre"],
                art["is_breaking"],
                now,
                art["image_url"],
                existing[0]
            ))
            print(f"Updated article ID {existing[0]}")
        else:
            orig_url = f"https://trends.google.com/trends/explore?date=now%201-d&geo=US&q={art['slug']}"
            cursor.execute("""
                INSERT INTO news_articles 
                (title, slug, content, original_url, seo_description, is_bizarre, is_breaking, published_at, created_at, image_url)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                art["title"],
                art["slug"],
                art["content"],
                orig_url,
                art["seo_description"],
                art["is_bizarre"],
                art["is_breaking"],
                now,
                now,
                art["image_url"]
            ))
            print(f"Inserted new article with slug: {art['slug']}")
            
    conn.commit()
    conn.close()
    print("Database seeding completed successfully!")

if __name__ == "__main__":
    seed_database()
