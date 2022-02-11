from com.dakshata.autotrader.api.AutoTrader import AutoTrader
 
autotrader = AutoTrader.create_instance( \
    '<your-api-key>', \
    AutoTrader.SERVER_URL)
 
# Place regular order
response = autotrader.place_regular_order( \
    'ABC123', 'NSE', 'WIPRO', 'BUY', 'LIMIT', 'INTRADAY', 1, 330.35, 0.0)
print(response)
 
# Place bracket order
response = autotrader.place_bracket_order( \
    'ABC123', 'NSE', 'WIPRO', 'SELL', 'LIMIT', 1, 326.35, 0.0, 1, 1, 0)
print(response)
 
# Place cover order
response = autotrader.place_cover_order( \
    'ABC123', 'NSE', 'SBIN', 'SELL', 'LIMIT', 1, 188.15, 190.0)
print(response)
 
# Cancel order
response = autotrader.cancel_order_by_platform_id( \
    'ABC123', '201007000438034')
print(response)
 
# Exit bracket or cover order
response = autotrader.cancel_child_orders_by_platform_id( \
    'ABC123', '201007000448051')
print(response)
 
# Modify an order
response = autotrader.modify_order_by_platform_id('ABC123', '201007000443194', price=325.9)
# response = autotrader.modify_order_by_platform_id('ABC123', '201007000443194', quantity=2)
# response = autotrader.modify_order_by_platform_id('ABC123', '201007000443194', trigger_price=322)
# response = autotrader.modify_order_by_platform_id('ABC123', '201007000443194', order_type='MARKET')
print(response)
 
# Square-off position
response = autotrader.square_off_position( \
    'ABC123', 'DAY', 'MIS', 'NSE', 'WIPRO')
print(response)
 
# Square-off portfolio
response = autotrader.square_off_portfolio( \
    'ABC123', 'DAY')
print(response)
 
# reading orders data
response = autotrader.read_platform_orders('ABC123')
print(*response.result, sep = "\n\n")
 
# reading positions data
response = autotrader.read_platform_positions('ABC123')
print(*response.result, sep = "\n\n")
 
# reading margins data
response = autotrader.read_platform_margins('ABC123')
print(*response.result, sep = "\n\n")