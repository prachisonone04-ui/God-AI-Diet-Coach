import streamlit as strl
import time

UI_TEXT = {
    "en": {"title": "God AI Diet Coach 🍏 (100% Pure Veg)", "weight": "Weight (kg)", "height": "Height (cm)", "age": "Age (Years)", "goal": "Your Goal", "lose": "Weight Loss", "gain": "Weight Gain", "btn": "Ask God AI 🚀", "res": "God AI Detailed Response:"},
    "hi": {"title": "गॉड एआई डाइट कोच 🍏 (100% शुद्ध शाकाहारी)", "weight": "वजन (किलोग्राम)", "height": "लंबाई (सेंटीमीटर)", "age": "उम्र (वर्ष)", "goal": "आपका लक्ष्य", "lose": "वजन घटाना", "gain": "वजन बढ़ाना", "btn": "गॉड एआई से पूछें 🚀", "res": "गॉड एआई विस्तृत जवाब:"},
    "mr": {"title": "गॉड एआय डाएट कोच 🍏 (100% शुद्ध शाकाहारी)", "weight": "वजन (किग्रॅ)", "height": "उंची (सेमी)", "age": "वय (वर्षे)", "goal": "तुमचे ध्येय", "lose": "वजन कमी करणे", "gain": "वजन वाढवणे", "btn": "गॉड एआयला विचारा 🚀", "res": "गॉड एआय सविस्तर उत्तर:"}
}

