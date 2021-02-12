# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

# Blood test analysis program
total_cholestrol = 70
ldl = 30
triglyceride = 120

low_cholesterol = total_cholestrol < 200
low_ldl = ldl < 100
low_triglyceride = triglyceride < 150

medium_cholesterol = 200 < total_cholestrol < 240
medium_ldl = 130 < ldl < 160
medium_triglyceride = 150 <= triglyceride < 200

high_cholesterol = 200 < total_cholestrol > 240
high_ldl = ldl > 160
high_triglyceride = triglyceride >= 200

if low_cholesterol and low_ldl and low_triglyceride:
    # good level
    print('*** Good level of cholestrol ***')
elif high_cholesterol or high_ldl or high_triglyceride:
    # High cholestrol level
    print('*** High cholestrol level ***')
    print('start taking pills such as statins')
    print('start TLC diet')
elif medium_cholesterol or medium_ldl or medium_triglyceride:
    #TLC_diet
    print('*** Borderline to moderately elevated ***')
    print("Start TLC diet")
    print("Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
    print('Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
    print('oats, barley, and other whole grains.')
    print('fruits such as apples, pears, bananas, and oranges.')
else:
    print('Error: unhandled case.')
