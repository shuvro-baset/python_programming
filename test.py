data = [
    {
        'item_name': 'Industrial Cable Tray Ms Sheet with cover',
        'uom': 'pcs',
        'qty': '17',
        'size': '6.74',
        'type_data': '',
        'brand_data': '',
        'model_data': '',
        'item_group': 'Accessories',
        'relevant_zone': '',
        'description': '0',
        'schedule_date': '27-09-2022',
        'stock_in_hand': '0',
        'last_in_house_date': '0',
        'suppliers': 'Altersense LMTd',
        'last_purchase_rate': '0',
        'last_6_month_consumption': '0'
    },
    {
        'item_name': 'Ms Square Box',
        'uom': 'pcs',
        'qty': '17',
        'size': '6.74',
        'type_data': '',
        'brand_data': '',
        'model_data': '',
        'item_group': 'Accessories',
        'relevant_zone': '',
        'description': '',
        'schedule_date': '27-09-2022',
        'stock_in_hand': '0',
        'last_in_house_date': '0',
        'suppliers': 'Altersense LMTd',
        'last_purchase_rate': '0',
        'last_6_month_consumption': '0'
    },
    {
        'item_name': 'thread',
        'uom': 'pcs',
        'qty': '17',
        'size': '6.74',
        'type_data': 'Accessories',
        'brand_data': '',
        'model_data': '',
        'item_group': 'Accessories',
        'relevant_zone': '',
        'description': '',
        'schedule_date': '27-09-2022',
        'stock_in_hand': '0',
        'last_in_house_date': '0',
        'suppliers': 'Altersense LMTd',
        'last_purchase_rate': '0',
        'last_6_month_consumption': '0'
    },
    {
        'item_name': 'support',
        'uom': 'job',
        'qty': '17',
        'size': '6.74',
        'type_data': 'Accessories',
        'brand_data': '',
        'model_data': '',
        'item_group': 'Accessories',
        'relevant_zone': '',
        'description': '',
        'schedule_date': '27-09-2022',
        'stock_in_hand': '0',
        'last_in_house_date': '0',
        'suppliers': 'Altersense LMTd',
        'last_purchase_rate': '0',
        'last_6_month_consumption': '0'
    },
    {
        'item_name': 'ms square',
        'uom': 'job',
        'qty': '17',
        'size': '',
        'type_data': '',
        'brand_data': 'hikvision',
        'model_data': '',
        'item_group': 'Accessories',
        'relevant_zone': '',
        'description': '',
        'schedule_date': '27-09-2022',
        'stock_in_hand': '0',
        'last_in_house_date': '0',
        'suppliers': 'Altersense LMTd',
        'last_purchase_rate': '0',
        'last_6_month_consumption': '0'
    },
    {
        'item_name': 'hikvision',
        'uom': 'pcs',
        'qty': '17',
        'size': '',
        'type_data': '',
        'brand_data': 'hikvision',
        'model_data': '',
        'item_group': 'Accessories',
        'relevant_zone': '',
        'description': '',
        'schedule_date': '27-09-2022',
        'stock_in_hand': '0',
        'last_in_house_date': '0',
        'suppliers': 'Altersense LMTd',
        'last_purchase_rate': '0',
        'last_6_month_consumption': '0'
    },
    {
        'item_name': 'hikvision',
        'uom': 'pcs',
        'qty': '17',
        'size': '',
        'type_data': '',
        'brand_data': 'hikvision',
        'model_data': '',
        'item_group': 'Accessories',
        'relevant_zone': '',
        'description': '',
        'schedule_date': '27-09-2022',
        'stock_in_hand': '0',
        'last_in_house_date': '0',
        'suppliers': 'Altersense LMTd',
        'last_purchase_rate': '0',
        'last_6_month_consumption': '0'
    },
    {
        'item_name': '16 port',
        'uom': 'pcs',
        'qty': '17',
        'size': '',
        'type_data': '',
        'brand_data': '',
        'model_data': '',
        'item_group': 'Accessories',
        'relevant_zone': '',
        'description': '',
        'schedule_date': '27-09-2022',
        'stock_in_hand': '0',
        'last_in_house_date': '0',
        'suppliers': 'Altersense LMTd',
        'last_purchase_rate': '0',
        'last_6_month_consumption': '0'
    },
    {
        'item_name': 'ADP Origin',
        'uom': 'box',
        'qty': '17',
        'size': '',
        'type_data': '',
        'brand_data': '',
        'model_data': '',
        'item_group': 'Accessories',
        'relevant_zone': '',
        'description': '',
        'schedule_date': '27-09-2022',
        'stock_in_hand': '0',
        'last_in_house_date': '0',
        'suppliers': 'Altersense LMTd',
        'last_purchase_rate': '0',
        'last_6_month_consumption': '0'
    },
    {
        'item_name': 'Rj 45',
        'uom': 'pcs',
        'qty': '17',
        'size': '',
        'type_data': '',
        'brand_data': '',
        'model_data': '',
        'item_group': 'Accessories',
        'relevant_zone': '',
        'description': '',
        'schedule_date': '27-09-2022',
        'stock_in_hand': '0',
        'last_in_house_date': '0',
        'suppliers': 'Altersense LMTd',
        'last_purchase_rate': '0',
        'last_6_month_consumption': '0'
    }
]

col = {"item_name": "", "uom": "", "qty": "", "size": "", "type_data": "", "brand_data": "", "model_data": "",
       "item_group": "", "relevant_zone": "", "description": "", "schedule_date": "", "stock_in_hand": "",
       "last_in_house_date": "", "suppliers": "", "last_purchase_rate": "", "last_6_month_consumption": ""}
for c in data:

    if c['item_name']:
        col['item_name'] = "Product Name"
        print("produt group: ", col)
    if c['uom']:
        col['uom'] = "UoM"
        print("UoM: ", col)

    if c['qty']:
        col['qty'] = "Required Qty"
        print("Required Qty: ", col)

    if c['size']:
        col['size'] = "Size"
        print("Size: ", col)

    if c['type_data']:
        col['type_data'] = "Type"
        print("Type: ", col)

    if c['brand_data']:
        col['brand_data'] = "Brand"
        print("Brand: ", col)

    if c['model_data']:
        col['model_data'] = "Model"
        print("Model: ", col)

    if c['item_group']:
        col['item_group'] = "Group"
        print("Group: ", col)

    if c['relevant_zone']:
        col['relevant_zone'] = "Relevant Zone"
        print("Relevant Zone: ", col)

    if c['description']:
        col['description'] = "Description"
        print("Description: ", col)

    if c['schedule_date']:
        col['schedule_date'] = "Rquired Date"
        print("Required Date: ", col)

    if c['stock_in_hand']:
        col['stock_in_hand'] = "Stock in Hand"
        print("Stock in Hand: ", col)

    if c['last_in_house_date']:
        col['last_in_house_date'] = "Last in House Date"
        print("Last in House Date: ", col)

    if c['suppliers']:
        col['suppliers'] = "Suppliers"
        print("Suppliers: ", col)

    if c['last_purchase_rate']:
        col['last_purchase_rate'] = "Last Purchase Rate"
        print("Last Purchase Rate: ", col)

    if c['last_6_month_consumption']:
        col['last_6_month_consumption'] = "Last 6 Month Consumption"
        print("Last 6 Month Consumption: ", col)
print("final col: ", col)
