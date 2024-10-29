import math as m

def solar_pv_sizing(building_width, building_length, roof_angle, pv_width, pv_height, pv_power):
    
    #roof angle in radians
    roof_angle_rad = m.radians(roof_angle)
    
    #adjusted roof width in meters
    adj_roof_width = building_width/m.cos(roof_angle_rad) 
    
    #adjusted roof width in meters
    adj_roof_length = building_length

    #adjust width & height
    adj_pv_width = pv_width/1000
    adj_pv_height = pv_height/1000

    # number of pv panels needed
    num_pv_panels = m.floor(adj_roof_width//adj_pv_width) * m.floor(adj_roof_length//adj_pv_height)

    #total capacity in KWp
    total_capacity = num_pv_panels * pv_power / 1000

    print("The number of possible panels is: ", num_pv_panels)
    print("The total capacity in KWp is: ", total_capacity)
    return

Solar_setup_result = solar_pv_sizing(8, 28, 22, 1690, 1046, 400)