#### from URL: https://www.futilitycloset.com/2024/05/24/day-tripper/

Lewis Carroll – computing the day of the week for any given date (1887) 

A letter from Lewis Carroll to
Nature
, March 31, 1887:
Having hit upon the following method of mentally computing the day of the week for any given date, I send it you in the hope that it may interest some of your readers. I am not a rapid computer myself, and as I find my average time for doing any such question is about 20 seconds, I have little doubt that a rapid computer would not need 15.
Take the given date in 4 portions, viz. the number of centuries, the number of years over, the month, the day of the month.
Compute the following 4 items, adding each, when found, to the total of the previous items. When an item or total exceeds 7, divide by 7, and keep the remainder only.
The Century-Item.
— For Old Style (which ended September 2, 1752) subtract from 18. For New Style (which began September 14) divide by 4, take overplus from 3, multiply remainder by 2. [The Century-Item is the first two digits of the year, so for 1811 take 18.]
The Year-Item.
— Add together the number of dozens, the overplus, and the number of 4’s in the overplus.
The Month-Item.
— If it begins or ends with a vowel, subtract the number, denoting its place in the year, from 10. This, plus its number of days, gives the item for the following month. The item for January is ‘0’; for February or March (the 3rd month), ‘3’; for December (the 12th month), ’12.’ [So, for clarity, the required final numbers after division by 7 are January, 0; February, 3; March, 3; April, 6; May, 1; June, 4; July, 6; August 2; September, 5; October, 0; November, 3; and December, 5.]
The Day-Item
is the day of the month.
The total, thus reached, must be corrected, by deducting ‘1’ (first adding 7, if the total be ‘0’), if the date be January or February in a Leap Year: remembering that every year, divisible by 4, is a Leap Year, excepting only the century-years, in New Style, when the number of centuries is
not
so divisible (
e.g.
1800).
The final result gives the day of the week, ‘0’ meaning Sunday, ‘1’ Monday, and so on.
Examples
1783,
September
18
17, divided by 4, leaves ‘1’ over; 1 from 3 gives ‘2’; twice 2 is ‘4.’
83 is 6 dozen and 11, giving 17; plus 2 gives 19,
i.e.
(dividing by 7) ‘5.’ Total 9,
i.e.
‘2.’
The item for August is ‘8 from 10,’
i.e.
‘2’; so, for September, it is ‘2 plus 3,’
i.e.
‘5.’ Total 7,
i.e.
‘0,’ which goes out.
18 gives ‘4.’ Answer,
‘Thursday.’
1676,
February
23
16 from 18 gives ‘2.’
76 is 6 dozen and 4, giving 10; plus 1 gives 11,
i.e.
‘4.’ Total ‘6.’
The item for February is ‘3.’ Total 9,
i.e.
‘2.’
23 gives ‘2.’ Total ‘4.’
Correction for Leap Year gives ‘3.’ Answer,
‘Wednesday.’
(Via Edward Wakeling,
Rediscovered Lewis Carroll Puzzles
, 1995.)
May 24, 2024
May 23, 2024
