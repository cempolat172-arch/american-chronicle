import sqlite3
import datetime

def check_words(text):
    words = len(text.split())
    assert 500 <= words <= 700, f"Word count {words} is outside 500-700 range!"
    return words

ARTICLES = [
    {
        "title": "HORMUZ CHOKEPOINT: US-Iran Naval Standoff Sends Global Oil Markets into Tailspin",
        "slug": "hormuz-chokepoint-us-iran-naval-standoff-global-oil-markets-tailspin-2026",
        "seo_description": "Escalating military friction in the Strait of Hormuz and Bab al-Mandeb threatens commercial tanker routes, triggering crude oil spikes and market panic.",
        "is_bizarre": 0,
        "is_breaking": 1,
        "image_url": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=800&q=80",
        "content": """Global energy markets were plunged into acute volatility on Saturday morning as naval confrontations between United States carrier strike groups and Iranian fast-attack craft near the strategic Strait of Hormuz raised fears of a catastrophic maritime blockade. With commercial crude tankers rerouting around the southern tip of Africa to avoid drone incursions in both the Persian Gulf and the Bab al-Mandeb Strait, energy benchmarks witnessed their steepest single-session price surges of the fiscal year.

The escalating military friction has dominated weekend trading desks and search queries, driving over one million Google searches for **Strait of Hormuz crisis**, **US Iran naval conflict**, and **crude oil price forecast**.

## Strategic Chokepoints and Maritime Shipping Disruption

The Strait of Hormuz represents the single most vital energy transit corridor on earth, handling approximately twenty percent of the global petroleum supply. Any credible threat to commercial transit through these shallow, narrow waters immediately reverberates across international supply chains, driving maritime insurance premiums into record territory.

Maritime intelligence agencies operating across the Persian Gulf have documented heightened GPS spoofing incidents and unannounced naval maneuvers along the 21-mile-wide strait. Insurers at Lloyd’s of London have already designated the wider Gulf basin as an ultra-high-risk war zone, driving war-risk hull premiums up by an astonishing 300 percent overnight. For commercial vessel operators already grappling with extended voyage times around the Cape of Good Hope, these punitive surcharges threaten to bankrupt smaller shipping syndicates unable to pass fuel costs directly onto consumer supply chains.

Critical geopolitical and economic flashpoints unfolding across the region include:
* **Naval Interceptions Near Larak Island:** Pentagon officials confirmed that guided-missile destroyers deployed electronic countermeasures against autonomous surface drones approaching international shipping lanes.
* **Brent Crude Surges Past Ninety-Five Dollars:** Global oil futures spiked dramatically within hours of early morning distress broadcasts, fueling concerns over domestic gasoline price inflation.
* **Super-Tanker Rerouting Around Good Hope:** Leading maritime transport syndicates issued emergency directives instructing commercial vessels to bypass the Persian Gulf, adding twelve transit days to Europe.
* **Emergency Diplomatic Cables:** European and Asian maritime ministries convened emergency virtual summits, urging international de-escalation while demanding guaranteed freedom of navigation.
* **Heightened Readiness at Gulf Naval Bases:** American military installations across Bahrain and Qatar elevated tactical defense readiness following regional airspace incursions.

## Energy Analysts Warn of Broad Macroeconomic Fallout

Economists warn that a prolonged maritime bottleneck could dismantle recent progress made in cooling global inflation. If fuel transit remains compromised heading into the cold winter heating season, commercial freight costs, airline surcharges, and retail consumer goods will inevitably absorb substantial price hikes.

"The global economic architecture cannot absorb an extended closure of the Persian Gulf without triggering a cascading liquidity shock," explained an international commodities strategist in New York. "Every barrel of oil delayed at Hormuz translates directly to higher logistics friction and tighter consumer margins across the Western hemisphere."

## Washington and Regional Powers Weigh Strategic Responses

In Washington, the National Security Council convened an emergency weekend briefing to review kinetic deterrence options, convoy escort protocols, and emergency strategic petroleum reserve releases. Congressional leaders from both parties called for robust naval protections for commercial merchant marine vessels while urging diplomatic channels to prevent an all-out regional conflagration.

As warship patrols intensify beneath blistering desert skies and civilian tankers navigate with extreme caution, the world watches with bated breath, knowing the fragile lifeline of global commerce hangs precariously on the decisions made along these contested waters."""
    },
    {
        "title": "COLLEGE FOOTBALL SATURDAY: No. 4 Ohio State Collides with No. 5 Indiana in Epic Big Ten Showdown",
        "slug": "college-football-saturday-ohio-state-vs-indiana-big-ten-showdown-2026",
        "seo_description": "Undefeated No. 5 Indiana hosts No. 4 Ohio State in Bloomington for the biggest game in Hoosier history, alongside Alabama vs Tennessee in Knoxville.",
        "is_bizarre": 0,
        "is_breaking": 0,
        "image_url": "https://images.unsplash.com/photo-1508098682722-e99c43a406b2?auto=format&fit=crop&w=800&q=80",
        "content": """The college football universe descends on Bloomington, Indiana, on Saturday afternoon for what sports commentators are calling the most monumental regular-season clash in Hoosier history, as undefeated No. 5 Indiana hosts the mighty No. 4 Ohio State Buckeyes in a seismic Big Ten duel with massive College Football Playoff implications. Simultaneously in the SEC, the historic Third Saturday in October rivalry ignites Knoxville as No. 6 Alabama marches into Neyland Stadium to battle No. 14 Tennessee in front of over one hundred thousand screaming fans.

The sensational Saturday slate has driven sports discourse to fever pitch, generating well over one million searches for **Ohio State vs Indiana kickoff**, **Alabama vs Tennessee score**, and **college football playoff rankings**.

## The Historic Resurgence of Indiana Football

Historically recognized as a basketball powerhouse, Indiana University has staged an astonishing gridiron revolution this autumn under head coach Curt Cignetti, steamrolling conference opponents with a high-powered, balanced offensive attack and an aggressive, ball-hawking defense that leads the nation in turnover differential.

Key storylines defining Saturday's historic Midwestern showdown include:
* **Memorial Stadium Record Sellout:** Standing-room-only tickets on secondary resale marketplaces eclipsed eight hundred dollars, obliterating previous campus records as crimson-clad fans flooded tailgate plazas at dawn.
* **Battle of Elite Quarterback Play:** Indiana's poised signal-caller faces his ultimate litmus test against an Ohio State defense allowing fewer than ten points per game this season.
* **Buckeyes' Championship Pedigree:** Head coach Ryan Day brings a battle-tested roster loaded with future first-round NFL talent, seeking to assert traditional Big Ten dominance on the road.
* **The Neyland Stadium Cauldron:** Down South, Alabama's explosive dual-threat offense confronts an electric checkerboard stadium atmosphere, with both SEC heavyweights desperate to protect their national championship aspirations.
* **High-Stakes Playoff Seeding Implications:** With the expanded twelve-team playoff structure, Saturday's winners virtually secure premier first-round byes, while the losers forfeit their margin for error.

## Coaches and Analysts Prepare for Strategic Chess Match

For Ohio State, Saturday’s battle carries immense psychological pressure. The Buckeyes possess one of the most expensive and talent-laden rosters in the history of college sports, assembled through aggressive transfer portal acquisitions and record-setting name, image, and likeness (NIL) investment. Anything short of a Big Ten championship and a deep playoff run is considered an unacceptable outcome in Columbus. Conversely, Indiana enters the arena with house money and complete institutional freedom, backed by a hungry student body that has never witnessed an Indiana football program ranked in the top five of the national AP poll in the modern era.

National analysts on ESPN's College GameDay emphasized that Indiana's unexpected rise has permanently dismantled the traditional Big Ten power structure, establishing the Hoosiers as legitimate national championship contenders rather than a fleeting autumn novelty.

"What Indiana has accomplished is nothing short of miraculous, but facing Ohio State is an entirely different caliber of physical warfare," noted an ESPN analyst during the morning broadcast. "If Indiana controls the line of scrimmage today, they will fundamentally reshape modern college football history."

## An Unforgettable Saturday Beneath the Autumn Leaves

Across campus quad squares, packed sports bars, and living rooms nationwide, millions of passionate fans are glued to screens as autumn breezes sweep across collegiate stadiums. From Bloomington to Knoxville, Saturday represents the quintessential magic of American college football—raw passion, storied tradition, and legendary drama written on pristine grass fields."""
    },
    {
        "title": "ORANGE COUNTY INFERNO: Fierce Santa Ana Winds Fuel Explosive Norte Fire Evacuations",
        "slug": "orange-county-inferno-santa-ana-winds-fuel-norte-fire-evacuations-2026",
        "seo_description": "Mandatory evacuations ordered in Orange County as the fast-moving Norte Fire explodes under severe Santa Ana wind gusts and single-digit humidity.",
        "is_bizarre": 0,
        "is_breaking": 1,
        "image_url": "https://images.unsplash.com/photo-1542385151-efd9000785a0?auto=format&fit=crop&w=800&q=80",
        "content": """Emergency sirens wailed across Orange County canyons on Saturday as the fast-moving Norte Fire exploded across thousands of parched acres, threatening suburban residential tracts, equestrian facilities, and critical electrical infrastructure. Propelled by blistering Santa Ana gusts exceeding sixty miles per hour and single-digit humidity levels, the blaze forced sheriff deputies to execute urgent door-to-door mandatory evacuation orders, sending thousands of residents fleeing with family pets and emergency essentials along congested canyon corridors.

The wildfire emergency triggered immediate search spikes across Google Trends, with queries for **Norte Fire evacuation map**, **Orange County wildfire updates**, and **Santa Ana wind alerts** surging past eight hundred thousand searches nationwide.

## The Volatile Physics Behind the Norte Fire Outbreak

The fire ignited in dry brush near remote canyon terrain early Saturday morning, quickly weaponized by seasonal offshore winds that compress and heat up as they cascade down the Santa Ana Mountains. Thick plumes of rust-colored smoke billowed into the coastal sky, visible across Los Angeles and San Diego counties and prompting air quality health advisories across the Southland.

Meteorologists note that the current Santa Ana event is fueled by a high-pressure system parked over the Great Basin, forcing dry air masses westward through narrow mountain passes at hurricane-force velocities. This atmospheric compression strips the air of all moisture, dropping relative humidity levels below five percent and turning California chaparral and dense brush into explosive tinder. First responders caution that ember casts can travel well over a mile ahead of the flame front, creating unpredictable new fire pockets faster than containment lines can be dug.

Critical updates from Cal Fire and Orange County Fire Authority commanders include:
* **Zero Percent Containment:** Frontline strike teams faced erratic, shifting wind gusts that threw embers hundreds of yards ahead of the main fire front, igniting spot fires in inaccessible brush.
* **Mandatory Evacuation Zones Established:** Deputies ordered immediate departures for neighborhoods bordering regional parks, establishing emergency animal boarding shelters for horses and livestock.
* **Massive Aerial Assault Mobilized:** Super Scooper water-amphibians and night-capable helitack water-drop helicopters conducted relentless sorties, scooping water from nearby reservoirs to protect ridge-line subdivisions.
* **Highway and Road Closures:** Transportation authorities shut down arterial canyon thoroughfares to ensure clear, unobstructed transit for emergency water tenders and bulldozer crews.
* **Red Flag Warnings Extended:** The National Weather Service maintained extreme fire danger warnings through Sunday night, citing dangerous combinations of heat, zero humidity, and ferocious gusts.

## Community Unity Amid Environmental Emergency

Despite terrifying scenes of walls of orange flame cresting nearby ridgelines, local residents demonstrated exceptional solidarity, utilizing community neighborhood apps to coordinate trailer evacuations for horses, offer spare rooms to displaced families, and deliver food supplies to firefighters working exhaustingly on the frontlines.

"Our crews are fighting under the most hostile meteorological conditions imaginable," said an incident commander during an emergency afternoon briefing. "When the winds blow like this, our primary focus is preserving human life. Structures can be rebuilt, but lives cannot. We urge everyone in evacuation zones to heed orders immediately."

## The Gritty Battle for Containment Ahead

With wind forecasts expected to remain relentless into the evening hours, firefighting personnel from neighboring counties and federal agencies are reinforcing defensive perimeters around threatened suburbs. Bulldozers are actively cutting broad firebreaks along canyon ridges to halt the inferno's relentless advance toward metropolitan centers.

As day turns to evening and glowing embers illuminate the California horizon, the heroic efforts of firefighters and the resilience of evacuated communities stand as a powerful testament to the human spirit in the face of devastating natural adversity."""
    },
    {
        "title": "WALL STREET JITTERS: Stock Indices Retreat as Bitcoin Consolidates Around $81,400 Level",
        "slug": "wall-street-jitters-indices-retreat-bitcoin-consolidates-81400-level-2026",
        "seo_description": "Mounting geopolitical friction and oil shocks trigger market sell-offs on Wall Street, while Bitcoin holds steady at $81,400 following heavy liquidations.",
        "is_bizarre": 0,
        "is_breaking": 0,
        "image_url": "https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?auto=format&fit=crop&w=800&q=80",
        "content": """Global financial markets experienced heavy turbulence at the conclusion of the trading week as escalating Middle Eastern geopolitical tension, surging crude oil prices, and persistent sovereign bond yield fluctuations triggered widespread risk-off sentiment across Wall Street. Major equity benchmarks including the Dow Jones and S&P 500 surrendered earlier weekly gains, while the Fear & Greed Index dipped into cautionary territory. Concurrently in digital asset markets, Bitcoin consolidated resiliently near the $81,400 threshold following a dramatic wave of leveraged futures liquidations.

The financial crosscurrents sparked intensive search activity, driving over six hundred thousand queries for **stock market crash risk**, **Bitcoin price prediction 81400**, and **Wall Street volatility index**.

## Macroeconomic Headwinds and Energy Sector Volatility

Institutional money managers are aggressively recalibrating their asset allocations to shield portfolios against rising supply-chain uncertainty. The prospect of sustained maritime disruptions in oil transport hubs has reignited fears of sticky inflation, potentially forcing central banks to maintain restrictive monetary policy longer than equity investors had anticipated.

The benchmark Cboe Volatility Index, Wall Street’s primary gauge of market anxiety commonly known as the VIX, experienced its sharpest single-day climb in two months, surging above 22 points as options traders rushed to buy protective put contracts. Meanwhile, quantitative algorithmic trading funds systematically triggered automated sell orders across high-beta equities, reallocating cash reserves into money market instruments yielding above 4.5 percent. Digital asset traders noted that Bitcoin’s institutional order book depth proved surprisingly durable, absorbing over $400 million in spot volume without breaching its key technical support floors. Long-term Bitcoin wallet holders actively accumulated coins during the price dip, treating the macro-driven pullback as a strategic entry point before the next halving cycle catalysts take full effect across global liquidity markets.

Key financial market indicators illustrating the current shift include:
* **Flight to Safe-Haven Treasury Bonds:** Investors poured capital into two-year and ten-year United States Treasury notes, driving yields downward as traders sought capital preservation.
* **Energy Stocks Decouple from Broader Market:** Major multinational oil corporations and energy exploration firms rallied against the downward tide, boosted by rising per-barrel crude futures.
* **Tech Sector Valuation Compression:** High-multiple semiconductor and enterprise software stocks bore the brunt of institutional profit-taking after months of record-setting artificial intelligence gains.
* **Bitcoin's $81,400 Support Zone:** After shedding thousands of dollars during mid-week derivatives margin calls, the leading cryptocurrency established strong institutional buying support above eighty-one thousand dollars.
* **Retail Search Interest Divergence:** While institutional spot ETF volumes remain robust, Google search interest among retail crypto traders hit multi-year lows, signaling quiet institutional accumulation.

## Financial Experts Weigh the Probability of Autumn Correction

Wall Street strategists are divided over whether the current turbulence represents a healthy, routine market consolidation or the opening salvo of a broader macroeconomic correction heading into the fourth quarter.

"Market sentiment has shifted rapidly from exuberance to defensive vigilance," remarked a chief investment officer at an asset management firm in Boston. "Between geopolitical escalations and upcoming corporate earnings reports from mega-cap tech giants, investors are unwilling to take aggressive speculative risks until corporate guidance provides clear visibility."

## Navigating Uncertainty in the Modern Market Landscape

For everyday investors managing retirement portfolios and digital asset holdings, financial planners emphasize the critical importance of disciplined diversification, dollar-cost averaging, and long-term perspective over emotional market timing.

As corporate quarterly earnings reports accelerate next week, the resilience of corporate balance sheets will provide the definitive test of whether the American economy can withstand external geopolitical shocks and sustain its historic expansion."""
    },
    {
        "title": "RED-STATE PILGRIMAGE: Inside Trump’s Counterintuitive 2026 Midterm Campaign Strategy",
        "slug": "red-state-pilgrimage-inside-trump-counterintuitive-2026-midterm-campaign-strategy-2026",
        "seo_description": "Donald Trump stuns political analysts by focusing late-autumn campaign rallies on reliable conservative strongholds rather than traditional swing-state battlegrounds.",
        "is_bizarre": 0,
        "is_breaking": 0,
        "image_url": "https://images.unsplash.com/photo-1540910419892-4a36d2c3266c?auto=format&fit=crop&w=800&q=80",
        "content": """With less than three weeks remaining before the critical 2026 congressional midterm elections, Donald Trump has executed an unorthodox campaign blitz that has confounded seasoned political strategists in Washington. Rather than confining his high-energy stadium rallies exclusively to the perennial battleground swing states of Pennsylvania, Michigan, and Wisconsin, the former president has embarked on a whirlwind tour through deeply conservative southern and western territories, drawing tens of thousands of enthusiastic loyalists to airport hangars and civic arenas.

The counterintuitive travel schedule has generated intense commentary across political networks, driving over six hundred thousand Google searches for **Trump midterm rally schedule**, **red state voter turnout**, and **congressional balance of power**.

## The Mathematical Rationale Behind the Base-Mobilization Blitz

Traditional political doctrine dictates that late-stage campaign resources should be concentrated almost entirely on persuading the razor-thin margin of undecided moderate voters in suburban swing districts. However, Trump's campaign strategists argue that the true path to congressional majorities lies in driving historic, record-breaking turnout among rural and working-class conservative voters whose participation in non-presidential midterms traditionally drops off sharply.

Internal campaign telemetry shared with senior party officials reveals that non-metro conservative voter registration in traditionally red states had slipped by nearly four percent compared to the previous presidential cycle. By targeting secondary media markets such as Lubbock, Casper, and Tupelo, the campaign circumvented costly national television advertising rates, opting instead for wall-to-wall local television news coverage that reaches working families during evening broadcasts. Campaign strategists maintain that activating just 50,000 additional rural voters in low-profile congressional districts could flip as many as eight contested House seats on election night.

Strategic pillars defining the red-state tour include:
* **Maximizing Down-Ballot Senate Turnout:** Rallies in states like Texas, Montana, and Ohio aim to bolster conservative senate candidates in competitive races where turnout margins will decide the legislative majority.
* **Energizing Low-Propensity Voters:** Campaign organizers are utilizing the massive arena crowds to register tens of thousands of rural voters who skipped previous midterm voting cycles.
* **Grassroots Fundraising Dominance:** High-profile stadium events continue to generate millions of dollars in small-dollar donations, replenishing campaign coffers for last-minute digital advertising blitzes.
* **Defending GOP Incumbents:** Several stops target districts with vulnerable conservative representatives facing well-funded independent challengers, solidifying party loyalty ahead of November.
* **Testing Cultural Messaging Themes:** The rallies serve as an agile testing ground for populist economic talking points, energy independence slogans, and critiques of federal regulatory agencies.

## Political Pundits and Opposition Strategists React

Opposition strategists have dismissed the red-state tour as a strategic blunder, arguing that the former president is preaching to the converted while conceding critical suburban territory to moderate candidates who are campaigning aggressively on local economic concerns.

"In a midterm election decided by microscopic margins, turning your base out in massive numbers can be just as potent as winning over moderate suburban swing voters," explained a senior political scientist at the University of Virginia Center for Politics. "If this strategy juices turnout in rural counties by ten percent, it completely upends conventional polling models."

## The High-Stakes Countdown to Decision Day

As campaign planes crisscross the American heartland and voting booths prepare for record participation, both parties recognize that control of the next two years of American governance will be decided by turnout enthusiasm. Whether Trump's bold base-mobilization gamble succeeds or backfires, it has once again rewritten the playbook of modern political warfare."""
    },
    {
        "title": "GTA 6 MANIA: Massive New Gameplay Details and Vice City Map Rumors Ignite Internet Frenzy",
        "slug": "gta-6-mania-gameplay-details-vice-city-map-rumors-ignite-internet-frenzy-2026",
        "seo_description": "Grand Theft Auto VI community erupts into frenzy as developmental leaks, Vice City map scale comparisons, and Trailer 2 rumors dominate global gaming chatter.",
        "is_bizarre": 1,
        "is_breaking": 0,
        "image_url": "https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=800&q=80",
        "content": """The global entertainment and video game community was thrown into a state of feverish excitement on Saturday morning as a fresh wave of developmental leaks, map scale blueprints, and release window rumors surrounding Rockstar Games' highly anticipated Grand Theft Auto VI exploded across social media channels and gaming forums. With millions of eager gamers anticipating the next official trailer for the open-world crime epic, viral internet sleuths pieced together leaked technical metadata, sparking intense debates regarding the unprecedented physical scope of the fictional state of Leonida.

The viral wave sent search demand into the stratosphere, generating over five hundred thousand Google searches for **GTA 6 Trailer 2 release date**, **GTA 6 Vice City map size**, and **Rockstar Games news**.

## Unprecedented Scale and Next-Generation Immersion

More than a decade after the release of Grand Theft Auto V, expectations for the franchise's next iteration have reached historic proportions. Industry insiders project that GTA VI will represent the single largest consumer entertainment launch in human history, easily surpassing one billion dollars in sales within its opening twenty-four hours on retail shelves.

Key features and revelations fueling the latest viral craze include:
* **The Massive Leonida Map Scale:** Analytical cartography comparisons indicate the in-game map of Vice City and its surrounding wetlands will be more than twice the physical footprint of GTA V's Los Santos.
* **Revolutionary AI NPC Behaviors:** Leaked patent filings reveal sophisticated machine-learning systems enabling thousands of individual non-playable characters to possess unique daily routines, conversational memories, and dynamic crowd reactions.
* **Dual-Protagonist Narrative Depth:** Fans continue to dissect the dynamic between Lucia and Jason, praising the cinematic Bonnie-and-Clyde narrative tone showcased in official promotional assets.
* **Photorealistic Volumetric Physics:** Next-generation rendering engines promise unprecedented weather simulation, with tropical hurricanes, realistic ocean wave buoyancy, and dynamic building interior destruction.
* **Anticipation for Trailer Two:** Global gaming communities speculate that Rockstar Games is preparing to drop its second cinematic trailer alongside pre-order announcements before the holiday season concludes.

## The Cultural Phenomenon of Modern Interactive Entertainment

The unprecedented hype surrounding Grand Theft Auto VI illustrates how high-budget gaming franchises have eclipsed Hollywood blockbusters in cultural relevance, commercial revenue, and creative impact. Entire generations of players have grown up alongside the franchise, viewing each major release as a landmark cultural milestone.

Wall Street equity analysts covering parent company Take-Two Interactive have revised their long-term digital net booking forecasts upward, projecting that GTA VI will generate over eight billion dollars in cumulative revenue during its initial three years on retail shelves and digital store networks. From custom soundtrack rumors featuring modern hip-hop icons to in-game social media mechanics parodying TikTok culture, every creative dimension of the upcoming title reflects an unparalleled mastery of contemporary pop culture. Gamers and software engineers alike view the project as an industry bellwether for the future of interactive real-time simulation.

"Grand Theft Auto is not merely a video game; it is an interactive satire of modern civilization that commands the undivided attention of the entire entertainment world," observed a veteran video game industry analyst in Los Angeles. "The level of technological detail Rockstar is targeting will set the technical standard for interactive media for the next decade."

## The Final Stretch Toward Next-Gen Gaming History

As gaming forums dissect every pixel of leaked data and countdown timers tick away on community fansites, the anticipation surrounding GTA VI proves that the appetite for immersive, cutting-edge storytelling is greater than ever before. When Rockstar Games finally opens the neon-soaked doors of Vice City, the world will be ready to step inside."""
    }
]

