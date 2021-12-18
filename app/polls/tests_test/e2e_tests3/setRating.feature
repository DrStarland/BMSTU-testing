Feature: Set Rating To Product

Scenario: User finds product by filter and sets rating to it
Given He entered <username> username
Given He entered <password> password
When He clicked on the filter, he saw products for <price> price
When He clicked on Product <number> with name <productName>
Then He set <ratingvalue> rating to it

Examples:
| username |   password  |   price | number | productName |  ratingvalue  |
|   aaa    |    123456   |    15   |    1   |  kistochka  |      10       |
