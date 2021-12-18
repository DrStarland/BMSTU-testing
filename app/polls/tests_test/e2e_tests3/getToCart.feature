Feature: Get Product To Cart

Scenario: User is getting product to cart
Given He entered <username> username
Given He entered <password> password
When He clicked on Product <number> with name <productName>
Then He added the product to cart, cartID = <cartID>, quantity = <quantity>
Then The total quantity of product became <total_quantity>

Examples:
| username |   password  | number | productName | cartID | quantity  |  total_quantity |
|   aaa    |    123456   |    1   |  kistochka  |    1   |     1     |       99        |
|  test14  |  qwerty123  |    2   |  kistochka  |    2   |     1     |        9        |
|   lo_lo  |   xxxxwwww  |    3   |  kistochka  |    3   |     1     |        0        |