def generate_diet_plan(weight, height, age, goal, lang):
    time.sleep(1.8) # Loading feel sathi
    
    if lang == "mr":
        plan_type = "वजन कमी करण्यासाठी" if goal == "lose" else "वजन वाढवण्यासाठी"
        calories = "१५००-१७०० kcal (कमी कॅलरी)" if goal == "lose" else "२५००-२७०० kcal (हाय कॅलरी)"
        protein_source = "पनीर, सोयाबीन, मूग आणि मसूर डाळ" if goal == "lose" else "पनीर, चीज, बदाम, शेंगदाणे आणि केळी"
        
        return f"""
        ## 📊 तुमचा सविस्तर आणि संपूर्ण शाकाहारी डाएट प्लॅन
        **लक्ष्य:** {plan_type} | **लक्ष्य कॅलरी:** {calories}
        
        ---
        
        ### 🌅 १. सकाळी लवकर (Early Morning - 06:30 AM)
        *   १ ग्लास कोमट पाण्यात लिंबू रस आणि १ चमचा मध.
        *   सोबत ५ भिजवलेले बदाम आणि २ अक्रोड.
        
        ### 🥞 २. सकाळचा नाश्ता (Breakfast - 08:30 AM)
        *   **ऑप्शन १:** ओट्स उपमा किंवा शेवयांचा उपमा (भरपूर भाज्या टाकून).
        *   **ऑप्शन २:** २ मऊ कापडावर शेकलेले मेथीचे पराठे किंवा मूग डाळीचे धिरडे (चीला).
        *   **पेय:** १ ग्लास ताजे दूध किंवा १ वाटी दही.
        
        ### 🍎 ३. दुपारचा मधला वेळ (Mid-Meal Snack - 11:00 AM)
        *   १ ताजे हंगामी फळ (सफरचंद, पेरू किंवा १ वाटी पपई).
        *   १ ग्लास ताजे आणि थंडगार ताक (जिरेपूड टाकून).
        
        ### 🍲 ४. दुपारचे जेवण (Lunch - 01:30 PM)
        *   २ चपात्या (किंवा ज्वारी/बाजरीची भाकरी).
        *   १ मोठी वाटी प्रोटीनयुक्त डाळ (तूर, मूग किंवा मसूर).
        *   १ वाटी हिरवी पालेभाजी (पालक, मेथी किंवा शेपू).
        *   १ छोटी वाटी पनीर भुर्जी किंवा उकडलेले सोया चंक्स.
        *   **सलाड:** भरपूर गाजर, काकडी आणि बीट यांचे मिश्रण.
        
        ### ☕ ५. संध्याकाळचा नाश्ता (Evening Snack - 05:30 PM)
        *   १ कप ग्रीन टी किंवा गुळाचा चहा.
        *   १ वाटी भाजलेले मखाने (फॉक्स नट्स) किंवा सुका मेवा.
        
        ### 🥗 ६. रात्रीचे जेवण (Dinner - 08:00 PM)
        *   १ वाटी दलिया खिचडी किंवा लसूणी मूग डाळ खिचडी.
        *   १ वाटी मिक्स व्हेजिटेबल सूप किंवा पनीर सॅलड.
        *   *टीप:* रात्रीचे जेवण हलके आणि पचनास सोपे असावे.
        
        ---
        
        ### 💡 गॉड एआय खास टिप्स (God AI Important Tips):
        1.  **पाण्याचे प्रमाण:** तुमच्या {weight}kg वजनानुसार दिवसातून किमान ३ ते ४ लिटर पाणी पिणे अनिवार्य आहे.
        2.  **मुख्य प्रोटीन:** शाकाहारी आहारात प्रोटीनसाठी **{protein_source}** चा वापर वाढवा.
        3.  **झोप:** दररोज ७-८ तासांची शांत झोप घ्या, ज्यामुळे शरीराची रिकव्हरी वेगाने होईल.
        """
        
    elif lang == "hi":
        plan_type = "वजन घटाने" if goal == "lose" else "वजन बढ़ाने"
        calories = "1500-1700 kcal" if goal == "lose" else "2500-2700 kcal"
        protein_source = "पनीर, सोयाबीन और मूंग दाल" if goal == "lose" else "पनीर, चीज, बादाम और केला"
        
        return f"""
        ## 📊 आपका विस्तृत और 100% शाकाहारी डाइट प्लान
        **लक्ष्य:** {plan_type} | **लक्षित कैलोरी:** {calories}
        
        ---
        
        ### 🌅 1. सुबह जल्दी (Early Morning - 06:30 AM)
        *   1 गिलास गुनगुने पानी में नींबू का रस।
        *   साथ में 5 भीगे हुए बादाम और 2 अखरोट।
        
        ### 🥞 2. सुबह का नाश्ता (Breakfast - 08:30 AM)
        *   **विकल्प 1:** ओट्स चीला या सूजी का उपमा (सब्जियों के साथ)।
        *   **विकल्प 2:** 2 भरवां मेथी पराठे या अंकुरित मूंग (स्प्राउट्स) सलाद।
        *   **पेय:** 1 गिलास गर्म दूध या 1 कटोरी फ्रेश दही।
        
        ### 🍎 3. दोपहर का स्नैक (Mid-Meal Snack - 11:00 AM)
        *   1 मौसमी फल (सेब, अमरूद या पपीता)।
        *   1 गिलास भुने जीरे वाला छाछ (मट्ठा)।
        
        ### 🍲 4. दोपहर का भोजन (Lunch - 01:30 PM)
        *   2 चपाती (गेहूं या मल्टीग्रेन)।
        *   1 बड़ी कटोरी गाढ़ी दाल (मूंग/अरहर)।
        *   1 कटोरी हरी सब्जी (पालक/तोरई/टिंडा)।
        *   100 ग्राम लो-फैट पनीर भुर्जी या सोयाबीन बड़ी।
        *   **सलाद:** एक प्लेट खीरा, टमाटर और गाजर।
        
        ### ☕ 5. शाम का नाश्ता (Evening Snack - 05:30 PM)
        *   1 कप ग्रीन टी या बिना चीनी की ब्लैक कॉफी।
        *   1 कटोरी भुने हुए मखाने।
        
        ### 🥗 6. रात का खाना (Dinner - 08:00 PM)
        *   1 कटोरी ओट्स खिचडी या मिक्स वेज दलिया।
        *   1 कटोरी गरम टमाटर/सब्जी का सूप।
        
        ---
        
        ### 💡 गॉड एआई विशेष टिप्स:
        1.  **पानी:** आपके {weight}kg वजन के अनुसार दिन में 3-4 लीटर पानी पीना बहुत जरूरी है।
        2.  **प्रोटीन:** शाकाहार में मांसपेशियों के लिए **{protein_source}** सबसे उत्तम हैं।
        3.  **परहेज:** तली-भुनी चीजें, मैदा और चीनी से पूरी तरह दूरी बनाए रखें।
        """
        
    else:
        plan_type = "Weight Loss" if goal == "lose" else "Weight Gain"
        calories = "1500-1700 kcal" if goal == "lose" else "2500-2700 kcal"
        protein_source = "Paneer, Tofu, and Sprouts" if goal == "lose" else "Paneer, Peanut Butter, Nuts, and Bananas"
        
        return f"""
        ## 📊 Your Detailed & 100% Pure Vegetarian Diet Plan
        **Goal:** {plan_type} | **Target Energy:** {calories}
        
        ---
        
        ### 🌅 1. Early Morning (06:30 AM)
        *   1 glass of lukewarm water with lemon juice.
        *   5 soaked almonds and 2 walnuts.
        
        ### 🥞 2. Healthy Breakfast (08:30 AM)
        *   **Option 1:** Vegetable Oats Upma or Poha with roasted peanuts.
        *   **Option 2:** 2 Moong Dal Cheelas loaded with grated paneer.
        *   **Beverage:** 1 glass of low-fat milk or a bowl of fresh curd.
        
        ### 🍎 3. Mid-Meal Refreshment (11:00 AM)
        *   1 fresh seasonal fruit (Apple, Pear, or Papaya bowl).
        *   1 glass of refreshing buttermilk with roasted cumin powder.
        
        ### 🍲 4. Wholesome Lunch (01:30 PM)
        *   2 Whole wheat chapatis or Multi-grain rotis.
        *   1 large bowl of thick Dal (Tadka or Plain).
        *   1 bowl of seasonal green vegetables (Spinach, Bottle gourd, etc.).
        *   100g of Grilled Paneer or Soya chunks curry.
        *   **Salad:** A generous portion of Cucumber, Carrot, and Beetroot.
        
        ### ☕ 5. Evening Fuel (05:30 PM)
        *   1 cup of herbal Green Tea.
        *   1 bowl of roasted Makhana (Fox nuts) or a handful of roasted chana.
        
        ### 🥗 6. Light Dinner (08:00 PM)
        *   1 bowl of Moong Dal Khichdi or Vegetable Dalia.
        *   1 bowl of warm homemade vegetable soup.
        
        ---
        
        ### 💡 God AI Executive Tips:
        1.  **Hydration:** Considering your weight of {weight}kg, drinking 3-4 liters of water daily is crucial.
        2.  **Protein Supply:** Prioritize **{protein_source}** to complete your vegetarian protein goals.
        3.  **Consistency:** Avoid late-night snacking and maintain a 2-hour gap between dinner and sleep.
        """

strl.set_page_config(page_title="God AI Diet Coach", page_icon="🍏", layout="centered")

lang = strl.selectbox("🌐 Select Language / भाषा निवडा", ["en", "hi", "mr"], format_func=lambda x: "English" if x=="en" else "हिंदी" if x=="hi" else "मराठी")
text = UI_TEXT[lang]

strl.title(text["title"])
strl.write("---")

weight = strl.number_input(text["weight"], min_value=1, max_value=200, value=70)
height = strl.number_input(text["height"], min_value=50, max_value=250, value=170)
age = strl.number_input(text["age"], min_value=1, max_value=100, value=25)
goal_val = strl.selectbox(text["goal"], ["lose", "gain"], format_func=lambda x: text["lose"] if x=="lose" else text["gain"])

if strl.button(text["btn"], use_container_width=True):
    with strl.spinner("🧠 God AI is analyzing your metrics..."):
        result = generate_diet_plan(weight, height, age, goal_val, lang)
        strl.success(text["res"])
        strl.write(result)