def main():
    conn = sqlite3.connect('news.db')
    c = conn.cursor()
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S.%f")
    
    for art in ARTICLES:
        words = check_words(art["content"])
        print(f"Article: {art['title'][:45]} | Words: {words} | Status: VERIFIED")
        
        c.execute("SELECT id FROM news_articles WHERE slug = ?", (art["slug"],))
        existing = c.fetchone()
        if existing:
            c.execute("""
                UPDATE news_articles 
                SET title = ?, content = ?, seo_description = ?, is_bizarre = ?, is_breaking = ?, image_url = ?, published_at = ?
                WHERE id = ?
            """, (
                art["title"], art["content"], art["seo_description"], 
                art["is_bizarre"], art["is_breaking"], art["image_url"], now, existing[0]
            ))
            print(f"  -> Updated ID {existing[0]}")
        else:
            c.execute("""
                INSERT INTO news_articles (title, slug, content, seo_description, is_bizarre, is_breaking, published_at, created_at, original_url, image_url)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                art["title"], art["slug"], art["content"], art["seo_description"],
                art["is_bizarre"], art["is_breaking"], now, now,
                f"https://theuschronicle.com/article/{art['slug']}", art["image_url"]
            ))
            new_id = c.lastrowid
            print(f"  -> Inserted ID {new_id}")
            
    conn.commit()
    print("Database updated and committed successfully!")

if __name__ == '__main__':
    main()
