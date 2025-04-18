def evaluate_outfit_score(weather, outfit):
    """ 
    Evaluates how appropriate a player's outfit is for the day based on the 
    weather, and if a player uses an accessory that is suitable for the weather, 
    they get a bonus. 
    
    Parameters:
    outfit (dict): Contains 'warmth', 'waterproof', and optional 'accessories' (list).
    weather (dict): Contains 'temperature' (int) and 'condition' (str).
    
    Returns:
    An int that ranges from 0 to 100
    """
    score = 100
    temp = weather['temperature']
    condition = weather['condition']
    
    if temp < 40: 
        ideal_cloth_warmth = 9
    elif 40 <= temp < 60:
        ideal_cloth_warmth = 7
    elif 60 <= temp < 75:
        ideal_cloth_warmth = 5
    else:
        ideal_cloth_warmth = 3 
    
    actual_warmth = outfit.get('warmth', 5)
    warmth_gap = abs(ideal_cloth_warmth - actual_warmth)
    score -= warmth_gap * 5

    if condition == 'rainy' and not outfit.get('waterproof', False):
        score -= 20
    if condition == 'snowy' and not outfit.get('waterproof', False):
        score -= 20
    if condition == 'sunny' and actual_warmth > 6:
        score -= 10

    accessories = outfit.get('accessories', [])
    
    expected = {
        'rainy': 'umbrella',
        'sunny': 'sunglasses',
        'cold': 'hat'
    }

    """ 
    If a player uses an accessory that is appropriate for the weather, they are 
    given a bonus score and if not appropriate, they are slightly penalized.
    """
    if condition == 'rainy' and 'umbrella' in accessories:
        score += 5
    elif 'umbrella' in accessories:
        score -= 2  
    
    if condition == 'sunny' and 'sunglasses' in accessories:
        score += 5
    elif 'sunglasses' in accessories:
        score -= 2

    if temp < 40 and 'hat' in accessories:
        score += 5
    elif temp >= 70 and 'hat' in accessories:
        score -= 2  

    score = max(0, min(score, 100))
    
    return score

weather1 = {'temperature': 28, 'condition': 'snowy'}
outfit1 = {'warmth': 9, 'waterproof': True, 'accessories': ['hat']}
print("Test 1:", evaluate_outfit_score(weather1, outfit1)) 

weather1 = {'temperature': 75, 'condition': 'sunny'}
outfit1 = {'warmth': 5, 'waterproof': True, 'accessories': ['hat']}
print("Test 1:", evaluate_outfit_score(weather1, outfit1)) 
