# StockAdviser
An app that recommends stocks in good financial position. Recommendation might change depending on the user preference.

Also helps the user to finalize the decision by getting the relevant news for that certain stock.

Different recommendations depending on the user preference("Ask things like what kind of investor they are(How much returns do you want? Within what time frame?"

When asking those questions, give users realistic values(such as returns within certain time frame).

Make a formula using "The intelligent investor"(And other books but for now only 1.) to see if the company is overvalued, undervalued, in a good financial position, if they can 
generate profit etc(Factors to think about later).

When users input their pesonal preference, put more weight on the logic they prefer(For example, if they're risky investors, put more weight on annual returns and make model or formula based on that)


3 outcomes from user preference. Passive, Standard, Risky
-Passive will focus on consistent average annual returns in longer period(ex.10 years ~ n), Won't look at the price(even if it's expensive), Will look at good dividend returns
,Look at liquidity of the stock, Will focus on undervalued stocks, Will also use the basic financial statement to determine if t he stock is good.

-Standard will look at the overall average during 5 year period, Will also look at the liquidity, Will use the basic financial statement to determine if the stock is in good position. Won't look at the price

(Standard and Passive will have lot of overlaps but will also have different parameters that each others don't have)

-Risky will look at the price range of 0.n to 5(Refer to how SEC defined penny stock), will look at the return over the period of 1 year at a percentage of x%, Will look at if it's traded the most

Mention about pros and cons of each investing style. For example, Risky and Standard will focus heavily on user's decision more than numbers and will have to be manually checked using news where passive will have satisfying numbers to prove that it's a good investment without any worries(however, might have lower returns every year)




Focus on how you're going to feed data and analyze them more than the code.



#Refer to the flowchart(To: urself)(September 28th 2021)








