from langchain.prompts.chat import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate


def build_prompt():
    system_message = SystemMessagePromptTemplate.from_template(
        '''Generate 50 highly relevant and specific product or service keywords for the given sub-industry. Use the provided industry context and detailed description to optimize the keywords for SEO.

Input Details:
1. Industry: A brief overview of the broader industry to establish the foundational context.
2. Description: Detailed insights or characteristics of the industry to provide additional context for keyword generation.
3. Sub-Industry: The specific sub-industry that is the primary focus for the keywords.

Guidelines:
1. Generate all keywords in lowercase for consistency.
2. Limit each keyword to 1-2 words for brevity and clarity.
3. Avoid duplicates or overly similar keywords to ensure a diverse and unique set.
4. Exclude generic terms that lack direct relevance to the sub-industry.
5. Ensure each keyword reflects the specificity of the sub-industry while aligning with the broader industry context.
6. Do not use periods at the end of the keywords.

Output Format:
keyword1, keyword2, keyword3, ...

Example 1:
Industry : Retail Musical Instruments
Description : This industry includes entities that primarily retail new musical instruments, sheet music, and related supplies; or retailing these new products in combination with services like musical instrument repair, rental, or music instruction.
Sub-Industry: Musical Instrument and Supplies Stores
Expected Output:
musical instruments, sheet music, guitar sales, piano sales, drum kits, violin strings, instrument repair, guitar accessories, music instruction, instrument rental, band instruments, recording supplies, music stands, brass instruments, woodwind instruments, percussion instruments, electric guitars, acoustic guitars, ukuleles, keyboards, music books, cymbals, bass guitars, digital pianos, sound equipment, amplifiers, guitar pedals, music lessons, instrument maintenance, orchestral instruments, professional microphones, music cables, guitar cases, string replacements, practice pads, studio monitors, music software, recording gear, music theory books, portable keyboards, beginner guitars, advanced violins, compact drum kits, custom instruments, guitar picks, music shop, instrument cleaning, instrument tuning, studio accessories, music lighting

Example 2:
Industry : Printing Services
Description : This industry includes entities that print on apparel and textile products, paper, metal, glass, plastics, and other materials, except fabric (grey goods).
Sub-Industry: Books Printing
Expected Output:
book printing, custom books, hardcover printing, softcover books, digital printing, offset printing, book binding, bulk printing, print on demand, booklet printing, photo books, textbook printing, novel printing, art books, children’s books, cookbook printing, coffee table books, professional printing, self-publishing, spiral binding, saddle stitch books, perfect binding, library binding, manuscript printing, glossy books, matte finish books, book covers, premium paper, embossing services, foil stamping, print proofs, booklets, limited edition books, eco-friendly printing, paper selection, color printing, black-and-white books, educational books, publishing services, large format books, paperback books, oversized books, chapter books, religious books, poetry books, anthology printing, graphic novels, trade books, archival quality, typography printing, creative covers

Example 3:
Industry : Financial Services
Description : This industry includes entities that make financial transactions (creation, liquidation, or change in ownership of financial assets) and/or that facilitate financial transactions.
Sub-Industry: Finance and Insurance
Expected Output:
financial planning, insurance policies, wealth management, risk assessment, life insurance, health insurance, property insurance, auto insurance, investment management, retirement planning, annuities, term insurance, whole life insurance, disability insurance, financial consulting, mortgage insurance, critical illness cover, umbrella insurance, savings plans, income protection, corporate insurance, financial advisory, estate planning, insurance claims, business insurance, personal loans, credit insurance, tax optimization, mutual funds, pension plans, asset protection, insurance underwriting, premium financing, risk management, liability insurance, wealth protection, insurance brokers, casualty insurance, investment advisors, insurance analytics, reinsurance services, structured finance, financial risk, insurance quotes, credit risk, long-term care insurance, travel insurance, cyber insurance, policy renewal, insurance audits

Example 4:
Industry : Marketing Services
Description : This industry includes entities that provide operating advice and assistance to businesses and other organizations on marketing issues, such as developing marketing objectives and policies, sales forecasting, new product development and pricing, licensing and franchise planning, and marketing planning and strategy.
Sub-Industry: Advertising Agencies
Expected Output:
digital advertising, brand strategy, media planning, content creation, social media ads, seo services, ppc campaigns, display ads, influencer marketing, creative design, ad copywriting, campaign management, programmatic ads, video advertising, native advertising, outdoor advertising, mobile advertising, email marketing, brand identity, market analysis, audience targeting, brand positioning, print ads, direct mail campaigns, ad optimization, ad analytics, retargeting ads, performance marketing, event promotions, public relations, television ads, radio advertising, sponsorship deals, ad placements, banner advertising, interactive ads, creative consulting, ad testing, experiential marketing, integrated campaigns, local advertising, corporate branding, geo-targeting ads, storytelling marketing, product launch ads, customer engagement, affiliate marketing, remarketing ads, media buying, marketing audits

Exmaple 5:
Industry : Newspaper Publishing
Description : This industry includes entities known as newspaper publishers. Entities in this industry produce and distribute newspapers (such as, gather news; write news columns, feature stories, and editorials; and sell and prepare advertisements). These entities may publish newspapers in print or electronic form.
Sub-Industry: Newspaper Publishers
Expected Output: 
newspaper printing, digital newspapers, local news, editorial services, classified ads, news syndication, political news, investigative reporting, news subscriptions, feature stories, sports reporting, entertainment news, obituaries publishing, breaking news, advertising sales, community news, news photography, press releases, opinion columns, business news, global news, lifestyle features, weather updates, news archives, special editions, weekend papers, news apps, online news portals, e-newspapers, newsroom management, headline writing, current events, news analytics, print advertising, media distribution, subscription management, cultural reporting, editorial columns, live reporting, environmental news, public affairs, mobile news platforms, news podcasts, advertising inserts, subscription offers, press coverage, local events, industry news, freelance reporting, news design'''
    )
    human_message = HumanMessagePromptTemplate.from_template('Industry: {industry}\nDescription: {description}\nSub-Industry: {sub_industry}')
    return ChatPromptTemplate.from_messages([system_message, human_message])